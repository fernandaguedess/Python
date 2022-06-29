arq = open('registrados.txt', 'a')
print('Olá, gostaria de criar uma conta?')
conf_user = input('Responda S se você quer criar uma conta e N se já possui uma.')
if (conf_user == 'S') or (conf_user == 's') or (conf_user == 'sim') or (conf_user == 'Sim'):
    nome_usuario = input('Digite o nome de usuário: ')
    arq.write('{}\n'.format(nome_usuario))

    senha_usuario = input('Digite uma senha: ')
    arq.write('{}\n'.format(senha_usuario))
    print('Cadastro realizado com sucesso!\n')
    print('Agora, efetue o seu login')
elif (conf_user == 'N') or (conf_user == 'n'):
    print('Efetue o seu login')
else: 
    print(
        'Você deve ter digitado seu nome de usuario errado, por favor verifique.'
    )

arq.close()
arq = open('registrados.txt')
nome_login = input('Digite o seu nome de usuario: ')
senha_usuario = input('Digite sua senha:')

registrados = arq.readlines()
if nome_login + '\n' in registrados:
    print('Bem vindo ao seu blog, {}!'.format(nome_login))
else:
    print(
        'Você deve ter digitado seu nome de usuario errado, por favor verifique.'
    )
arq.close()

import time


class blog():
    def __init__(self, postagens="4", programados="2", lixeira="3"):
        self.postagens = postagens
        self.programados = programados
        self.lixeira = lixeira

    @property
    def postagens(self):
        return self.__postagens

    @postagens.setter
    def postagens(self, numero):

        if numero.isdigit():
            num = int(numero)

            if num > 1 and num <= 4:
                self.__postagens = num
            else:
                print("Postagem inexistente")

        else:
            print("Escolha apenas números!")

    @property
    def programados(self):
        return self.__programados

    @programados.setter
    def programados(self, numero):

        if numero.isdigit():
            num = int(numero)

            if num >= 1 and num <= 2:
                self.__programados = num
            else:
                print("Essa postagem não está programada")

        else:
            print("Escolha apenas números!")

    @property
    def lixeira(self):
        return self.__lixeira

    @lixeira.setter
    def lixeira(self, numero):

        if numero.isdigit():
            num = int(numero)

            if num >= 1 and num <= 3:
                self.__lixeira = num
            else:
                print("Essa postagem não está na lixeira")

        else:
            print("Escolha apenas números!")



    #def criarPostagem(self):
     #   ufhjhfjfh
    def editarPostagens(self):
        num = input("Olhar/editar POSTAGEM: ")
        self.postagens = num
    def editarProgramados(self):
        num = input("Olhar/editar PROGRAMADO: ")
        self.programados = num

    def editarLixeira(self):
        num = input("Olhar/editar LIXEIRA: ")
        self.lixeira = num

    def __str__(self):
        return "POSTAGENS: {} \nPROGRAMADOS: {}\nLIXEIRA: {} \n".format(
            self.postagens, self.programados, self.lixeira)


def main():
    bl01 = blog()

    while True:
        print("\n" * 40)
        print(bl01)

        print("Configurações----")
        print("1 = Editar Postagens")
        print("2 = Editar Programados")
        print("3 = Editar Lixeira")
        print("4 = Criar Postagem")
        print("5 = Sair\n ----------------")#ok
        selec = input("Selecionar: ")

        if selec == "1":
            bl01.editarPostagens()

        elif selec == "2":
            bl01.editarProgramados()

        elif selec == "3":
            bl01.editarLixeira()

        elif selec == "4":
            bl01.editarCriar()

        elif selec == "5":
            print("Saindo ...")
            break

        else:
            print("Selecione uma opção válida!")

        time.sleep(2)


main()
#login ok
#menu ok
