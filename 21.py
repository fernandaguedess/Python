#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
#o return em uma função é diferente de mostrar um valor, por mais que pareçam a msm coisa
#a ordem é sempre o tipo de variável e dps o método(no caso,int(input))
#dentro da função só pode ter o que ela vai fazer, sem declarar as variáveis,bem enxuto msm

def soma(x,y,z):
  s = x+y+z
  print("A funcao s é: ", s)

x = int(input("Digite o primeiro elemento:"))
y = int(input("Digite o segundo elemento:"))
z = int(input("Digite o terceiro elemento:"))

  
soma(x,y,z)

#dentro da função só pode ter o que ela vai fazer,sem a parte de atribuir valores as variáveis