
#Se eu quiser usar 2 codigos com a mesma variavel no mesmo arquivo e eu botar "\" separando os 2 codigos, nao havera conflito... ele usara a variavel com mesmo nome nos 2 codigos sem buscar valores misturados entre eles

#Exercicio 2
print("Python has three numeric types: int, float, and complex")

myValue=1
print(myValue)
#Print vai exibir o valor da minha variavel , myValue é minha variavel
print(type(myValue))
#Type é o tipo numerico... "int,float,complex"
print(str(myValue))
#O str converte a variavel em string, ou seja é uma sequencia de texto que podem ser numeros, letras, simbolos, caracteres especiais... neste caso ficaria print("1")
print(str(myValue) + " is of the data type " + str(type(myValue)))
# string(referente a conversão da variavel myValue para string) + string(referente ao texto literalmente) + string(referente ao type "int,float,complex") sendo exibidos por meio do print

\
#Exercicio 3

myValue=3.14
print(myValue)

print(type(myValue))

print(str(myValue))

print(str(myValue) + " is of the data type " + str(type(myValue)))

\
#Exercicio 4

myValue=5j
print(myValue)

print(type(myValue))

print(str(myValue))

print(str(myValue) + " is of the data type " + str(type(myValue)))

\
#exercicio 5

myValue=True
print(myValue)

print(type(myValue))

print(str(myValue))

print(str(myValue) + " is of the data type " + str(type(myValue)))

\
myValue=False
print(myValue)

print(type(myValue))

print(str(myValue))

print(str(myValue) + " is of the data type " + str(type(myValue)))