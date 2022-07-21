def clear():
    import os 
    os.system('cls')
    
def menu():
    print('''
            --------------------------------------------------------
                        CADASTRO DE NOTAS DE ALUNOS
            --------------------------------------------------------
                [1] EMITIR RELATÓRIO DE MÉDIAS
                [2] EMITIR RELÁTÓRIO DE APROVADOS E REPROVADOS
            --------------------------------------------------------
    ''')

def calcular_media(lista_notas):
    import statistics
    media = statistics.mean(lista_notas)
    return media 

def criar_arquivo_relatorio():
    file = open('relatorio_notas.txt' , 'x')
    file.close()

def adicionar_no_arquivo(nome,media):
    file = open('relatorio_notas.txt' , 'a')
    file.write(f"{nome} ----- {media}\n")
    file.close()

def criar_arquivo_aprovados():
    file = open('aprovados.txt' , 'x')
    file.close()

def criar_arquivo_reprovados():
    file = open('reprovados.txt' , 'x')
    file.close()

def verificar_aprov_reprov(nome,media,media_aprov):
    if media >= media_aprov:
        file = open('aprovados.txt' , 'a')
        file.write(f"{nome}\n")
        file.close()
    else:
        file = open('reprovados.txt' , 'a')
        file.write(f"{nome}\n")
        file.close()
