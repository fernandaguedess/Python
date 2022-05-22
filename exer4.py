#Escreva um programa que receba 2 valores do tipo inteiro x e y, e calcule o valor de z: z = (x2 + y2)

x = float(input("Digite o primeiro número:"))
y = float(input("Digite o segundo número:"))

z = (pow(x,2)+ 2*x*y+ pow(y,2))

print("O resultado é:", z)