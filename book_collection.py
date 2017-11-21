collection_list = []
isNew = False
newFile = ""
fileName =""
item = ""

def init():
    # define as variáveis globais que serão utilizadas
    global isNew
    global fileName
    global collection_list
    # pede ao usuário qual opção ele deseja realizar
    print("\nEscolha sua opção de coleção:\n1 - Criar nova coleção.\n2 - Abrir coleção existente.")
    try:
        option = int(input("\nInsira número 1 ou 2:"))
        if option == 1:
            # se o usuário selecionar a opção 1 informa que a nova coleção foi criada.
            print("\nVocê criou uma nova coleção de livros.")
            # seta a variável de arquivo novo
            isNew = True
        elif option == 2:
            # se o usuário selecionar abrir um arquivo existente
            # pergunta o nome do arquivo a ser aberto
            fileName = input("\nQual o nome do programa que deseja abrir? ")
            fileName = fileName + ".txt"
            # seta a variável informando que o arquivo não é novo
            isNew = False
            # lê o arquivo informado
            read_file()
        else:
            print("\nEsta opção é inválida.")
            init()
        main()
    except:
        # limpar a coleção para reiniciar a aplicação
        collection_list = []
        print("\nOcorreu algum erro inexperado.")
        init()

def main():
    global collection_list
    print("\nEscolha uma das opções abaixo:")
    print("A - Adicionar livro")
    print("B - Buscar livro")
    print("R - Remover livro")
    print("L - Listar livros")
    print("S - Sair")
    option = input("Digite sua opção: ")

    if option == 'A' or option =='a':
        # se a opção selecionada foi incluir um novo livro
        add_book()

    elif option =='B' or option =='b':
        # se a opção selecionada foi buscar 
        find_book()

    elif option =='R' or option =='r':
        # se a opção selecionada foi remover
        remove_book()

    elif option =='L' or option =='l':
        # se a opção selecionada foi listar
        get_collection(collection_list)
    
    elif option =='S' or option =='s':
        # se a opção selecionarda foi sair
        exit()
    else:
        print("\nA opção informada é invalida.")
        main()

def add_book():
    print("\nVocê digitou a opção 'Adicionar livro'.")
    # pede ao usuário para digitar o livro que deseja adicionar
    add = input("\nDigite o livro para adicionar:")
    # adiciona o livro do usuário à coleção
    collection_list.append(add)
    # apresenta as opções do menu novamente para o usuário
    main()

def find_book():
    global collection_list
    global key
    print("\nVocê digitou a opção 'Buscar livro'.")
    # pede ao usuário para digitar o livro que deseja buscar
    key = input("Digite um livro a buscar:")
    # busca o a posição do livro na coleção
    position = find_item(collection_list, key)
    
    if not (position is None):
        # se o item foi encontrado apresenta a mensagem de item encontrado
        print("\nO livro %s foi encontrado." %key)
        print("O livro está na posição: %s" %position)
    else:
        # senão apresenta a mensagem que o livro digitado não foi encontrado
        print("\nO livro %s não foi encontrado." %key)

    # volta ao menu inicial com as opções para o usuário
    main()

def find_item(list_itens, value):
    # para cada item na lista
    for index, item in enumerate(list_itens):
        # se o item da lista for igual ao valor, retorna o indice da lista
        if item == value:
            return index

    # se fosse com while
#    count = 0
#    position = None
#    while count < len(collection_list):
#        if collection_list[count] == value:
#            position = index
#        count = count + 1
#    return position
    

def remove_book():
    global item
    global collection_list

    print("\nVocê digitou a opção 'Remover livro'.")
    # verifica se há algum livro na coleção
    if len(collection_list) == 0:
        print("\nA sua coleção não possui livros!")
        # se não há livros, volta ao menu inicial com as opções para o usuário
        main()
    
    # pede ao usuário para digitar o livro que deseja remover
    item = input("\nDigite o livro que deseja remover: ")
    # busca o a posição do livro na coleção
    position = find_item(collection_list, item)
    
    if not (position is None):
        # se o item foi encontrado, remove o mesmo da lista
        del collection_list[position]
        print("\nO livro %s foi removido." %item)
    else:
        # se o livro não foi encontrado solicita ao usuário para tentar novamente
        print("\nO livro %s não foi encontrado. Tente novamente: " %item)
        remove_book()

    # volta ao menu inicial com as opções para o usuário
    main()

def get_collection(list_itens):
    print("\nVocê digitou a opção 'Listar livros'.")
    if len(collection_list) == 0:
        # se não há livros, informa ao usuário
        print("\nA sua coleção não possui livros!")
    else:
        # mostra ao usuário quais são os livros da coleção
        print("\nA coleção é formada pelos seguintes livros: ")
        for index, item in enumerate(list_itens):
            print("- %s" %item)

    # volta ao menu inicial com as opções para o usuário
    main()

def exit():
    if isNew == True:
        # se o arquivo é novo pergunta se o usuário deseja salvar o arquivo
        saving_file()
    else:
        # se o arquivo não é novo pergunta se o usuário deseja atualizar as informações no arquivo
        print("Deseja salvar alterações no arquivo?")
        print("S - Sim")
        print("N - Não")
        save = input("\nDigite sua opção: ")
        if save == "S" or save =='s':
            # se o usuário desejar salvar, escreve no arquivo
            write_file()
        else:
            print("\nArquivo não será salvo.")
    print("\nObrigado por utilizar o programa!")

def read_file():
    global collection_list
    # abre o arquivo no modo de leitura (r)
    fileToRead = open(fileName, "r")
    # para cada livro no arquivo, adiciona na coleção
    for book in fileToRead:
        book = book.strip('\n')
        collection_list.append(book)
    # fecha o arquivo
    fileToRead.close()

    # abre as opções a serem realizadas com a coleção do arquivo
    main()

def saving_file():
    global newFile
    print("\nDeseja salvar novo arquivo?")
    print("S - Sim")
    print("N - Não")

    # verifica se o usuário deseja salvar em um arquivo
    save = input("\nDigite sua opção: ")
    if save == "S" or save =='s':
        # se a opção do usuário for salvar
        newFile = input("\nQual o nome do novo arquivo que deseja criar?")
        newFile = newFile + ".txt"
        # cria o arquivo no diretório
        create_file()
        # escreve no arquivo
        write_file()
    elif save == "N" or save =='n':
        print("\nArquivo não será salvo.")
    else:
        print("\nOpção inválida.")
        # retorna a função atual
        saving_file()

def create_file():
    global newFile
    # cria o arquivo no diretório, no modo de escrita (w)
    file_create = open(newFile, "w")
    # fecha o arquivo
    file_create.close()
    print("\nO arquivo %s foi criado!" %newFile)

def write_file():
    global newFile
    global fileName
    global isNew
    if isNew:
        # abre o arquivo no modo de alteração (a)
        fileToWrite = open(newFile, "a")
        for book in collection_list:
            # escreve cada livro na coleção
            fileToWrite.write(book + "\n")
        # fecha o arquivo
        fileToWrite.close()
    else:
        # apaga todos os registros do arquivo no modo de escrita (w)
        fileToWrite = open(fileName,"w")
        # fecha o arquivo
        fileToWrite.close()

        # após limpar o arquivo, abre o mesmo para escrever nele
        fileToWrite = open(fileName,"a")
        for book in collection_list:
            # escreve cada livro na coleção
            fileToWrite.write(book + "\n")
        # fecha o arquivo
        fileToWrite.close()

# inicializa o programa
init()
