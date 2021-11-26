nome = input("Qual seu nome? ")
salario = int (input("Informe o valor do seu salário: "))
vendas = int (input("Quanto você vendeu este mês? "))
comisao = vendas * 0.15
total = salario + comisao


print(nome, "O total que você vai receber é: ", total)