myString = "This is a string."
print(myString)

print(type(myString))

print(myString + " is of the data type " + str(type(myString)))

\
#Exercicio 2

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

\
#Exercicio 3

name = input("What is your name? ")
#Comando input esta atrelando uma string a uma variavel

print(name)

#Exercicio 4

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name,color,animal))
#Esse print esta trazendo de forma sequencial as informações que eu botei no console... no caso o nome Victor, cor azul e animal passaro
#O resultado seria "Victor, you like a blue bird!"