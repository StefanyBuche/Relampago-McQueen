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

  def nomear(nome):
    raise Exception("função não implementada")

  @staticmethod
  def validar_cpf(n_cpf):
    if len(n_cpf) != 11:
        print("\nCPF inválido.\n")
        return False
    elif any(c.isalpha() for c in n_cpf):
          print("\nErro no numero do CPF, Pode estar contendo letras.\n")
          return False

    soma = 0
    for i in range(0, 9):
        soma += int(n_cpf[i]) * (10 - i)
        resto = 11 - (soma % 11)
    if resto >9:
        resto = 0
    if resto != int(n_cpf[9]):
        print("\nCPF inválido..\n")
    else:
        soma = 0
        for i in range(0, 10):
            soma += int(n_cpf[i]) * (11 - i)
        resto = 11 - (soma % 11)
        if resto>9:
            resto = 0
        if resto != int(n_cpf[10]):
            print("\nCPF inválido...\n")
        else:
            print("\nCPF:",n_cpf,"\n")
      
        return True
 
  @staticmethod
  def validar_email(validar_email):
      validador = re.match(r'^[a-z-0-9_.+-]+@[a-z-0-9]+\.[a-z-0-9]+', validar_email) 
      # https://www.hashtagtreinamentos.com/regular-expressions-no-python?gad=1&gclid=Cj0KCQjw4s-kBhDqARIsAN-ipH2bqCI7kZgefuTenHNH8UPIZenfYGzxF0zvxpc4c-h1WHBDIJv4RxYaAtqSEALw_wcB
      if validador is None:
            print("\nOps. E-mail inválido.\n")
            return False

      print("\nE-mail validado:",validar_email,"\n")
      return True

  @staticmethod
  def validar_numero(numero): #https://pypi.org/project/phonenumbers/
      if len(numero) < 12:
            print("\nNúmero inválido. \nDigite o número com cód. postal do país(ex.'+55') e o DDD(ex'11')\n")
            return False

      try :
            tell_ajustado = phonenumbers.parse(numero)
            # print(tell_ajustado)
            local = geocoder.description_for_number(tell_ajustado, 'pt-br')
            formato = phonenumbers.format_number(tell_ajustado, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            print("\nNumero telefônico:",formato)
            print("DDD de : ", local,"\n")
      except:
            print("\nErro no nº de telefone.\n")
            return False


class Cliente (Pessoa):
  def __init__(self,cpf,nome,email,telefone,cartao):
    super().__init__(cpf,nome,email,telefone)
    self.cartao = cartao

  @staticmethod
  def nomear(nome):
    if nome == '':
        print("\nCampo Vazio.")
        return False
    
    return True

  @staticmethod
  def validar_cartao(n_cartao):
      if len(n_cartao) != 16:
          print ("\nConfira os números do seu cartão\n")
          return False
      elif any(c.isalpha() for c in n_cartao):
          print("\nErro no numero do cartão, Pode estar contendo letras.\n")
          return False
      cartao_formatado = ''
      for i in range(0,16,4):
          cartao_formatado = cartao_formatado + n_cartao[i:i+4] + '.'

      cartao_formatado = cartao_formatado[:-1]
      print(f'\nCartão validado: {cartao_formatado} \n')
      return True

  def salvar_cliente_banco (self):
      cursor = conexao.cursor()
      sql = f"INSERT INTO clientes (idCPF, nome, email, telefone, cartao) VALUES ('{self.cpf}','{self.nome}','{self.email}','{self.telefone}','{self.cartao}')"
      cursor.execute(sql)
      conexao.commit()
      print("Contrato de aluguel concluído.")

  def alterar_cliente_banco(self):
      cursor=conexao.cursor()
      cursor.execute(f"select idCPF from clientes where idCPF = {self.cpf}")
      tabela = cursor.fetchall()
      
      if len(tabela) == 0:
        print(f"Cliente não encontrado")
        print("CPF do cliente não foi encontrado entre os contados salvos.")
        
      else:
        cursor.execute(f"UPDATE clientes SET nome = '{self.nome}', email = '{self.email}',telefone = '{self.telefone}',\
                        cartao ='{self.cartao}' WHERE idCPF = '{self.cpf}'")
        print("\nAtualizado com Sucesso.")
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

