print ("Responda o interrogatório com: 1-Sim.  0-Não")

quest1 = int(input("Telefonou para a vítima? "))

quest2 = int(input("Esteve no local do crime? "))

quest3 = int(input("Mora perto da vítima? "))

quest4 = int(input("Devia para a vítima? "))

quest5 = int(input("Já trabalhou com a vítima? "))

soma = quest1 + quest2 + quest3 + quest4 + quest5

if(soma == 2):
    print("Você é suspeito!")

elif(soma >=3 and soma <=4):
    print("Você é cumplice do crime.")
    
elif(soma > 4):
    print("Você é o assasino!")

else:
    print("Você é inocente.")
