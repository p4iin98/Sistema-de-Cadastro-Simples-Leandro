from lib.functions import *
from lib.arquivos import *
from time import sleep
from datetime import date

arq = 'cadastro.txt'
if not encontrarArquivo(arq):
    print('ARQUIVO DE CADASTRO NAO ENCONTRADO, CRIANDO...')
    criarArquivo(arq)
data_atual = date.today()
alunoslista = []
listapassageira = list()
print('	\033[1;32mSISTEMA ACADEMIA CADASTRO ALUNOS V.5\033[1;32m\n\n')
listmenu = ['Ver alunos cadastrados', 'Cadastrar', 'Procurar Aluno', 'Fechar']

while True:
    linha()
    resposta = menuprincipal(listmenu)
    if resposta == 1:
        print()
        linha(48)
        print(f'\033[1;93m{linha2(21)}ALUNOS{linha2(21)}')
        '''if alunoslista == []:
      print('TA VAZIO')
    print(f'{menu(alunoslista)}')
    linha()'''
        lerArquivo(arq)
        digite_algo = input(
            '\033[1;32mAPERTE ENTER PARA VOLTAR AO MENU...\n\n')

    elif resposta == 2:
        cadastro = str(input('\033[1;96mNome do aluno: '))
        print('')
        while True:
            try:
                cadastro2 = int(input('Idade do aluno: '))
                print()
            except ValueError:
                print('ERRO! DIGITE UM NÚMERO INTEIRO PARA IDADE.\n\n')
            else:
                break
        while True:
            cadastro3 = planos()
            if cadastro3 == 1:
                plano = ('PLANO: FORTX(R$130,00)')
                data_vencimento = date(2020, data_atual.month + 1,
                                       data_atual.day)
                data_correta = f'{data_vencimento.day}/{data_vencimento.month}/{data_vencimento.year}'
                arquivoCadastrar(arq, cadastro, cadastro2, plano, data_correta)
                linha()
                print(f'{cadastro} FOI CADASTRADO COM SUCESSO!')
                linha()
                break
            elif cadastro3 == 2:
                plano = ('PLANO: BODYPERFECT(R$ 90,00)')
                data_vencimento = date(2021, 2, data_atual.day)
                data_correta = f'{data_vencimento.day}/{data_vencimento.month}/{data_vencimento.year}'
                arquivoCadastrar(arq, cadastro, cadastro2, plano, data_correta)
                linha()
                print(f'{cadastro} FOI CADASTRADO COM SUCESSO!')
                linha()
                break
            elif cadastro3 == 3:
                plano = ('PLANO: PREMIUM(R$65,00')
                data_vencimento = date(2021, data_atual.month, data_atual.day)
                data_correta = f'{data_vencimento.day}/{data_vencimento.month}/{data_vencimento.year}'
                arquivoCadastrar(arq, cadastro, cadastro2, plano, data_correta)
                linha()
                print(f'{cadastro} FOI CADASTRADO COM SUCESSO!')
                linha()
                print()
                break

    elif resposta == 3:
        palavra_find = str(input('Digite o nome que quer procurar: '))
        procurarNomeArquivo(arq, palavra_find)
        print('OBS: Se não aparecer nada, o aluno não foi encontrado!')
        input('APERTE ENTER PARA VOLTAR AO MENU...\n\n')

    elif resposta == 4:
        print('FECHANDO O PROGRAMA...')
        sleep(2)
        print('FECHADO!')
        break
'''
try:
      listapassageira.clear()
      cadastro = str(input('Nome do aluno: '))
      cadastro2 = int(input('Idade do aluno: '))
      linha()
      linha()
      listapassageira.append(cadastro)
      listapassageira.append(cadastro2)
      while True:
        cadastro3 = planos()
        if cadastro3 == 1:
          listapassageira.append('Plano: Mensal(R$130,00)')
          data_vencimento = date(2020, data_atual.month + 1, data_atual.day)
          #calculodata = (data_vencimento - data_atual)
          listapassageira.append(data_vencimento)
          break
        elif cadastro3 == 2:
          listapassageira.append('Plano: Trimestral(R$ 90,00)')
          data_vencimento = date(2020, data_atual.month + 1, data_atual.day)
          #calculodata = (data_vencimento - data_atual)
          listapassageira.append(data_vencimento)
          break
        elif cadastro3 == 3:
          listapassageira.append('Plano: Anual(R$65,00')
          data_vencimento = date(2020, data_atual.month + 1, data_atual.day)
          #calculodata = (data_vencimento - data_atual)
          listapassageira.append(data_vencimento)
          break
        else:
          print('Opção de plano inválida!')
      copia = listapassageira.copy()
      alunoslista.append(copia)
      linha()
      print(f'{cadastro} FOI CADASTRADO COM SUCESSO!\n')
    except ValueError:
      print('DEU ERRO NO CADASTRO! DIGITE UM NÚMERO INTEIRO!')
'''
