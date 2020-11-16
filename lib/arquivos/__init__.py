from lib.functions import *
def encontrarArquivo(arq):
    try:
        o = open(arq, 'rt')
        o.close()
    except FileNotFoundError:
        return False
    else:
        return True



def criarArquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('ERRO AO CRIAR ARQUIVO.')
    else:
        print(f'Arquivo {arq} criado com sucesso!')



def lerArquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('ERRO AO LER ARQUIVO.')
    else:
        print(a.read())

def arquivoCadastrar(arq, nome='Desconhecido', idade=0, plano = 'Nenhum', vencimento = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Encontrei um erro na hora de cadastrar no arquivo txt')
    else:
        try:
          a.write(f'\n{nome}      {idade} anos --> {plano} --> Vencimento do plano: {vencimento}\n')
          a.write('----------------------------------------')
        except:
          print('ERRO AO IMPRIMIR O TXT')
        finally:
          a.close()


def procurarNomeArquivo(arq, nome):
  a = open(arq, 'r')
  for f in a.readlines():
    if f.find(nome) > -1:
      linha()
      print('ENCONTRADO!\n\n')
      print(f'\033[1;93m{f}\033[1;32m')
      linha()

