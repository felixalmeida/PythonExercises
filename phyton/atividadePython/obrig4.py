dia = int (input("Informe o dia: "))
mes = int (input("Informe o mes: "))
ano = int (input("Informe o ano: "))

if (mes > 12):
    print("Data Inválida")

elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes== 12 and dia <=31):
    print("Data válida!")

elif ( mes==2 and dia>31):
    print("Data inválida!")

elif (mes==4 and dia>30):
    print("Data inválida!")

elif (mes==6 and dia>30):
    print("Data inválida!")

elif (mes==9 and dia>30):
    print("Data inválida!")

elif (mes==11 and dia>30):
    print("Data inválida!")

elif (ano % 4 ==0):
    print("Data válida (ano bissexto)!")

else:
    print("Data inválida!")

