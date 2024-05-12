import random
#Faz a importação do modulo random da biblioteca do Python, tem a funcionalidade de trabalhar com numeros aleatorios
number = random.randint(1, 10)
# Toda vez que o código rodar, ele vai selecionar um número aleatório entre 1 e 10
isGuessRight = False
# Determinando o valor da variável como falso... então, quando iniciar o código, a variável isGuessRight vai ser falso e não haverá conflito, pois se fosse true ele iria parar no while
attempts = 0
#Atribui a variável attempts o valor 0
while not isGuessRight:
# Enquanto o valor da variável for falso, ele vai repetir o loop
    guess = input("Guess a number between 1 and 10: ")
    attempts += 1
#Adiciona 1 a cada vez que o loop for executado, ate o usuario acertar ele vai salvar as tentativas
    if int(guess) == number:
# Se o valor do input for igual ao valor da variável number, ele vai mostrar a mensagem que o usuário venceu
        print("You guessed {}. That is correct! You win!".format(guess))
        print("Number of attempts:", attempts)
# Mostra o número de tentativas que o usuário levou para acertar
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))



#Neste exercicio nao tinha a variavel "attemtps", eu fiz isso para mostrar quantas tentativas o usuário levou para acertar com ajuda do chatgpt (fiz por curiosidade)

"""
import random
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
"""