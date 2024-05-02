myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
    
#Comando for é usado para criar um loop para cada item da lista
#Comando format controla aonde vao ser inseridos os dados na string que esta sendo printada na tela... "item" seria o valor do primeiro {} e o "type(item)" seria o valor do segundo {}