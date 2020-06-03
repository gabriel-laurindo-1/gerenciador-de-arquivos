# Classe de carregamento de arquivos de dados para analise
# Autor: Gabriel Laurindo
# Data: 2020.04.05
# Versao: 0.1


import os
import shutil
from Gerenciador_de_Arquivos.Arquivo import Arquivo

class GerenciadorDeArquivos:
    def __init__(self, diretorio=None):
        super().__init__()
        self.__diretorioRaiz = diretorio
        self.__termoDeBusca = ''
        self.__listaDeArquivos = []
        self.__NumeroArquivosEncontrados = 0
        self.__arquivoSelecionado = ''
    
    #Getter
    @property
    def numeroDeArquivosEncontrados(self):
        return self.__NumeroArquivosEncontrados

    # Busca os arquivos com base no termo de pesquisa informado
    def buscarArquivos(self, palavraChave):
        for raiz, diretorios, arquivos in os.walk(self.__diretorioRaiz):
            for arquivo in arquivos:
                if palavraChave in arquivo:
                    self.__NumeroArquivosEncontrados += 1
                    caminho_completo = os.path.join(raiz, arquivo)
                    nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
                    tamanho_arquivo = os.path.getsize(caminho_completo)
                    self.__listaDeArquivos.append(Arquivo(raiz, nome_arquivo, extensao_arquivo, tamanho_arquivo))

    # Exibe a lista de arquivos encontrados
    def lista_arquivos(self):
        indice = 1
        print(f'N\t|\tArquivo')
        for arquivo in self.__listaDeArquivos:
            print(f'{indice}\t|\t{arquivo.nomeCompleto}')
            indice += 1
        print()

    # Retorna uma tupla com os nomes dos arquivos encontrados
    def get_ListaDeArquicos(self):
        lista = []
        for arquivo in self.__listaDeArquivos:
            lista.append(arquivo.endereco)
        return tuple(lista)

    # Retorna todos os arquivos existentes no diretorio raiz
    def exibir_arquivos_diretorio(self):
        indice = 1
        print(f'N\t|\tArquivo')
        arquivosDir = os.listdir(self.__diretorioRaiz)
        for arquivo in arquivosDir:
            print(f'{indice}\t|\t{arquivo}')
            indice += 1
        print()

    # Seleciona o arquivo a a ser gerenciado dentro da classe
    def selecionarArquivo(self, nArquivo):
        self.__arquivoSelecionado = nArquivo

    # Retorna o endereco do objeto do arquivo selecionado
    def __cursorArquivo(self, nomeArquivo=None):
        if nomeArquivo == None:
            nomeArquivo = self.__arquivoSelecionado
        for arquivo in self.__listaDeArquivos:
            if nomeArquivo == arquivo.nomeCompleto:
                return arquivo

    # Metodo interno para verificar a existencia do arquivo dentro do diretorio selecionado
    def __arquivoExiste(self):
        pass

    # Le os dados do arquivo selecionado
    def abrirArquivo(self, nomeArquivo=None):
        fileOpen = self.__cursorArquivo(nomeArquivo)
        fileOpen.ler()
        print(f'Arquivo {fileOpen.nomeCompleto} lido com sucesso !\n')

    # Retorna o conteudo do arquivo selecionado
    def acessarConteudo(self, nomeArquivo=None):
        fileContent = self.__cursorArquivo(nomeArquivo)
        return fileContent.conteudo

    # Move um arquivo selecionado para um novo diretorio
    def mover(self, nomeArquivo=None, novoDiretorio=None):
        fileMove = self.__cursorArquivo(nomeArquivo)
        shutil.move(fileMove.endereco, novoDiretorio)
        print(f'Arquivo {fileMove.nomeCompleto} movido para {novoDiretorio}\n')

    # Copia o arquivo selecionado
    def copiar(self, nomeArquivo=None):
        fileCopied = self.__cursorArquivo(nomeArquivo)
        novoDiretorio = fileCopied.endereco
        novoDiretorio = novoDiretorio.replace('.' , '(copia).')
        shutil.copy(fileCopied.endereco, novoDiretorio)
        print(f'Arquivo {fileCopied.nomeCompleto} copiado com sucesso!\n')

    # Apaga o arquivo selecionado
    def remover(self, nomeArquivo=None):
        fileRemoved = self.__cursorArquivo(nomeArquivo)
        if os.path.exists(fileRemoved.endereco): # verifica se o arquivo existe no diretorio
            os.remove(fileRemoved.endereco)
        print(f'Arquivo {fileRemoved.nomeCompleto} removido com sucesso!\n')

    # Renomeia o arquivo escolhido
    def remonear(self, nomeAtual=None, novoNome=None):
        fileRename = self.__cursorArquivo(nomeAtual)
        nomeNovo = fileRename.endereco.replace(nomeAtual, novoNome)
        os.rename(fileRename.endereco, nomeNovo)
        print(f'Arquivo {nomeAtual} renomeado para {novoNome}\n')

    # Cria um arquivo no diretorio raiz em que a classe esta
    def criar(self, nome, conteudo):
        pass


