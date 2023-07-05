from cliente import Cliente
from cliente import Pessoa
import carro
import datetime
import mysql.connector
conexao = mysql.connector.connect(
  host = "db4free.net",
  user = "mcqueen",
  password = "mcqueen123",
  database = "mcqueen"
)

cursor = conexao.cursor()

class Aluguel:
    def __init__(self,idCliente,idCarro,idAluguel):
       self.idCliente = idCliente
       self.idCarro = idCarro
       self.idAluguel = idAluguel

    def informacao_carro(self):
        # sql = f"select modelo, valor_aluguel from carros where idcarros = {self.idCarro}"
        sql = f"select * from carros where idcarros = {self.idCarro}"
        cursor.execute(sql)
        resultadoCarro = cursor.fetchall()
        carro = resultadoCarro[0]
        self.carro = carro
        print("\nDescrição do carro alugado:\n")
        for linha in resultadoCarro:
          print(f"modelo: {linha[1]} - {linha[2]} ({linha[3]})")
          print(f"Combustivel:",linha[4])
          print(f"Porte {linha[5]} - Câmbio {linha[6]}")
          print("Quantidade de Portas:",linha[7])
          print("Quantidade de passageiros suportado:",linha[8],"\n")

    def informacao_cliente(self):
        sql = f"select nome, cartao from clientes where idCPF = {self.idCliente}"
        cursor.execute(sql)
        resultadoCliente = cursor.fetchall()
        cliente = resultadoCliente[0]
        self.cliente = cliente

    def valor_aluguel(self, dias):
        valor_total = dias * self.carro[9]
        self.dias_alugados = dias
        self.valor_total = valor_total
        print(f"Total de dias alugados: {dias}.\nFicará no valor de: R${valor_total:.2f}" )
    
    def datas(self,saida,retorno_previo):
        self.data_saida = saida
        self.data_retorno_previo = retorno_previo
        if saida >= retorno_previo:
            print("Data incorreta.")
            return False

        print(f"Data de saída: {self.data_saida} \nData previa de retorno: {self.data_retorno_previo}")
        return True

    def retorno_multa(self,retorno):
        data_previa = datetime.datetime.strptime(self.data_retorno_previo, '%Y-%m-%d')
        data_retorno = datetime.datetime.strptime(retorno,'%Y-%m-%d')
        data_saida = datetime.datetime.strptime(self.data_saida, '%Y-%m-%d')
        diferenca_dias = abs((data_previa - data_retorno).days)
        multa = self.carro[9] * diferenca_dias * 1.2

        if data_retorno < data_saida:
            print("Data de retorno menor que data de saída.")
            return False
        elif data_retorno != data_previa:
            print(f"Carro retornado com {diferenca_dias} dias de atraso.")
            print(f"Diferença a pagar: R${multa:.2f}")
        else: 
            print("Sem multa!")
        return True

        self.data_retorno = data_retorno
        self.multa = multa

    def pagamento(self,pgto):
        if pgto == "cartao":
            Cliente.validar_cartao(self.cliente[1])
        elif pgto == "dinheiro":
            print("Receber...")
        self.pgto = self.cliente[1]
    
    def salvar_aluguel(self):
        cursor=conexao.cursor()
        sql = f"INSERT INTO aluguel (idCarro, idCliente, dias_alugados, valor_total, dia_saida, previsao_retorno, \
                forma_pagamento) VALUES ('{self.idCarro}','{self.idCliente}','{self.dias_alugados}','{self.valor_total}','{self.data_saida}',\
                '{self.data_retorno_previo}','{self.pgto}')"
        cursor.execute(sql)
        conexao.commit()

    def atualizar_aluguel(self):
        cursor=conexao.cursor()
        sql = f"UPDATE aluguel SET valor_multa = '{self.multa}', retorno = '{self.data_retorno}' WHERE idaluguel = '{self.idAluguel}'"
        cursor.execute(sql)
        conexao.commit()


alugando = Aluguel("18447009092","1","4")
alugando.informacao_carro()

dt = alugando.datas("2020-01-02","2020-01-03")
if dt == False:
    raise Exception()

alugando.valor_aluguel(5)

ret_multa = alugando.retorno_multa("2020-01-01")
if ret_multa == False:
    raise Exception()
# alugando.informacao_cliente()
# alugando.pagamento("cartao")
# alugando.salvar_aluguel()
# alugando.atualizar_aluguel()
  
