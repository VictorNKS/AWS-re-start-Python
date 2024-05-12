#Importa todo o arquivo AWSlab14 como uma biblioteca, tirei todos os espaços para evitar bugs (antes nao estava dando para fazer o lab)
import AWSlab14
#Define o valor da variavel data deste arquivo como a função do arquivo AWSlab14 que era abrir o arquivo insulin.json e trazer os dados
data = AWSlab14.RJF('JSON Files/insulin.json')
#Se o valor de data nao for igual a : (retorna como true, dizendo que não é igual)
if data != "" :
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
# Calculating the molecular weight of insulin  
# Getting a list of the amino acid (AA) weights  
    aaWeights = data['weights']
# Count the number of each amino acids  
    aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})  
# Multiply the count by the weights  
    molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  

    print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))

    print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))

else :
    print("Error. Exiting program")