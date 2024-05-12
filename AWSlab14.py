
# importando a biblioteca json
import json

#criando uma função para a variavel readJsonFile e a defenindo como qualquer variavel... no caso usei o nome do arquivo json mesmo
def RJF(insulin_json):
    #variavel data nao teve o valor definido
    data = ""
    #abrindo o arquivo insulin_json que é o alias do readJsonFile(função), aqui esta sendo chamada a função do def e defenindo o conteudo do arquivo como uma variavel que no caso eu botei insulina
    with open(insulin_json) as insulina:
        #atribuindo a variavel data o comando da biblioteca que foi importada no inicio "import json", json.load(insulina)
        data = json.load(insulina)
#O comando json.load() lê o arquivo JSON linha por linha e converte os dados em um objeto Python. Isso permite que você trabalhe com os dados do arquivo JSON como se fossem um dicionário ou uma lista em Python.
    return data

# Call the function to read the JSON file and print its content
json_data = RJF("JSON Files/insulin.json")
#print(json_data) tirei o print apos criar o AWSlab14Calc

#Entao o codigo vai criar uma função e defenir como uma variavel chamada insulin_json
# a data= "" vai receber o conteudo do JSON... que no caso seria o insulin.json...

"""
O codigo seria assim no AWS mas eu mudei algumas variaveis acima para testar
import json
def readJsonFile(fileName):
data=""
def readJsonFile(fileName):
    data = ""
    with open('JSON Files/insulin.json') as json_file:
        data = json.load(json_file)
    return data
"""