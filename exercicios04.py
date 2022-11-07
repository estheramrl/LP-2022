import random
import os
#1. Faça um programa que armazene 15 números inteiros em uma lista e depois
#permita que o usuário digite um número inteiro para ser buscado na lista, se
#for encontrado o programa deve imprimir a posição desse número na lista, caso
#contrário, deve imprimir a mensagem: "Nao encontrado!".
'''
lista=[]
for i in range(15):
    lista.append(random.randrange(0,50))
print(lista)
print('\n')

num = int(input("Digite o número a ser verificado: "))
try:
    posicao = lista.index(num)
except:
    posicao = -1

if posicao >= 0:
    print(f'Encontrado o {num} na posição {posicao}')
else:
    print(f'Numero informado não encontrado!')
'''

#2. Faça um programa que armazene 10 letras em uma lista e imprima uma listagem
#numerada.

'''
lista2 = 'POSIÇÃO\tCARACTER\n'

lista=[]
for i in range(10):
    lista.append(chr(random.randrange(65,90)))
    lista2 += f'{i}\t{lista[i]}\n'
    print(lista2)
'''    

#3. Construa uma programa que armazene 15 números em uma lista e imprima
#uma listagem numerada contendo o número e uma das mensagens: par ou ímpar.

'''
lista = []
for i in range(15):
    lista.append(random.randrange(0,15))
    if lista[i] % 2 == 0:
        print(f'Posição {i} - Nº{lista[i]} = par ')
    else:
        print(f'Posição {i} - Nº{lista[i]} = ímpar ')
'''

#4. Faça um programa que armazene 8 números em uma lista e imprima todos os
#números. Ao final, imprima o total de números múltiplos de seis.
'''
lista=[]
cont = 0
for i in range(8):
    lista.append(random.randrange(1,48))
    if lista[i] % 6 == 0:
        cont += 1

print(lista)


print(f'O total de numero multiplos de 6 é {cont}')   

----------------------------------------------------

lista=[0, 6, 12, 18, 24, 30, 36]
cont = 0

for i in lista:
    if i % 6 == 0:
        cont += 1
        
print(lista)

print(f'O total de numero multiplos de 6 é {cont}')
'''

#5. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule
#e armazene a média arredondada. Armazene também a situação do aluno: 1-
#Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma listagem
#contendo as notas, a média e a situação de cada aluno em formato tabulado.
#Utilize quantas listas forem necessárias para armazenar os dados.
'''
lista_notas = []
lista_notas2 = []
lista_alunos = []
lista = '\nNOME\tNOTA 1\tNOTA 2\tMEDIA\n'


for i in range(5):
    lista_alunos.append(input('Nome do aluno: '))
    lista_notas.append(float(input('Nota da prova 1: ')))
    lista_notas2.append(float(input('Nota da prova 2: ')))
    media = (lista_notas[i]+lista_notas2[i])/2
    lista += f'\n{lista_alunos[i]}\t{lista_notas[i]}\t{lista_notas2[i]}\t{media}'
print(lista)


alunos = []
    for cont in range(qtde_alunos):
        aluno = {}
        aluno['nome'] = input('Nome: ')
        aluno['n1'] = round(float(input('Nota1: ')), 1)
        aluno['n2'] = round(float(input('Nota2: ')), 1)
        aluno['media'] = round((aluno['n1']+aluno['n2'])/2, 1)
        aluno['situacao'] = 'APROVADO' if aluno['media'] >= 6 else 'REPROVADO'       
        alunos.append(aluno)
    
    for aluno in alunos:
        print(f"{aluno['nome']}\t{aluno['n1']}\t{aluno['n2']}\t{aluno['media']}\t{aluno['situacao']}")
    '''

#6. Construa um programa que permita armazenar o salário de 20 pessoas. Calcular
#e armazenar o novo salário sabendo-se que o reajuste foi de 8%. Imprimir uma
#listagem numerada com o salário e o novo salário. Declare quantas listas forem
#necessárias.
'''
funcionarios = []


def cadastrar_funcionario():
    print('CADASTRO DE FUNCIONARIO')
    funcionario = {}
    funcionario['nome'] = input('Nome:')
    funcionario['salario_bruto'] = float(input('Salbário Bruto: '))
    return funcionario

def menu():
    #tela = 
       # [1] - Cadastrar
       # [0] - sair
    
    opcao = -1
    while (opcao!=0):
        print(tela)
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:
            funcionario = cadastrar_funcionario()
            funcionarios.append(funcionario)
        else:
            if opcao!=0:
                print('Opção Inválida! Tente novamente.')

def reajustar_salarios(pessoas, reajuste):
    for pessoa in pessoas:
        pessoa['salario_bruto'] = pessoa['salario_bruto'] * (1+reajuste/100)

def exibir_salarios(pessoas):
    for pessoa in pessoas:
        print(f"{pessoa['nome']}\t{pessoa['salario_bruto']}")

menu()
print('Salários antes do Reajuste')
exibir_salarios(funcionarios)
reajustar_salarios(funcionarios,8)
print('Salários após o Reajuste')
exibir_salarios(funcionarios)


lista = '\n Nº \tSALÁRIO\tNOVO SALÁRIO\n'
lista_salario = []
lista_novosalario = []

for i in range(3):
    lista_salario.append(float(input('Salário: ')))
    lista_novosalario.append(lista_salario[i]*1.08)
    print(round((lista_novosalario[i]), 2))
'''

#7. Crie umprograma que leia o preço de compra e o preço de venda de 100 mercadorias
#(utilize listas). Ao final, o programa deverá imprimir quantas mercadorias
#proporcionam: 
#• lucro < 10%
#• 10% <= lucro <= 20%
#• lucro > 20%


#8. Construa um programa que armazene o código, a quantidade, o valor de compra
#e o valor de venda de 30 produtos. A listagem pode ser de todos os produtos ou
#somente de um ao se digitar o código. Utilize dicionário como estrutura de dados.
'''
qntd_produto = int(input('Quantidade de produtos a ser analisado: '))
mercadorias = []
for i in range(qntd_produto):
    produto = {}
    produto['codigo']  = i
    produto['valor_compra'] = float(input('Valor da compra do produto: '))
    produto['valor_venda'] = float(input('Valor da venda do produto: '))
    produto['quantidade'] = int(input('Quantidade do produto: '))
    mercadorias.append(produto)

for produto in mercadorias:
    print(f"\n{produto['codigo']}\t{produto['valor_compra']}\t{produto['valor_venda']}\t{produto['quantidade']}")
'''


#9. Faça um programa que leia dois conjuntos de números inteiros, tendo
#cada um 10 elementos. Ao final o programa deve listar os elementos comuns aos
#conjuntos.
'''
numero = []
numero2 = []
def popular_lista(lista, qtde):
    for i in range(qtde):
        lista.append(int(input(f'Elemento da posição {i}: ')))

def exibir_lista(lista):
    for elemento in lista:
        print(elemento, end=" ")
    print('\n')

popular_lista(numero, 4)
exibir_lista(numero)
popular_lista(numero2, 4)
exibir_lista(numero2)
'''






#10. Faça um programa que leia uma lista com 10 elementos e obtenha outra lista resultado
#cujos valores são os fatoriais da lista original.
'''
l = []
lf = []
def populate_lista(lista, qntd):
    for i in range(qntd):
        lista.append(random.randrange(qntd))

def fatorial(n):
    fat = 1
    x = 2
    while x <= n:
        fat = fat*x
        x = x + 1
    return fat


populate_lista(l,10)
exibir_lista(l)

for x in l:
    lf.append(fatorial(x))

exibir_lista(lf)
'''


#11. Construa um programa que leia dados para uma lista de 100 elementos inteiros.
#Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.



#12. Crie um programa para gerenciar um sistema de reservas de mesas em uma casa
#de espetáculo. A casa possui 30 mesas de 5 lugares cada. O programa deverá
#permitir que o usuário escolha o código de uma mesa (1 a 30) e forneça a
#quantidade de lugares desejados. O programa deverá informar se foi possível
#realizar a reserva e atualizar a reserva. Se não for possível, o programa deverá
#emitir uma mensagem. O programa deve terminar quando o usuário digitar
#o código 0 (zero) para uma mesa ou quando todos os 150 lugares estiverem
#ocupados.

#13. Construa um programa que realize as reservas de passagens áreas de uma companhia.
#O programa deve permitir cadastrar o número de 10 voos e definir a
#quantidade de lugares disponíveis para cada um. Após o cadastro, leia vários
#pedidos de reserva, constituídos do número da carteira de identidade do cliente e
#do número do voo desejado. Para cada cliente, verificar se há possibilidade no
#voo desejado. Em caso afirmativo, imprimir o número da identidade do cliente e
#o número do voo, atualizando o número de lugares disponíveis. Caso contrário,
#avisar ao cliente a inexistência de lugares. A leitura do número 0 (zero) para o voo
#desejado indica o término da leitura de reservas.

#14. Faça um programa que armazene 50 números inteiros em uma lista. O programa
#deve gerar e imprimir uma segunda lista em que cada elemento é o quadrado do
#elemento da primeira lista.

#15. Faça um programa que leia e armazene vários números, até digitar o número
#0. Imprimir quantos números iguais ao último número foram lidos. O limite de
#números é 100.

#16. Crie um programa para ler um conjunto de 100 números reais e informe:
#• quantos números lidos são iguais a 30
#• quantos são maior que a média
#• quantos são iguais a média

#17. Faça um programa que leia um conjunto de 30 valores inteiros, armazene-os em
#um vetor e os imprima ao contrário da ordem de leitura.

#18. Faça um programa que permita entrar com 20 valores numéricos, 
# em que podem existir vários elementos repetidos. Gere
#uma lista ordenada que terá apenas os elementos não repetidos.

#19. Suponha uma estrutura de 30 elementos contendo: código e telefone. Faça
#um programa que permita buscar pelo código e imprimir o telefone.

#20. Faça um programa que leia a matrícula e a média de 100 alunos. Ordene da maior
#para a menor nota e imprima uma relação contendo todas as matrículas e médias.
