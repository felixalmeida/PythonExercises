nota1 = float (input("Informe a primeira nota: "))
nota2 = float (input("Informe a segunda nota: "))

media = (nota1 + nota2)/2

print("Suas notas são: ", nota1, " e ",nota2," e sua média: ", media)

if (media >=9 ):
    print("Conceito A.")
    print("Você está aprovado!")

elif (media >= 7.5 and media <= 8.9):
    print("Conceito B")
    print("Você está aprovado!")

elif (media >=6 and media <=7.4):
    print("Conceito C")
    print("Você está aprovado!")

elif (media >=4 and media <=5.9):
    print("Conceito D")
    print("Você está reprovado!")
else:
    print("Conceito E")
    print("Você está reprovado!")