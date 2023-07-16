from cliente import Cliente
from cliente import Pessoa
import carro
import datetime
import mysql.connector
conexao = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "mcqueen"
)

cursor = conexao.cursor()

class Aluguel:
    def __init__(self,idCliente,idCarro):
       self.idCliente = idCliente
       self.idCarro = idCarro

    def informacao_carro(self):
        # sql = f"select modelo, valor_aluguel from carros where idcarros = {self.idCarro}"
        sql = f"select * from carros where idcarros = {self.idCarro}"
        cursor.execute(sql)
        resultadoCarro = cursor.fetchall()
        if len(resultadoCarro) == 0:
            print("Carro sem cadastro.\n")
            return False
        else: 
            carro = resultadoCarro[0]
            self.carro = carro
            print("\nDescrição do carro alugado:\n")
            for linha in resultadoCarro:
                mostrar_informacao_carro(linha)

    def informacao_cliente(self):
        sql = f"select nome, cartao from clientes where idCPF = {self.idCliente}"
        cursor.execute(sql)
        resultadoCliente = cursor.fetchall()
        if len(resultadoCliente) == 0:
            print("\nCliente sem cadastro.")
            return False
        else:
            cliente = resultadoCliente[0]
            self.cliente = cliente
            print("Cliente",self.cliente[0],"\n")
        return True

    def valor_aluguel(self, dias):
        valor_total = dias * self.carro[9]
        self.dias_alugados = dias
        self.valor_total = valor_total
        print(f"\nTotal de dias alugados: {dias}.\nFicará no valor de: R${valor_total:.2f}\n" )
    
    def datas(self,saida,retorno_previo):
        self.data_saida = saida
        self.data_retorno_previo = retorno_previo
        if saida >= retorno_previo:
            print("Data incorreta.")
            return False

        print(f"\nData de saída e retorno prévio: {self.data_saida} / {self.data_retorno_previo}\n")
        return True

    def retorno_multa(self,retorno):
        cursor.execute(f"select * from aluguel where idcarro = {self.idCarro} and idcliente = {self.idCliente} and retorno is null")
        resultado_retorno = cursor.fetchall()
        if len(resultado_retorno) == 0:
            print("\nAluguel não encontrado")
            return False
        else:
            aluguel = resultado_retorno[0]
            valor_diaria = aluguel[4] / aluguel[3]

            data_retorno = datetime.datetime.strptime(retorno,'%Y-%m-%d')
            previsao_retorno = datetime.datetime.combine(aluguel[7], datetime.time())
            data_saida = datetime.datetime.combine(aluguel[6], datetime.time())

            diferenca_dias = abs((previsao_retorno - data_retorno).days)
            multa = valor_diaria * diferenca_dias * 1.3

            if data_retorno < data_saida:
                print("\nData de retorno menor que data de saída.\n")
                return False
            elif data_retorno != previsao_retorno:
                print(f"\nCarro retornado com {diferenca_dias} dias de atraso.")
                print(f"Diferença a pagar: R${multa:.2f}\n")
            else: 
                print("\nSem multa!")

            self.data_retorno = data_retorno
            self.multa = multa
        return True

    def pagamento(self,pgto):
        if pgto == "cartao":
            Cliente.validar_cartao(self.cliente[1])
        elif pgto == "dinheiro":
            print("\nReceber...")
        self.pgto = self.cliente[1]
    
    @staticmethod
    def listar_carros_disponiveis():
        sql = "select * from aluguel where retorno is null"
        cursor.execute(sql)
        alugueis = cursor.fetchall()
        
        carros_alugados = []
        for aluguel in alugueis:
            carros_alugados.append(aluguel[1])
        print(carros_alugados)

        sql2 = "select * from carros"
        cursor.execute(sql2)
        todos_carros = cursor.fetchall()

        def filtro(carro):
            return carro[0] not in carros_alugados

        carros_disponiveis = list(filter(filtro, todos_carros))
        print("\n--Carros disponiveis:-- \n")
        for carro_disponivel in carros_disponiveis:
            mostrar_informacao_carro(carro_disponivel)

    def salvar_aluguel(self):
        cursor=conexao.cursor()
        cursor.execute(f"select * from aluguel where idCarro = {self.idCarro} and retorno is null")
        alugueis_existentes = cursor.fetchall()
        if len(alugueis_existentes) > 0:
            print("\n!!!!!Carro indisponível!!!!!")
            return 

        sql2 = f"INSERT INTO aluguel (idCarro, idCliente, dias_alugados, valor_total, dia_saida, previsao_retorno, \
                forma_pagamento) VALUES ('{self.idCarro}','{self.idCliente}','{self.dias_alugados}','{self.valor_total}','{self.data_saida}',\
                '{self.data_retorno_previo}','{self.pgto}')"
        cursor.execute(sql2)
        conexao.commit()
    
    def corrigir_aluguel(self):
        cursor=conexao.cursor()
        
        cursor.execute(f"UPDATE aluguel SET dias_alugados = '{self.dias_alugados}', valor_total = '{self.valor_total}',\
                        dia_saida = '{self.data_saida}', previsao_retorno = '{self.data_retorno_previo}',\
                        forma_pagamento = '{self.pgto}' where idcarro = '{self.idCarro}'")
        conexao.commit()

    def registar_retorno(self,idCarro):
        cursor=conexao.cursor()
        cursor.execute(f"select * from aluguel where idcarro = '{self.idCarro}' and retorno is null")
        listados = cursor.fetchall()
        lista = listados[0]
        if lista[2] != self.idCliente:
            print("CPF de devolução diferente do CPF do contrato.\nTente novamente.\n")

            return False
        else:
            sql = f"UPDATE aluguel SET valor_multa = '{self.multa}', retorno = '{self.data_retorno}' WHERE idcarro = '{self.idCarro}'"
            cursor.execute(sql)
            conexao.commit()
        return True

    def consultar_aluguel():
        sql = f"select * from aluguel"
        cursor.execute(sql)
        linhas = cursor.fetchall()
        print("\nNúmero total de aluguel retornado: ",cursor.rowcount)
        print("Contratos:\n")
        for linha in linhas:
            print("ID aluguel:",linha[0])
            print("Carro alugado:",linha[1])
            print("Nome do cliente:", linha[2])
            print("Dias alugados:",linha[3])
            print("Dia de saida:",linha[6],)
            print("Data prévia de retorno", linha[7])
            print("Dia de retorno:",linha[8])
            print(f"Valor total de aluguel: R${linha[4]:.2f}")
            print(f"Valor de multa: R$ {linha[5]} \n")

def mostrar_informacao_carro(linha):
        print(f"Id carro: {linha[0]}")
        print(f"modelo: {linha[1]} - {linha[2]} ({linha[3]})")
        print(f"Combustivel:",linha[4])
        print(f"Porte {linha[5]} - Câmbio {linha[6]}")
        print("Quantidade de Portas:",linha[7])
        print("Quantidade de passageiros suportado:",linha[8],"\n") 
