import re
import phonenumbers
from phonenumbers import geocoder
import mysql.connector
conexao = mysql.connector.connect(
  host = "db4free.net",
  user = "mcqueen",
  password = "mcqueen123",
  database = "mcqueen"
)
cursor = conexao.cursor()

class Pessoa:
  def __init__(self,cpf,nome,email,telefone): 
      self.cpf = cpf
      self.nome = nome
      self.email = email
      self.telefone = telefone
       
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
  def validar_numero(numero):
      if len(numero) < 12:
          print("Número inválido. \nDigite o número com cód. postal do país(ex.'+55') e o DDD(ex'11')")
          return False

      tell_ajustado = phonenumbers.parse(numero)
      # print(tell_ajustado)
      local = geocoder.description_for_number(tell_ajustado, 'pt-br')
      formato = phonenumbers.format_number(tell_ajustado, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
      #https://pypi.org/project/phonenumbers/
      print("Numero telefônico:",formato)
      print("DDD de : ", local)
      return True


class Cliente (Pessoa):
  def __init__(self,cpf,nome,email,telefone,cartao):
    super().__init__(cpf,nome,email,telefone)
    self.cartao = cartao
  
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
      sql = f"INSERT INTO pessoas (idCPF, nome, email, telefone) VALUES ('{self.cpf}','{self.nome}','{self.email}','{self.telefone}')"
      cursor.execute(sql)
      conexao.commit()

  def alterar_funciona_banco(self):
      cursor=conexao.cursor()
      sql = f"UPDATE pessoas SET nome = '{self.nome}', email = '{self.email}',telefone = '{self.telefone}',cartao ='{self.cartao}' WHERE idCPF = '{self.cpf}'"
      cursor.execute(sql)
      conexao.commit()

  def consultar_funciona_banco():
      sql = "select * from pessoas"
      cursor.execute(sql)
      linhas = cursor.fetchall()
      print("Número total de  registro retornado: ",cursor.rowcount)
      print("Clientes:\n")
      for linha in linhas:
          print("CPF:",linha[0])
          print("Nome:",linha[1])
          print("E-mail:",linha[2])
          print("Nº telefone:",linha[3])
          print("Nº Cartão:",linha[4],"\n")



# def menu():
#     while True:
#         print("\n--Area Cliente--\n")
#         print("1. Cadastrar")
#         print("2. Atualizar cadastro")
#         print("3. Ver clientes")
#         opcao = input("Digite o numero de sua escolha: ")

#         if opcao == "1":
#           cpf = ""
#           nome = ""
#           email = ""
#           telefone = ""
#           cartao = ""
#           print("Informações adicionadas:\n")

#           cpf_validado = Pessoa.validar_cpf(cpf)         
#           if cpf_validado == False:
#             raise Exception()
          
#           email_validado = Pessoa.validar_email(email)
#           if email_validado == False:
#             raise Exception()
          
#           numero_validado = Pessoa.validar_numero(telefone)
#           if numero_validado == False:
#             raise Exception()
            
#           cartao_validado = Pessoa.validar_cartao(cartao)
#           if cartao_validado == False:
#             raise Exception()
        
#           pessoa = Pessoa(cpf, nome, email, telefone, cartao)
#           pessoa.salvar_no_banco()

#         elif opcao == "2":
#           cpf = input("Digite seu CPF:")
#           nome = input("Atualize seu nome: ")
#           email = input("Atualize seu e-mail: ")
#           telefone = input("Atualize seu número: ")
#           cartao = input("Atualize seu cartão: ")
          
#           cpf_validado = Pessoa.validar_cpf(cpf)         
#           if cpf_validado == False:
#             raise Exception()
          
#           email_validado = Pessoa.validar_email(email)
#           if email_validado == False:
#             raise Exception()
          
#           numero_validado = Pessoa.validar_numero(telefone)
#           if numero_validado == False:
#             raise Exception()

#           cartao_validado = Pessoa.validar_cartao(cartao)
#           if cartao_validado == False:
#             raise Exception()
          
#           pessoa = Pessoa(cpf, nome, email, telefone, cartao)
#           pessoa.alterar_no_banco()
#         elif opcao == "3":
#           consultar_clientes()
#         else:
#             print("!!!Opção inválida!!!")
        
# menu()
# conexao.close()