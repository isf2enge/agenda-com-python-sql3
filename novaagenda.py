from abc import ABC,abstractmethod #importando o método abstract
import sqlite3
class Agenda(ABC):
    def __init__(self,conta,numero,telefone):
        self.__conta = conta
        self.__numero = numero
        self.__telefone = telefone

    @abstractmethod
    def trocanumero(self): #método abstrato
        pass

    def gettelefone(self): #Acesso ao encapsulamento,com get e set.
        return self.__telefone
    def settelefone(self,telefonenovo):
        self.__telefone = telefonenovo
    def getnumero(self): #Acesso ao encapsulamento,com get e set.
        return self.__numero
    def getconta(self): #Acesso ao encapsulamento,com get e set.
        return self.__conta


class Pessoa(Agenda):
    def __init__(self,conta,numero,telefone):
        super(Pessoa,self).__init__(conta,numero,telefone)
        # Criando o Banco de Dados:
        conexao = sqlite3.connect('Aagenda.db')
        # Criando o cursor:
        c = conexao.cursor()
    def trocanumero(self,numeronovo): #Função para trocar o número
        self.settelefone(numeronovo)
        return self.gettelefone()
    def armazenamento(self):   #Função para criar o banco de dados

        # Criando o Banco de Dados:
        conexao = sqlite3.connect('Agendat.db')
        # Criando o cursor:
        c = conexao.cursor()
        # Criando a tabela(colunas ou tipos de colunas):
        c.execute("""CREATE TABLE  IF NOT EXISTS  Agendat (
           conta TEXT,
            numero REAL,
            telefone REAL
            )""")

        # Inserir dados na tabela:
        c.execute("INSERT INTO Agendat VALUES (:conta,:numero,:telefone)", {
            'conta': self.getconta(),
            'numero': self.getnumero(),
            'telefone': self.gettelefone()
        })

        # Commit as mudanças:
        conexao.commit()

        # Fechar o banco de dados:
        conexao.close()




if __name__ == '__main__':
    mario = Pessoa('Mario',32,123456789)
    print(mario.armazenamento())


