from cliente import Cliente
from cliente import Pessoa
import carro
import mysql.connector
conexao = mysql.connector.connect(
  host = "db4free.net",
  user = "mcqueen",
  password = "mcqueen123",
  database = "mcqueen"
)

cursor = conexao.cursor()

class Aluguel:
    def __init__(self,idCliente,idCarro, aluguel):
       self.idCliente = idCliente
       self.idCarro = idCarro
       self.aluguel = aluguel
    def informacao_carro(self):
        sql = f"select modelo, valor_aluguel from carros where idcarros = {self.idCarro}"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        carro = resultado[0]
        self.carro = carro
        print("Carro valor:",carro[1])

    def alugar(self, dias):
        valor_total = dias * self.carro[1] 
        print(f"Total de dias alugados: {dias}. Ficará no valor de: R${valor_total:.2f}" )

    # def multa(self,valor):
        ...
        #multa = valor_do_carro * 1.2 * dias_atraso
        #multa_total = multa + valor_aluguel
  
alugando = Aluguel("33333333333","1","5")
alugando.informacao_carro()
alugando.alugar(7)
  
