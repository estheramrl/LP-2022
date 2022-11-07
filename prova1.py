'''
PROVA PRÁTICA DE PYTHON
Ao término enviar e-mail conforme modelo:
Para:       preti.joao@ifmt.edu.br
Assunto:    Prova 1 de Laboratório de Programação 2022/2
Mensagem:   NOME COMPLETO DO ESTUDANTE
Anexo:      prova1.py
'''

def main():
    '''
    Executa todass as questões
    '''

    #1. Faça um programa que leia o valor de um produto, o percentual
    #   do desconto desejado e imprima o valor do desconto e o valor
    #   do produto subtraindo o desconto. (2,0pt)
    
    valor = int(input('Informe o valor do produto: '))
    desconto = int(input('Qual o valor do desconto: '))
    porcent = valor*(desconto/100)

    print(f'\nO valor do produto com o desconto é: {valor - porcent}')
    


    #2. Faça um programa que leia 3 números e imprima o maior deles. (2,0pt)
    
    
    n1 = int(input('Nº1: '))
    n2 = int(input('Nº2: '))
    n3 = int(input('Nº3: '))

    if n1 > n2 and n1 > n3 and n2 > n3:
        print(f'\nO maior número é o: {n1}')
    elif n2 > n1  and n2 > n3 and n1 > n3:
        print(f'\nO maior número é o: {n2}')
    elif n3 > n1 and n3 > n2 and n2 > n1:
        print(f'\nO maior número é o: {n3}')
    


    #3. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
    #   da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
    #   a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
    #   "Reprovado" ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
    #   reprovação e as demais em prova final). (2,0pt)
    
    lista = 'ALUNO\tNOTA 1\tNOTA 2\tMÉDIA'
    aluno = input('Nome aluno: ').upper().strip()
    nota1 = int(input('Nota prova 1: '))
    nota2 = int(input('Nota prova 2: '))
    media = (nota1+nota2)/2

    if media >= 7:
        print(f'O aluno(a) {aluno} foi aprovado !!\n')
        print(lista)
        lista = f'{aluno}\t{nota1}\t{nota2}\t{media}'
        print (lista)
    elif media >= 3 and media < 7:
        print(f'O aluno(a) {aluno} está em prova final !!\n')
        print(lista)
        lista = f'{aluno}\t{nota1}\t{nota2}\t{media}'
        print (lista)
    elif media < 3:
        print(f'O aluno(a) {aluno} está reprovado!!\n')
        print(lista)
        lista = f'{aluno}\t{nota1}\t{nota2}\t{media}'
        print (lista)
    


    #4. Faça um programa que apresente um menu com 4 opções:
    #   [1] - Cadastrar
    #   [2] - Excluir
    #   [3] - Pesquisar
    #   [0] - Sair
    #   O usuário deve escolher uma opção e o programa deve imprimir uma mensagem 
    #   ao entrar em cada opção do menu. O programa só deve encerrar quando a opção
    #   escolhida for zero (0). (2,0pt)
    
    cont = 1
    while cont >= 1:
        print('\n[1] - Cadastrar\n[2] - Excluir\n[3] - Pesquisar\n[0] - Sair\n')
        escolha = int(input('Escolha uma opção: '))
        if escolha == 1:
            print('Você escolheu a opção cadastrar!!')
        elif escolha == 2:
            print('Você escolheu a opção excluir!!')
        elif escolha == 3:
            print('Você escolheu a opção pesquisar!!')
        elif escolha == 0:
            print('Saindo...')
            cont = 0
        else:
            print('Você escolheu uma opção inválida!!')
    

    #5. Faça um programa que calcule o retorno de um investimento. (2,0pt)
    #   O programa deve solicitar do usuário o:
    #   - valor que será investido;
    #   - prazo do investimento (meses);
    #   - juros mensal.

    investimento = int(input('Informe o valor do investimento: '))
    meses = int(input('Quantidade de meses que será investido: '))
    juros = float(input('Valor do percentual de juros mensal: '))

    for x in range(meses):
        investimento += (juros/100)
    print(f'\nO retorno do investimento será de: R${investimento}')



main()