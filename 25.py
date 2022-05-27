#(Desafio) Utilizando listas faça um programa que faça 5 perguntas para uma pessoa (ou várias pessoas) sobre um crime.  As perguntas são: 
# 1.Telefonou para a vítima no dia do crime?  
#2: Esteve no local do crime?  Responda com S ou N
#3: Mora perto da vítima?  Responda com S ou N
#4: Devia dinheiro para a vítima?  Responda com S ou N
#5: Já trabalhou com a vítima? Responda com S ou N
#O programa deve no final emitir uma classificação sobre a participação da(s) pessoa(s) no crime.  
#• Suspeita: 2 questões positivas (sim) 
#• Cumplice: entre 3 e 4 questões positivas 
#• Assassino: 5 questões positivas 
#• Inocente: menos de 2 questões positivas




a = int(input("1.Telefonou para a vítima no dia do crime?Responda com 1 ou 0 , 1 para sim e 0 para não "))
b = int(input("2.Esteve no local do crime?Responda com 1 ou 0 , 1 para sim e 0 para não "))
c = int(input("3.Mora perto da vítima?Responda com 1 ou 0 , 1 para sim e 0 para não "))
d = int(input("4.Devia dinheiro para a vítima?Responda com 1 ou 0 , 1 para sim e 0 para não "))
e = int(input("5.Já trabalhou com a vítima?Responda com 1 ou 0 , 1 para sim e 0 para não  "))



resp = []

#for i in range(a,e,1):
    #resp.insert(0,i)
resp.insert(0,a)
resp.insert(1,b)
resp.insert(2,c)
resp.insert(3,d)
resp.insert(4,e)

#S = 1
#N = 0
#tentar ver uma maneira de receber as respostas com uma letra e convertê-las usano o replace


if (sum(resp)) == 5:
    print('SEU ASSASSINO!')
elif (sum(resp)) == 2:
    print('Suspeito,viu? Suspeito....')
elif (sum(resp)) <= 1:
    print('Finalmente um inocente!!!!!:D')
elif (sum(resp)) < 5 and (sum(resp)) > 2:
    print('Parece que temos um CÚMPLICE aqui...ihhh')
else:
    print('Digite um caractere válido!')