kgMorango = float(input("Total de Kilos de Morango: "))
kgMaca = float(input("Total de Kilos de Maçã: "))

morango = 2.5
maca = 1.80

if (kgMorango < 0 or kgMaca < 0):
    print("Erro! Verifique os valores digitados no painel.")

elif (kgMorango <= 5 and kgMaca <= 5):
    totalMorango = morango * kgMorango
    totalMaca = maca * kgMaca
    totalCompras = totalMorango + totalMaca
    print ("Valor total a ser pago: R$ %.2f" %totalCompras)

elif  (kgMorango > 5 and kgMaca > 5):
    totalMorango = 2.2 * kgMorango
    totalMaca = 1.5 * kgMaca
    totalCompras = totalMorango + totalMaca
    print ("Valor total a ser pago: R$ %.2f" %totalCompras)
       
elif (kgMorango > 5 and kgMaca <= 5):
    totalMorango = 2.2 * kgMorango
    totalMaca = maca * kgMaca
    totalCompras = totalMorango + totalMaca
    print ("Valor total a ser pago: R$ %.2f" %totalCompras)
    
elif (kgMorango <= 5 and kgMaca > 5):
    totalMorango = morango * kgMorango
    totalMaca = 1.5 * kgMaca
    totalCompras = totalMorango + totalMaca
    print ("Valor total a ser pago: R$ %.2f" %totalCompras)
    
else:
    print("Erro, verifique os valores informados")
