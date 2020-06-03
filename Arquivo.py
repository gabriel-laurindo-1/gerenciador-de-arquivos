import csv

class Arquivo:
    def __init__(self, diretorio, nome, extensao, tamanho):
        super().__init__()
        self.__nome = nome
        self.__extensao = extensao
        self.__diretorio = diretorio
        self.__tamanho = tamanho
        self.__objArquivoLido = ''
        self.__conteudo = []
        self.__endereco =  self.__diretorio + "/" + self.__nome + self.__extensao

    #Getter
    @property
    def nome(self):
        return self.__nome

    @property
    def nomeCompleto(self):
        return f'{self.__nome}{self.__extensao}'

    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def conteudo(self):
        return self.__conteudo


    def ler(self, delimitador=',', linhasIgnoradas=0):
        remove = 0
        with open(self.__endereco, 'r') as dataFile:
            self.__objArquivoLido = csv.reader(dataFile, delimiter=delimitador)
            for linha in self.__objArquivoLido:
                if remove >= linhasIgnoradas:
                    self.__conteudo.append(linha)
                remove += 1

    def escrever(self, texto):
        with open(self.__nome, 'a') as dataFile:
            dataFile.write(texto)

               
    
   
