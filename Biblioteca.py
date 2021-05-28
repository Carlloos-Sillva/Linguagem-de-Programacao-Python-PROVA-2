class Livro:

    def __init__(self, registro, autor, editora, ano_publicacao, ano_aquisicao, data, lido):
        self.registro = registro
        self.autor = autor
        self.editora = editora
        self.ano_publicacao = ano_publicacao
        self.ano_aquisicao = ano_aquisicao
        self.data = data
        self.lido = lido

    def __repr__(self):
        return repr((self.registro))

    def busca_autor(self, autor):
        for i in Livros:
            if autor == i.autor:
                print(i)

    def busca_titulo(self, registro):
        for i in Livros:
            if registro == i.registro:
                print(i)

    def lido_livro(self, data):
         self.lido = 'Sim'
         self.data = data

    def info(self):
        print('********************************************************')
        print()
        print('Registro do titulo do livro..: ' + self.registro)
        print('O autor principal do livro...: ' + self.autor)
        print('A editora do livro...........: ' + self.editora)
        print('Ano de publicação do livro...: ' + str(self.ano_publicacao))
        print('Ano de aquisição do livro....: ' + str(self.ano_aquisicao))
        print('Data lido do livro...........: ' + str(self.data))
        print('Livro lido...................: ' + self.lido)

L1 = Livro('The Witcher - O Sangue dos Elfos', 'Sapkowski Andrzej', 'WMF Martins Fontes', 1994, 2020, 000, 'Sim')
L2 = Livro('O Senhor dos Anéis - As Duas Torres', 'J. R. R. Tolkien', 'HarperCollins Brasil', 2001, 2018, 000, 'Não')
L3 = Livro('Neuromancer: 1', 'Willian Gibson', 'Editora Aleph: 5ª edição', 1984, 2021, 000, 'Não')
L4 = Livro('A Guerra dos Tronos : As Crônicas de Gelo e Fogo, volume 1', 'George R. R. Martin', 'Suma 1ª edição', 1996, 2018, 000, 'Não')
L5 = Livro('Evangelho de Sangue: Bem vindo ao inferno', 'Clive Barker', 'Darkside; 1ª edição', 2007, 2015, 000, 'Sim')
L6 = Livro('Frankenstein: O clássico está vivo!', 'Mary Shelley', 'Darkside; 1ª edição', 1818, 2016, 000, 'Não')
L7 = Livro('Code Geass: Lelouch of the Rebellion', 'Ichirō Ōkouchi', 'Kadokawa Shoten', 2005, 2013, 000, 'Sim')

L1.info()# - Imprimir todos os Livros.
L2.info()# - Imprimir todos os Livros.
L3.info()# - Imprimir todos os Livros.
L4.info()# - Imprimir todos os Livros.
L5.info()# - Imprimir todos os Livros.
L6.info()# - Imprimir todos os Livros.
L7.info()# - Imprimir todos os Livros.

Livros = [L1,L2,L3,L4,L5,L6,L7]# Leitura de todos os Livros

print()
print('--------------------------------------------------------------')
print(' Lista de todos livros em ordem alfabética: ')
print()
print(sorted(Livros, key=lambda Livro: Livro.registro))

print()
print(' livros que foram lidos: ')
Livros[0].lido_livro(2020)
print()
print(' Busca do livro pelo autor: ')
Livros[0].busca_autor('J. R. R. Tolkien')
print()
print(' Busca pelo titulo: ')
Livros[0].busca_titulo('Neuromancer: 1')
