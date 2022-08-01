nome = "    João Paulo  "
print(len(nome))                #retorna tamanho da string
nome = nome.strip()             #remove os espaços em branco
print(len(nome))
print(nome[1])                  #retorna o primeiro caractere (0 conta como posição)
print(nome[2:4])                #retorna carctere de 2 a 3 (ultimo não incluso)
print(nome[-5:-1])              #começa a contagem de string pelo final
print(nome[0:10:2])             #de 0 a 10 (ultimo caractere não incluso)
print(nome.lower())             #transforma as strings em minusculo
print(nome.upper())             #transforma as strins em maiusculo
print(nome.replace("o","0"))    #substitui toda strin "o" por "0"
print("au" in nome)             #verifica se contém "au" na string nome, caso tenha retorna True
print("au" not in nome)         ## caso não tenha "au" na string retorna True  
idade = 40
texto = "Meu nome é {} e tenho {} anos"
print(texto.format(nome,idade)) #Essa função irá formatar o texto com as variaveis nome e idade nos "{}"