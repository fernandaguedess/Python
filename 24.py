#Escreva um programa que leia um número de 1 a 10 e mostre a tabuada desse número (multiplicação).

num = int(input("Digite um número para a sua tabuada:"))
for i in range(1,11,1):
    prod = num * i
    print(num,'x',i,'=',prod)


#para cada argumento,uma vírgula
#só colocar aspas em partes textuais