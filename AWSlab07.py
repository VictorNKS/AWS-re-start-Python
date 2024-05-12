#Exercicio 1

userReply = input("Do you need to ship a package? (Enter yes or no) ")
#Coletando dados do usuario com a resposta de sim ou nao atraves da função input, a mensagem entre parenteses é a mensagem que vai aparecer para o usuario

if userReply == "yes":
    print("We can help you ship that package!")
#Se ele falar "sim", vai aparecer a mensagem acima e o simbolo == representa "igual a" é um comparativo

#Exercicio 2

else:
    print("Please come back when you need to ship a package. Thank you.")
#Se a resposta nao for "yes" o codigo vai dar print na mensagem acima

\
#Exercicio 3

userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
#É possivel responder por meio de 3 variaveis... o "elif" é usado neste caso... se ele nao responder stamps, ele passa para a resposta do envelope e se ele nao responder do envelope ele vai para o copy
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
#O {} dentro da string sera substituido pela variavel copies ou seja... o numero que o usuario inserir vai aparecer no print
#O format vai trazer valores para string, neste caso indicando a variavel copies
else:
    print("Thank you, please come again.")
#Se ele não responder nenhuma das 3 opções, a resposta sera dada neste else