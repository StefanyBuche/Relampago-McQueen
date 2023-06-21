
import phonenumbers
from phonenumbers import geocoder

class Pessoa:
  def __init__(self,nome): 
      self.nome = nome
  def nomear(self):
      print("Nome Adicionado com sucesso:",self.nome)

class Celular (Pessoa):
  def __init__(self, nome, celular):
      super().__init__(nome)
      self.celular = celular
  def conferir_numero(self,numero):
      if len(numero) < 12:
        print("Número inválido. \nDigite o número com cód. postal do país(ex.'+55') e o DDD(ex'11')")
      else:
        tell_ajustado = phonenumbers.parse(numero)
        # print(tell_ajustado)
        local = geocoder.description_for_number(tell_ajustado, 'pt-br')
        # print(local)
        formato = phonenumbers.format_number(tell_ajustado, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        #https://pypi.org/project/phonenumbers/
        print("Numero telefônico adicionado com sucesso:",formato)

class Cpf (Pessoa):
  def __init__(self, nome, cpf):
    super().__init__(nome)
    self.cpf = cpf
  def validar_cpf(self,n_cpf):
    if len(n_cpf) != 11:
      print("CPF inválido.")
    else:
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
            print("CPF Adicionado com sucesso:",n_cpf)

# p =  input("Seu nome: ")
# n =  input("nº cllr: ")
# cpf = input("digite seu CPF sem os caracteres: ")
Pessoa('Carla').nomear()
Celular('Carla', '+5548999999999').conferir_numero('+5548999999999')
Cpf('Carla', '99999999999').validar_cpf('99999999999')
