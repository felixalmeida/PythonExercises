#Nome: Felix Oliveira (fiz sozinho, ta incompleto pq fiz na raça, mas vou terminar ele pra aprender mais, obg pela ajuda)
#To gostando do curso
import os 
from funcs import limparTela

while True:   
    print ("\nBem vindo ao jogo da Morte!")
    desafiante = input("Desafiante! Informe seu nome: ")
    print("############################")
    competidor = input("Competidor! Informe seu nome: ")
    limparTela()

    print("Vez de: ",desafiante)
    
    palavra = str(input("Informe a palavra chave: "))
    dicas = []
    dica1 = str(input("Informe a primeira dica: "))
    dicas.append(dica1)
    dica2 = str(input("Informe a segunda dica: "))
    dicas.append(dica2)
    dica3 = str(input("Informe a terceira dica: "))
    dicas.append(dica3)
    
    
    limparTela()
    
    letras_descobertas = [] #loop para adicionar "*" do tamanho da palavra secreta
    for i in range(0, len(palavra)):
        letras_descobertas.append("_")

    print("Vez de: ",competidor,"\nNúmero de letras da palavra chave: ")
    for x in letras_descobertas:
        print(x, end= ' ')

    acertou = False
    erros = 0
    acertos = 0
    nDicas = 0
    while acertou == False and erros <3:

        print("\n############## Escolha uma opção: ##############")
        print("1- Jogar")
        print("2- Solicitar dica")
        opcao = input("\n")

        if opcao == "1":
            letra = str(input("\nDigite a letra: "))

            if letra in palavra:
                acertos +=1
            else:
                erros += 1
                print("Erros: ",erros)
            if erros == 3:
                print("Você perdeu, ",competidor)

        
            for i in range(0, len(palavra)) :
                if letra == palavra[i]:
                    letras_descobertas[i] = letra
                acertou = True
            for x in letras_descobertas:
                print(x, end= ' ')
                    

            for x in range(0, len(letras_descobertas)):
                if letras_descobertas[x] == "_":
                    acertou = False
                
    
        elif opcao == "2":
            
            nDicas += 1

            if nDicas >len(dicas):
                print("Você não tem mais dicas!")
            else:
                print("\n",dicas[nDicas-1])
            
            letra = str(input("\nDigite a letra: "))

            if letra in palavra:
                acertos +=1
            else:
                erros += 1
                print("Erros: ",erros)
            if erros == 5:
                print("Você perdeu, ",competidor)

            

            for i in range(0, len(palavra)) :
                if letra == palavra[i]:
                    letras_descobertas[i] = letra
                acertou = True
            for x in letras_descobertas:
                print(x, end= ' ')
                    

            for x in range(0, len(letras_descobertas)):
                if letras_descobertas[x] == "_":
                    acertou = False


        else:
            print("Opção inválida!")
    if acertou == True:
        print("\nVocê venceu, ",competidor)        

    continuar = str(input("Jogar novamente? S ou N\n"))

    if continuar == "n":
            break

    limparTela()    


        

                      

    
         
                    
            
        
