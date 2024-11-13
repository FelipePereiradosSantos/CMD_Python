import os

def pwd ():
    
    return os.getcwd()

def mkdir(nome_dir):

    novo_dir = pwd()+"/"+nome_dir

    return os.mkdir(novo_dir)

def ls():

    return os.listdir()

def touchFile (nome_texto, conteudo_texto):

    with open(nome_texto, "w") as texto:
        texto.write(conteudo_texto)

def catFile (nome_texto):

    return print(open(nome_texto, "r").read())

print("|----------CMD----------|")
print("Comandos:\npwd - verificar o diretório atual\nmkdir - criar um novo diretório\nls - listar todos os arquivos do diretorio atual\ntouch file - criar arquivo de texto\ncat file - ler arquivo de texto")

while (True):

    input_usuario = input()

    match (input_usuario):

        case "pwd": 
            print(pwd())

        case "mkdir":
            nome_dir = input("Insira o nome do diretório:")
            mkdir(nome_dir)
            print(f"Diretorio {nome_dir} criado com sucesso!")

        case "ls":
            print(ls())

        case "touch file":
            nome_texto = input("Escreva o nome do arquivo: ")
            conteudo_texto = input("Escreva o conteudo do arquivo: ")
            touchFile((nome_texto+".txt"), conteudo_texto)
            print(f"Arquivo de texto {nome_texto} criado com sucesso!")

        case "cat file":
            nome_texto = input("Insira o nome do texto: ")
            print(catFile(nome_texto))

        case _:
            print("Comando Inválido")