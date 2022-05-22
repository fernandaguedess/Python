#Escreva um programa que receba o salário de um funcionário (float), e retorne o resultado do novo salário com reajuste de 15%.

salario = float(input("Digite aqui o seu salário:"))

valor = (((100+15)/100)*salario)

print("O dado salário com reajuste de 15% é: R$ ",valor)