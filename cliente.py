import re
import phonenumbers
from phonenumbers import geocoder
import mysql.connector
conexao = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "mcqueen"
)
cursor = conexao.cursor()

class Pessoa:
  def __init__(self,cpf,nome,email,telefone): 
      self.cpf = cpf
      self.nome = nome
      self.email = email
      self.telefone = telefone

  def nomear(self):
    raise Exception("função não implementada")

  @staticmethod
  def validar_cpf(n_cpf):
    if len(n_cpf) != 11:
        print("CPF inválido.")
        return False

    soma = 0
    for i in range(0, 9):
        soma += int(n_cpf[i]) * (10 - i)
        resto = 11 - (soma % 11)
    if resto >9:
        resto = 0
    if resto != int(n_cpf[9]):
        print("CPF inválido..")
    else:
        soma = 0
        for i in range(0, 10):
            soma += int(n_cpf[i]) * (11 - i)
        resto = 11 - (soma % 11)
        if resto>9:
            resto = 0
        if resto != int(n_cpf[10]):
            print("CPF inválido...")
        else:
            print("CPF:",n_cpf)
      
        return True
 
  @staticmethod
  def validar_email(validar_email):
      validador = re.match(r'^[a-z-0-9_.+-]+@[a-z-0-9-]+\.[a-z-0-9]+', validar_email) 
      # https://www.hashtagtreinamentos.com/regular-expressions-no-python?gad=1&gclid=Cj0KCQjw4s-kBhDqARIsAN-ipH2bqCI7kZgefuTenHNH8UPIZenfYGzxF0zvxpc4c-h1WHBDIJv4RxYaAtqSEALw_wcB
      if validador is None:
            print("Ops. E-mail inválido.")
            return False

      print("E-mail:",validar_email)
      return True

  @staticmethod
  def validar_numero(numero): #https://pypi.org/project/phonenumbers/
      if len(numero) < 12:
            print("Número inválido. \nDigite o número com cód. postal do país(ex.'+55') e o DDD(ex'11')")
            return False

      try :
            tell_ajustado = phonenumbers.parse(numero)
            # print(tell_ajustado)
            local = geocoder.description_for_number(tell_ajustado, 'pt-br')
            formato = phonenumbers.format_number(tell_ajustado, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            print("Numero telefônico:",formato)
            print("DDD de : ", local)
      except:
            print("Erro no nº de telefone.")
            return False


class Cliente (Pessoa):
  def __init__(self,cpf,nome,email,telefone,cartao):
    super().__init__(cpf,nome,email,telefone)
    self.cartao = cartao

  def nomear(self):
    print(self.nome)

  @staticmethod
  def validar_cartao(n_cartao):
      if len(n_cartao) != 16:
          print ("Confira os números do seu cartão")
          return False

      cartao_formatado = ''
      for i in range(0,16,4):
          cartao_formatado = cartao_formatado + n_cartao[i:i+4] + '.'

      cartao_formatado = cartao_formatado[:-1]
      print(f'Cartão validado: {cartao_formatado}')
      return True

  def salvar_cliente_banco (self):
      cursor=conexao.cursor()
      sql = f"INSERT INTO clientes (idCPF, nome, email, telefone, cartao) VALUES ('{self.cpf}','{self.nome}','{self.email}','{self.telefone}','{self.cartao}')"
      cursor.execute(sql)
      conexao.commit()

  def alterar_cliente_banco(cpf,nome,email,telefone,cartao):
      cursor=conexao.cursor()
      sql = f"UPDATE clientes SET nome = '{nome}', email = '{email}',telefone = '{telefone}',cartao ='{cartao}' WHERE idCPF = '{cpf}'"
      cursor.execute(sql)
      conexao.commit()

  def consultar_clientes_banco():
      sql = "select * from clientes"
      cursor.execute(sql)
      linhas = cursor.fetchall()
      print("\nNúmero total de  registro retornado: ",cursor.rowcount)
      print("Clientes:\n")
      for linha in linhas:
          print("CPF:",linha[0])
          print("Nome:",linha[1])
          print("E-mail:",linha[2])
          print("Nº telefone:",linha[3])
          print("Nº Cartão:",linha[4],"\n")
  

class Funcionario (Pessoa):
  def __init__(self,cargo):
    super().__init__(cpf,nome,email,telefone)
    self.cargo = cargo
  
  def salvar_funciona_banco (self):
      cursor=conexao.cursor()
      sql = f"INSERT INTO ... (...) VALUES ('{...}','{...}','{...}','{...}')"
      cursor.execute(sql)
      conexao.commit()

  def alterar_funciona_banco(self):
      cursor=conexao.cursor()
      sql = f"UPDATE ... '"
      cursor.execute(sql)
      conexao.commit()

  def consultar_funciona_banco():
      sql = "select * from pessoas"
      cursor.execute(sql)
      linhas = cursor.fetchall()
      print("Número total de funcionário retornado: ",cursor.rowcount)
      for linha in linhas:
          print("CPF:",linha[0])
          print("Nome:",linha[1])
          print("E-mail:",linha[2])
          print("Nº telefone:",linha[3])
          print("Cargo ocupado:",linha[4],"\n")

