#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.

#n1 = int(input("Digite um numero: "))
#n2 = int(input("Digite um numero: "))

#if n1 + n2 > 10:
#   print (f"A soma dos produtos é {n1+n2}")
#else:
#   print("") 

#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.

#n1 = int(input("Digite um numero: "))
#n2 = int(input("Digite um numero: "))
#soma = (n1+n2)

#if soma > 20:
#   print(f"O valor somado é maior que 20 logo {soma+8}")
#else:
#   print(f"O valor somado é menor que 20 logo {soma-5}")


#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".
# resto de divisão é " % "
#num = int(input("Digite um numero: "))

#if num %3 == 0 :
#   print("É múltiplo de 3")
#else:
#   print("Não é múltiplo de 3")

#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.

#num = int(input("Digite um numero: "))

#if num %5 == 0 :
#   print("É divísivel por 5")
#else:
#   print("Não é dívisivel por 5")

#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.

#num = int(input("Digite um numero: "))

#if num %3 == 0 and num %7 == 0:
#   print("O número informado é dívisel por 3 e por 7")
#elif num %3 != 0 and num %7 == 0:
#   print("O número informado é divisivel por 7 mas não é divisivel por 3")
#elif num %3 == 0 and num %7 != 0:
#   print("O número informado é divisivel por 3 mas não é divisivel por 7")
#elif num %3 != 0 and num %7 != 0:
#   print("O número informado não é divisivel por 7 e nem por 3") 


#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa em linguagem C que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.

#salario = int(input("Valor do salário bruto: "))
#valor = float(input("Valor das prestações: "))

#if valor > salario*0.3:
#   print ("O empréstimo não pode ser concedido !!")
#else:
#   print("O empréstimo pode ser concedido !!")

#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.

#num = int(input("Informe um número: "))

#if num >= 20 and num <= 50:
#   print("Número informado está compreendido entre 20 e 50")
#else:
#   print("Número informado não está compreendido entre 20 e 50")

#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".

#num = int(input("Informe um número: "))

#if num > 20 :
#   print("O número é maior do que 20")
#elif num == 20 :
#   print("O número é igual a 20")
#elif num < 20 :
#   print("O número é menor do que 20")   


#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e como
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.

#nascimento = int(input("Informe o ano de nascimento: "))
#atual = int(input("Informe o ano atual: "))
#idade = atual - nascimento

#if nascimento < 1000 or nascimento > 9999 or atual < 1000 or atual > 9999:
#   print("O ano informado é inválido !!")      
#else:
#   print(f"A idade do usuário é: {idade}")
   

#10. Faça um programa que leia três números inteiros e imprima os três em ordem
 #    crescente.

#num1 = int(input("Digite o primeiro número: "))
#num2 = int(input("Digite o segundo número: "))
#num3 = int(input("Digite o terceiro número: "))

#if num1 <= num2 and num1 <= num3 and num2 <= num3:
#   print(f"{num1} {num2} {num3}")
#elif num2 <= num1 and num2 <= num3 and num1 <= num3:
#   print(f"{num2} {num1} {num3}")
#elif num3 <= num1 and num3 <= num2 and num1 <= num2:
#   print(f"{num3} {num1} {num2}")
#elif num1 >= num3 and num1 >= num2 and num2 >= num3:
#   print(f"{num3} {num2} {num1}")
#elif num2 >= num1 and num2 >= num3 and num1 >= num3:
#   print(f"{num3} {num1} {num2}")
#elif num3 >= num1 and num3 >= num2 and num1 >= num2:
#   print(f"{num2} {num1} {num3}")         
   
#11. Faça um programa que leia 3 números e imprima o maior deles.

#num1 = int(input("Digite o primeiro número: "))
#num2 = int(input("Digite o segundo número: "))
#num3 = int(input("Digite o terceiro número: "))

#if num1 <= num2 and num1 <= num3 and num2 <= num3:
#   print(f"O maior número é o: {num3}")
#elif num2 <= num1 and num2 <= num3 and num1 <= num3:
#   print(f"O maior número é o: {num3}")
#elif num3 <= num1 and num3 <= num2 and num1 <= num2:
#   print(f"O maior número é o: {num2}")
#elif num1 >= num3 and num1 >= num2 and num2 >= num3:
#   print(f"O maior número é o: {num1}")
#elif num2 >= num1 and num2 >= num3 and num1 >= num3:
#   print(f"O maior número é o: {num2}")
#elif num3 >= num1 and num3 >= num2 and num1 >= num2:
#   print(f"O maior número é o: {num3}") 

#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idade
#• Se é maior de 65 anos

'''
idade = int(input("Informe a a idade: "))

if idade >= 18 and idade < 65:
   print("O usuário é maior de idade!!")
elif idade > 65:
   print("Usuário idoso com idade superior a 65 anos!!")
else:
   print("O usuário é menor de idade!!")
'''

#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#    da prova 2 de umaluno. O programa deve imprimir o nome, a nota da prova 1,
#    a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#    "Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#    reprovação e as demais em prova final).
'''
nome = input("Nome do aluno: ")
nota1 = int(input("Nota prova 1: "))
nota2 = int(input("Nota prova 2: "))
media = nota1+nota2/2

if media >= 7 and media <=10:
   print(f"O aluno {nome} está aprovado!!")
   print(f"A nota da prova 1 é {nota1}")
   print(f"A nota da prova 2 é {nota2}")
   print(f"A média final é {media}")
else:
   print(f"O aluno {nome} está reprovado!!")
   print(f"A nota da prova 1 é {nota1}")
   print(f"A nota da prova 2 é {nota2}")
   print(f"A média final é {media}")
'''

#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#    desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%

#15. Um comerciante comprou umproduto e quer vendê-lo com umlucro de 45% se o
#    valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#    Faça um programa que leia o valor do produto e imprima o valor da venda.

#16. A confederação brasileira de natação irá promover eliminatórias para o
#    próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#    a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos

#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#    as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#    muito caro. Umvendedor de um plano de saúde apresentou a tabela a seguir.
#    Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#    nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00

#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#    correspondente. Caso o usuário digite umnúmero fora desse intervalo, deverá
#    aparecer uma mensagem informando que não existe mês com este número. Utilize
#    o switch para este problema.

#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#    para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#    mesmo número de pontos, criar um programa que informe se uma equipe foi
#    classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses valores em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".
#20. O banco x concederá um crédito especial com juros de 2% aos seus clientes de
#    acordo com o saldomédio no último ano. Faça um programa que leia o saldo médio
#    de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#    O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#    crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio

#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#    livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#    imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#    tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:

#22. Construa um programa que leia o percurso em quilómetros, o tipo do carro e
#    informe o consumo estimado de combustível, sabendo-se que umcarro tipo C faz
#    12 kmcom umlitro de gasolina, um tipo B faz 9 kme o tipo C, 8 kmpor litro.

#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#    a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#    bebida conforme a tabela a seguir.
#Prato Sobremesa Bebida
#Vegetariano 180cal Abacaxi 75cal Chá 20cal
#Peixe 230cal Sorvete diet 110cal Suco de laranja 70cal
#Frango 250cal Mousse diet 170cal Suco de melão 100cal
#Carne 350cal Mousse chocolate 200cal Refrigerante diet 65cal

#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#    cobrar dosmotoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#    carro deve ser renovado é determinado pelo último número da placa do mesmo,
#    faça um programa que, a partir da leitura da placa do carro, informe o mês
#    em que o emplacamento deve ser renovado.

#25. A prefeitura contratou uma firma especializada para manter os níveis de
#    poluição considerados ideais para umpaís do 1º mundo. As indústrias,
#    maiores responsáveis pela poluição, foram classificadas em três grupos.
#    Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#    aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#    acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º gurpo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos