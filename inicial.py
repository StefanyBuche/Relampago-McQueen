from cliente import Cliente, Pessoa
import carro
import mysql.connector
conexao = mysql.connector.connect(
  host = "db4free.net",
  user = "mcqueen",
  password = "mcqueen123",
  database = "mcqueen"
)

cursor = conexao.cursor()

print("\nMenu inicial da locadora McQueen\n")
usuario = input("Coloque seu nome de usuário: ")

if usuario == 'bruno':
  print("olá bruno")
  while True:
    print("\n--Area Cliente--\n")
    print("1. Cadastrar")
    print("2. Atualizar cadastro")
    print("3. Ver clientes")
    print("4. Fechar contrato de aluguel")
    print("0. Sair da Area Cliente")
    opcao = input("Digite o numero de sua escolha: ")

    if opcao == "1":
        cpf = input("Digite o CPF: ")
        cpf_validado = Pessoa.validar_cpf(cpf)         
        if cpf_validado == False:
          raise Exception()

        nome = input("Digite o nome: ")


        email = input("Digite o email: ")
        email_validado = Pessoa.validar_email(email)
        if email_validado == False:
          raise Exception()        

        telefone = input("Digite o telefone: ")
        numero_validado = Pessoa.validar_numero(telefone)
        if numero_validado == False:
          raise Exception()        

        cartao = input("Digite os 16 nº cartão: ")
        cartao_validado = Cliente.validar_cartao(cartao)
        if cartao_validado == False:
          raise Exception()        
        
        print("\nInformações adicionadas:\n")

        cliente = Cliente(cpf,nome,email,telefone,cartao)
        cliente.nomear()
        cliente.salvar_cliente_banco()
        

    elif opcao == "2":
        cpf = input("Digite o CPF:")
        nome = input("Atualize o nome: ")
        email = input("Atualize o e-mail: ")
        telefone = input("Atualize o número: ")
        cartao = input("Atualize o cartão: ")

        print("\n Cadastro atualizado:\n")
      
        cpf_validado = Pessoa.validar_cpf(cpf)         
        if cpf_validado == False:
          raise Exception()
        
        email_validado = Pessoa.validar_email(email)
        if email_validado == False:
          raise Exception()
        
        numero_validado = Pessoa.validar_numero(telefone)
        if numero_validado == False:
          raise Exception()

        cartao_validado = Cliente.validar_cartao(cartao)
        if cartao_validado == False:
          raise Exception()
        Cliente.alterar_cliente_banco(cpf,nome,email,telefone,cartao)
        print("\n")

    elif opcao == "3":
        Cliente.consultar_clientes_banco()

    elif opcao == "4":
      ...

    elif opcao == "0":
        print("\nAté logo...\n")
        break

    else:
        print("!!!Opção inválida!!!")
        
elif usuario == 'stefany' or usuario == 'julia':
  print("olá, bem-vindo")
  while True:
    print("\n--Area Aluguel--\n")
    print("1. Cadastrar Carro")
    print("2. Atualizar cadastro de carro")
    print("3. Ver Carros")
    print("4. Excluir carro")
    print("5. Ver alugueis")
    print("0. Sair da Area Aluguel.")
    opcao = input("Digite o numero de sua escolha: ")

    if opcao == "1":
        modelo = input("Digite o modelo do carro:\n")
        fabricante = input("Digite o fabricante do carro:\n")
        ano = input("Digite o ano do lançamento do carro:\n")
        combustivel = input("Digite o tipo de combustivel do carro:\n")
        porte = input("Digite o porte do carro:\n")
        cambio = input("Digite o câmbio do carro:\n")
        portas = int(input("Digite a quantas portas tem o carro:\n"))
        ocupantes = int(input("Digite quantas ocupantes o carro suporta:\n"))
        valor = float(input("Digite o valor do aluguel:"))
        carro.cadastroCarro(modelo,fabricante,ano,combustivel,porte,cambio,portas,ocupantes,valor)
    
    elif opcao == "2":
        idCarro= input("Digite o ID do carro ao ser atualizado: ")
        modelo= input("Digite o novo modelo do carro: ")
        ano= int(input("Digite o novo ano do carro: "))
        porte=int(input("Digite o porte do carro:"))
        cambio=input("Digite o câmbio do carro:")
        valor=float(input("Digite o novo valor do aluguel:"))
        carro.atualizarCarro(idCarro, modelo, ano,porte,cambio,valor)

    elif opcao == "3":
        carro.exibirCarro()

    elif opcao == "4":
        modelo= input("Digite o modelo do carro a ser excluído: ")
        carro.excluirCarro()

    elif opcao == "5":
        ...

    elif opcao == "0":
        print("\nAté Logo...\n")
        break

    else:
        print("Opção inválida!")


else:
  print("opção incorreta!")
menu()