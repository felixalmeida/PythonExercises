p1 = float (input("Informe o valor do primeiro produto: R$ "))
p2 = float (input("Informe o valor do segundo produto: R$ "))
p3 = float (input("Informe o valor do terceiro produto: R$ "))

if (p1 < p2 and p1 < p3):
    print("Compre o produto 1, é mais barato!")
elif (p2 < p1 and p2 < p3):
    print("Compre o produto 2, é mais barato!")
else:
    print("Compre o produto 3, é mais barato!")