from datetime import date

def linha(tam = 42):
  print('-' * tam)

def linha2(tam):
  return '-' * tam


def lerInt(msg):
    try:
      rec = int(input(msg))
      return rec
    except ValueError:
      print('Digite um número inteiro e que tenha a opção acima!')
    except NameError:
      print('Digite um número inteiro e que tenha a opção acima!')



def planos():
  print('PLANOS DISPONÍVEIS NA ACADEMIA: ')
  print('[1] -- PLANO FORTX (MENSAL) R$130,00')
  print('[2] -- PLANO BODYPERFECT (TRIMENSAL) R$90,00 ')
  print('[3] -- PLANO PREMIUM (ANUAL) R$65,00\033[1;32m')
  c = int(input(('Digite o plano escolhido: ')))
  return c



def menuprincipal(lista):
  contador = 1
  data = date.today()
  formatando_data = (f'{data.day}/{data.month}/{data.year}')
  print(f'      BEM-VINDO! Hoje é: {formatando_data}!')
  linha()
  for item in lista:
    print(f'\033[1;94m{contador} ----> {item}\033[1;32m')
    linha()
    contador += 1
  c = int(input(('Digite a sua opção: ')))
  print()
  return c



'''def menu(lista):
  contador = 1
  for item in lista:
    print(f'{contador}º --> {item[0]} --> {item[1]} anos --> {item[2]} ---> Pagamento em: {item[3] - date.today()}')
    if (item[3] - date.today()) < (item[3] - item[3]):
      print('\033[1;31mALUNO ESTÁ COM A MENSALIDADE EM VENCIMENTO! ATENÇÃO: ENTRAR EM CONTATO.')
      print(f'\033[1;31mMENSALIDADE VENCIDA EM: {item[3]}\033[1;32m')
    linha()
    contador += 1
  return input('\nAPERTE ENTER PARA CONTINUAR...')'''
