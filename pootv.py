#Crie um programa que simule uma televisão, definindo uma classe e criando como um objeto.
#O usuário pode informar o canal e aumentar ou diminuir o volume .
#A cada interação com a TV, exibir o canal, o volume...
#Obs: • deve ser verificado se o canal informado e o volume estão dentro de faixas válidas. Por exemplo, o volume não deve ser < 0.
#• os métodos relacionados a volume não precisam de parâmetros.
#• opcional: implementar ligar, desligar, gravar...

class Televisão():
        def __init__(self,canal = "1",volume="40"):
            self.canal=canal
            self.volume= volume
            
        def canal(self):
            return self.__canal

        def alterarCanal(self,numero):
            if numero.isdigit():
                num = int(numero)

                if num > 0 and num <= 150:
                    self.__canal = num
                else:
                    print("Canal inválido")
            
            else:
                print("O canal deve ter só números")



            self.canal= self.canal+numnovoCanal

        def volume(self):
            return self.__volume

        def defaumentarvolume(self,numero):
            if numero.isdigit():
                num = int(numero)

                if num >= 0 and num <= 100:
                        self.__volume = num
                else:
                        print("O volume deve ser entre 0 e 100")
            else:
                print("O volume deve ser apenas números!")
        def mudaCanal(self):
            num = input("Mudar para CANAL: ")
            self.canal = num

        def mudaVolume(self):
            num = input("Mudar para VOLUME: ")
            self.volume = num

        def __str__(self):
            return "CANAL: {} \nvolume: {}\n ".format(self.canal, self.volume)

def main():
    tvi = Televisão()

    while True:
        print("\n"*40)
        print(tvi)

        print("opções")
        print("1 - mude o canal")
        print("2 - mude o volume")
        print("3 - desligar\n ")
        selec = input("Selecionar:")

        if selec == "1":
            tvi.mudaCanal()

        elif selec == "2":
            tvi.mudaVolume()

        elif selec == "3":
            print("Desligar")
            break

        else:
            print("Selecione uma opção válida :)")

        time.sleep(2)

main()







