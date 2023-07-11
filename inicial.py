from cliente import Cliente, Pessoa
import carro
import mysql.connector
from aluguel import Aluguel
conexao = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
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
    print("5. Registrar retorno")
    print("0. Sair da Area Cliente")
    opcao = input("Digite o numero de sua escolha: ")

    if opcao == "1":
        while True: 
            cpf = input("Digite o CPF: ")
            cpf_validado = Pessoa.validar_cpf(cpf)  
            if cpf_validado == False:
                print("Ops.")
            else:
                break
        
        nome = input("Digite o nome: ")

        while True: 
            email = input("Digite o email: ")
            email_validado = Pessoa.validar_email(email)
            if email_validado == False:
                print("E-mail inválido.")
            else:
                break

        while True: 
            telefone = input("Digite o telefone: ")
            numero_validado = Pessoa.validar_numero(telefone)
            if numero_validado == False:
                print("Telefone inválido.")
            else:
                break

        while True: 
            cartao = input("Digite os 16 nº cartão: ")
            cartao_validado = Cliente.validar_cartao(cartao)
            if cartao_validado == False:
                print("Número do cartão inválido.")
            else:
                break
        
        print("\nInformações adicionadas:\n")

        cliente = Cliente(cpf,nome,email,telefone,cartao)
        cliente.nomear()
        cliente.salvar_cliente_banco()
        

    elif opcao == "2":
        while True:
            cpf = input("Digite o CPF:")
            cpf_validado = Pessoa.validar_cpf(cpf)  
            if cpf_validado == False:
                print("CPF inválido.")
            else:
                break

        nome = input("Atualize o nome: ")

        while True:    
            email = input("Atualize o e-mail: ")
            email_validado = Pessoa.validar_email(email)
            if email_validado == False:
                print("E-mail inválido.")
            else:
                break

        while True:
            telefone = input("Atualize o número: ")
            numero_validado = Pessoa.validar_numero(telefone)
            if numero_validado == False:
                print("Telefone inválido.")
            else:
                break

        while True:
            cartao = input("Atualize o cartão: ")
            cartao_validado = Cliente.validar_cartao(cartao)
            if cartao_validado == False:
                print("Número do cartão inválido.")
            else:
                break

        print("\n Cadastro atualizado:\n")
      
        Cliente.alterar_cliente_banco(cpf,nome,email,telefone,cartao)
        print("\n")

    elif opcao == "3":
        Cliente.consultar_clientes_banco()

    elif opcao == "4":
        while True:
            print("\nCarros indisponíveis:")
            Aluguel.listar_carros_disponiveis()

            cliente = input("Digite o CPF do cliente: ")
            carro = int(input("Digite o ID do veículo: "))
            alugando = Aluguel (cliente, carro)
            alugando.informacao_carro()
            alugando.informacao_cliente()


            quantidade_dia = int(input("Quando dias de aluguel: "))
            alugando.valor_aluguel(quantidade_dia)

            dia_saida = input("Dia de saída 'ano-mes-dia': ")
            dia_previa_retorno = input("Dia retorno prévio 'ano-mes-dia': ")
            dt = alugando.datas(dia_saida,dia_previa_retorno)
            if dt == False:
                raise Exception()

            pgto = input("Forma de pagamento: ")
            alugando.pagamento(pgto)
            alugando.salvar_aluguel()

            break

    elif opcao == "5":
        
        cliente = input("Digite o CPF do cliente: ")
        carro = int(input("Digite o ID do veículo: "))
        alugando = Aluguel(cliente,carro)

        dia_retorno = input("Dia retorno 'ano-mes-dia': ")
        res = alugando.retorno_multa(dia_retorno)
        alugando.atualizar_aluguel(carro)

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
        valor = int(input("Valor diária: "))
        
        carro.cadastroCarro(modelo,fabricante,ano,combustivel,porte,cambio,portas,ocupantes,valor)
    
    elif opcao == "2":
        idCarro= input("Digite o ID do carro ao ser atualizado: ")
        modelo= input("Digite o novo modelo do carro: ")
        ano= int(input("Digite o novo ano do carro: "))
        porte= input("Digite o porte do carro: ")
        cambio= input("Digite o câmbio do carro: ")
        valor= input("Digite o novo valor do aluguel: ")
        carro.atualizarCarro(idCarro, modelo, ano,porte,cambio,valor)

    elif opcao == "3":
        carro.exibirCarro()

    elif opcao == "4":
        modelo= input("Digite o ID do carro a ser excluído: ")
        carro.excluirCarro(modelo)

    elif opcao == "5":
        Aluguel.consultar_aluguel()

    elif opcao == "0":
        print("\nAté Logo...\n")
        break

    else:
        print("Opção inválida!")


else:
  print("opção incorreta!")
menu()