import os
palavraChave = input("Informe a palavra chave: ")
os.system("cls")

letras_descobertas = [] #armazena cada chute que corresponde a uma letra da palavra secreta
print("Jogo da forca: ")

#loop para adicionar "*" do tamanho da palavra secreta
for i in range(0, len(palavraChave)):
    letras_descobertas.append("_")

acertou = False
for x in letras_descobertas:

        print(x, end= ' ')


while acertou == False :
    letra = str(input("\nDigite a letra: "))

    #loop percorrendo a palavra para verificar se a letra existe na palavra secreta
    for i in range(0, len(palavraChave)) :
        if letra == palavraChave[i]:
            letras_descobertas[i] = letra
        acertou = True     
    for x in letras_descobertas:

        print(x, end= ' ')

    

    #loop para testar se todas as letras foram descobertas
    for x in range(0, len(letras_descobertas)):
        if letras_descobertas[x] == "_":
            acertou = False   



print ("\nVitória!")
