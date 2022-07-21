import functions as f

notas = []

while True:
    f.menu()

    try:
        option = int(input("> "))
    except(ValueError,TypeError):
        print("Tente novamente")
    else:
        if option < 1 or option > 2:
            print("Opção Inválida, tente novamente")
            
        elif option == 1: # EMITIR RELATÓRIO DE MÉDIAS
            f.clear()
            try:
                qtd_notas = int(input("Quantidade de notas por aluno: "))
            except(ValueError,TypeError):
                print("Tente, novamente")
            else:
                f.clear()
                print("Digite 'pare' no nome do aluno para finalizar o cadastro de notas")
                f.criar_arquivo_relatorio()
                status = 'continua'
                while status == 'continua':
                    try:
                        aluno = str(input("Nome do aluno: "))
                        if aluno == 'pare':
                            break
                        else:
                            f.clear()
                            i = 0
                            while i < qtd_notas:
                                nota = float(input(f"Nota {i + 1}: "))
                                notas.clear() 
                                notas.append(nota)
                                i = i + 1
                            f.adicionar_no_arquivo(aluno,f.calcular_media(notas)) 
                    except(ValueError,TypeError):
                        print("Tente novamente")
                    else:
                        f.clear()
                        print("Deu certo")
        



        elif option == 2: # EMITIR RELÁTÓRIO DE APROVADOS E REPROVADOS
            f.clear()
            try:
                qtd_notas = int(input("Quantidade de notas por aluno: "))
                media_aprovar = float(input("Média para ser aprovado: "))
            except(ValueError,TypeError):
                print("Tente, novamente")
            else:
                f.clear()
                print("Digite 'pare' no nome do aluno para finalizar o cadastro de notas")
                f.criar_arquivo_aprovados()
                f.criar_arquivo_reprovados()
                status = 'continua'
                while status == 'continua':
                    try:
                        aluno = str(input("Nome do aluno: "))
                        if aluno == 'pare':
                            break
                        else:
                            f.clear()
                            i = 0
                            while i < qtd_notas:
                                nota = float(input(f"Nota {i + 1}: "))
                                notas.clear() 
                                notas.append(nota)
                                i = i + 1
                            f.verificar_aprov_reprov(aluno,f.calcular_media(notas),media_aprovar)
                    except(ValueError,TypeError):
                        print("Tente novamente")
                    else:
                        f.clear()
                        print("Deu certo")