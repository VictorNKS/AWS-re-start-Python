# Python3.6  
# Coding: utf-8  
# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

#Criando um  novo dicionatio com a variavel pKR e atribuindo valores ao y c k h r d e
pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}
insulin.count("Y")
#Conta o numero de ocorrencia de cada aminoacido
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

#Variavel pH é atribuida com valor 0
pH = 0

#criando um loop que vai de 0 a 14, ele vai continuar ate o valor de pH ser igual 14
while (pH <= 14): 
    netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))
    pH +=1

#Imprime o valor de pH e o valor de netCharge
print('{0:.2f}'.format(pH), netCharge)
