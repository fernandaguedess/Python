from login import Login
from blog import Blog
from datetime import datetime

Login()
Blog()

def Main():
    bl01 = Blog()

    while True:
        print("\n" * 40)
        print(bl01)

        print("Configurações----")
        print("1 = alterar Identificador")
        print("2 = alterar Tema")
        print("3 = alterar Título")
        print("4 = alterar Texto")
        print("5 = Publicar")
        print("6 = Sair\n ----------------")
        selec = input("Selecionar: ")

        if selec == "1":
            bl01.alterarIdentf()

        elif selec == "2":
            bl01.alterarTema()

        elif selec == "3":
            bl01.alterarTitulo()

        elif selec == "4":
            bl01.alterarTexto()

        elif selec == "5":
            print("Post publicado!")
            break

        elif selec == "6":
            print("Saindo ...")
            break

        else:
            print("Selecione uma opção válida!")

        time.sleep(2)


Main()