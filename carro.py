import mysql.connector
conexao = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "mcqueen"
)

cursor = conexao.cursor()
def cadastroCarro(modelo,fabricante,ano,combustivel,porte,cambio,portas,ocupantes,valor):
    cursor=conexao.cursor()
    sql=f"INSERT INTO carros(modelo,fabricante,ano_lancamento,combustivel,porte,cambio,portas,ocupantes,valor_aluguel) \
          VALUES ('{modelo}','{fabricante}','{ano}','{combustivel}','{porte}','{cambio}',{portas},{ocupantes},{valor})"
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
    sql = f"UPDATE carros SET modelo = '{modelo}', ano_lancamento = '{ano}',porte = '{porte}',cambio = '{cambio}',valor_aluguel = {valor} WHERE idcarros = {idCarro}"
    cursor.execute(sql)
    conexao.commit()
    print("O carro foi atualizado com sucesso!")

def excluirCarro(idCarro):
    cursor = conexao.cursor()
    sql = f"DELETE FROM carros WHERE idcarros= {idCarro}"
    cursor.execute(sql)
    conexao.commit()

    print("O carro foi excluído com sucesso!")
