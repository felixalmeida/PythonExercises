saque = int(input("Informe um valor a sacar: "))

if (saque < 10 or saque > 600):
    print("Valor indisponível!")

else:

    nota100 = saque/100
    saque = saque%100

    nota50 = saque/50
    saque = saque%50

    nota10 = saque/10
    saque = saque%10

    nota5 = saque/5
    saque = saque%5

    nota1 = saque/1
    saque =  saque%1

    print("Notas de 100: ",int(nota100))
    print("Notas de 50: ",int(nota50))
    print("Notas de 10: ",int(nota10))
    print("Notas de 5: ",int(nota5))
    print("Notas de 1: ",int(nota1))