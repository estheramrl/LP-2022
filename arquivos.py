#r: arquivo ser aberto em modo leitura
#w: arquivo será escrito do 0
#a: arquivo será escrito a partir da última linha

arquivo = open('usuarios.txt', 'w')
arquivo.write('esther_a_4@hotmail.com\n')
arquivo.write('goulart@hotmail.com.br.ed\n')
arquivo.write('joaosilva@gmail.com\n')
arquivo.write('usuariodemart@gamil.com')
arquivo.close()

arquivo = open('usuarios.txt', 'r')
for linha in arquivo:
    print(linha.strip())
arquivo.close()
