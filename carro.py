import mysql.connector
conexao = mysql.connector.connect(
  host = "db4free.net",
  user = "mcqueen",
  password = "mcqueen123",
  database = "mcqueen"
)

cursor = conexao.cursor()
def cadastroCarro(modelo,fabricante,ano,combustivel,porte,cambio,portas,ocupantes,valor):
    cursor=conexao.cursor()
    sql=f"INSERT INTO carros(modelo,fabricante,ano_lancamento,combustivel,porte,cambio,portas,ocupantes,valor_aluguel) VALUES ('{modelo}','{fabricante}','{ano}','{combustivel}','{porte}','{cambio}',{portas},{ocupantes},{valor})"
    cursor.execute(sql)
    conexao.commit()

def exibirCarro():
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM carros")
    carros= cursor.fetchall()
    for carro in carros:
        print(carro)

def atualizarCarro(idCarro,modelo,ano,porte,cambio,valor):
    cursor = conexao.cursor()
    sql = f"UPDATE carros SET modelo = '{modelo}', ano_lancamento = '{ano}',porte {porte},cambio {cambio},valor_aluguel{valor} WHERE idcarros = {idCarro}"
    cursor.execute(sql)
    conexao.commit()
    print("O carro foi atualizado com sucesso!")

def excluirCarro():
    cursor = conexao.cursor()
    sql = f"DELETE FROM carros WHERE id=2"
    cursor.execute(sql)
    conexao.commit()

    print("O carro foi excluído com sucesso!")

# def menu():
#     while True:
#         print("\n---Locadora---")
#         print("1. Adicionar Carros")
#         print("2. Visualizar Carros")
#         print("3. Atualizar Carros")
#         print("4. Excluir Carros")
#         print("0. Sair da Locadora.")
#         opcao = input("Digite a opção desejada: ")
        
#         if opcao == "1":
#             modelo = input("Digite o modelo do carro:\n")
#             fabricante= input("Digite o fabricante do carro:\n")
#             ano=input("Digite o ano do lançamento do carro:\n")
#             combustivel=input("Digite o tipo de combustivel do carro:\n")
#             porte=input("Digite o porte do carro:\n")
#             cambio=input("Digite o câmbio do carro:\n")
#             portas=input("Digite a quantas portas tem o carro:\n")
#             ocupantes=input("Digite quantas ocupantes o carro suporta:\n")
#             valor=input("Digite o valor do aluguel:")
#             cadastroCarro(modelo,fabricante,ano,combustivel,porte,cambio,portas,ocupantes,valor)
        
#         elif opcao == "2":
#             exibirCarro()
#         elif opcao == "3":
#             idCarro= input("Digite o ID do carro ao ser atualizado: ")
#             modelo= input("Digite o novo modelo do carro: ")
#             ano= int(input("Digite o novo ano do carro: "))
#             porte=int(input("Digite o porte do carro:"))
#             cambio=input("Digite o câmbio do carro:")
#             valor=float(input("Digite o novo valor do aluguel:"))
#             atualizarCarro(idCarro, modelo, ano,porte,cambio,valor)
#         elif opcao == "4":
#             modelo= input("Digite o modelo do carro a ser excluído: ")
#             excluirCarro()
#         elif opcao == "0":
#             break
#         else:
#             print("Opção inválida!")
# menu()
# conexao.close()