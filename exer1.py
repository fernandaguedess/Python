#Escreva um programa que receba 2 notas de um aluno (float) e informe a média


x = float(input("Digite sua primeira nota:"))
y = float(input("Digite sua segunda nota:"))

media = (( x + y ) /2)

print("Sua média é:", media)

#o float é necessário antes do input porque este sempre retorna uma string