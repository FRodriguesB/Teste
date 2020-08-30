import sqlite3

class Agenda():
    def __init__(self, id = 0, nome = "", telefone = ""):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.conexao = sqlite3.connect("banco.db")
 
    def inserir(self):
        try:
            c = self.conexao.cursor()
            c.execute("insert into agenda (nome, telefone) values ('" + self.nome + "', '" + self.telefone + "' )")
            self.conexao.commit()
            c.close()
            return "Registro cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção"
 
    def atualizar(self):
        try:
            c = self.conexao.cursor()
            c.execute("update agenda set nome = '" + self.nome + "', telefone = '" + self.telefone +  "' where id = " + str(self.id) + " ")
            self.conexao.commit()
            c.close()
            return "Registro atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração"
 
    def apagar(self, codigo):
        try:
            c = self.conexao.cursor()
            c.execute("delete from agenda where id = " + str(codigo) + " ")
            
            self.conexao.commit()
            c.close()
            return "Registro excluído com sucesso!"
        except OSError as err:
            print("OS error: {0}".format(err))
            return "Ocorreu um erro na exclusão"
 
    def buscar(self, nome):
        try:
            c = self.conexao.cursor()
            resultado = c.execute("select * from agenda where nome = '" + nome + "' ")

            res = resultado.fetchall()
     
            comp = (len(res))
            
            for linha in res:
                self.id = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
            c.close()

            if (comp != 0):
                return ("Busca feita com sucesso! o id é: %d" %self.id)
            else:
                self.id = 0
                self.telefone = ""
                return ("Nenhum registro encontrado")
                
        except OSError as err:
            print("OS error: {0}".format(err))
            return "Ocorreu um erro na busca do Registro"

