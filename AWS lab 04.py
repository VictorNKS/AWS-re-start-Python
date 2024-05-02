myFruitList = ["apple", "banana", "cherry"]
#O comando list cria uma lista e a numeração das variaveis começa do 0 em diante

print(myFruitList)

print(type(myFruitList))

print(myFruitList[0])

print(myFruitList[1])

print(myFruitList[2])

myFruitList[2] = "orange"
#Na forma sequencial do codigo é mudado em determinado momento uma variavel... nao vai aparecer no inicio porque foi feito apos o print da primeira lista e o codigo de alteração veio depois do print

print(myFruitList)

\
#Exercicio 2

myFinalAnswerTuple = ("apple", "banana", "pineapple")
#O comando turple é como se fosse uma lista mas não pode ser alterada

print(myFinalAnswerTuple)

print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])

print(myFinalAnswerTuple[1])

print(myFinalAnswerTuple[2])

# myFinalAnswerTuple[2] = "orange"
# print(myFinalAnswerTuple)
# vai trazer um erro TypeError: 'tuple' object does not support item assignment, que seria referente o turple nao "suportar" este comando para alteração

\
#Exercicio 3

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
#Comando dictionary vai atrelar 2 variaveis, caso vc de o print da primeira variavel vai mostrar o par dela Ex Eu : Voce no print(myFavoriteFruitDictionary["Eu"]) o resultado vai ser Voce

print(myFavoriteFruitDictionary)

print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])

print(myFavoriteFruitDictionary["Saanvi"])

print(myFavoriteFruitDictionary["Paulo"])