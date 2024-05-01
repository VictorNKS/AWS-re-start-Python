#Por meio do comando ctrl + shift + p abri o Command Palette e digitei Start REPL para abrir o Python shell no VS Code

import tkinter as tk
#O comando "import" é usado para acessar uma biblioteca que ja vem dentro do Python... no header do codigo é necessario ter o nome da biblioteca e o nome do modulo... por ser um pensamento "sequencial" é necessario que seja feito o import da biblioteca no inicio... no caso o tkinter é o nome da biblioteca e "tk" é o "alias"

from tkinter import PhotoImage
#De dentro da biblioteca tkinter, escolhi a opção "PhotoImage" para mostrar uma imagem... ela permite criar e mostrar imagems em aplicações do Tkinter

from pathlib import Path
#É necessario importara biblioteca pathlib para atribuir uma variavel em um arquivo que eu vou defenir o diretorio dentro do meu repositorio com o a função Path... entao se eu tiver la \imagens\Joaozinho.png, eu posso fazer o Path("imagens/Joaozinho.png") e tambeem posso fazer uma variavel para path ou seja.. joaoft = Path("imagens/Joaozinho.png"), toda vez que eu usar a variavel joaoft ele vai me mostrar o caminho da imagem

window = tk.Tk()
#Window representa uma janela(instancia) que vai sair, o tk(alias) representa a biblioteca do tkinter e "Tk" representa a função, ele cria uma instancia da janela
#Deste modo seria.... a criação da janela = a biblioteca tkinter + a funcionalidade Tk
#Window é uma variavel que vai representar a janela criada pela função ".Tk()"

awslab2 = Path("Imagens/AWS lab 02.png")
#A variavel que eu atribui ao Path que esta dizendo aonde esta a foto no meu repositorio

imagemdawslab2 = PhotoImage(file=awslab2)
#PhotoImage e a variavel que vai mostrar a imagem na janela e o caminho dela... o "file" vai mostrar o caminho da imagem, ou seja esta me apontando para a variavel awslab2 que é o caminho da imagem
#Então o imagemdawslab2 é a variavel que eu atribui para mostrar a imagem

mostraAWSlab2 = tk.Label(window, image=imagemdawslab2)
#O tk.Label é uma ferramenta da biblioteca tkinter que vai "mostrar" a imagem em uma janela, ela funciona junto com a ferramenta window que representa a janela principal da tkinter
#O comando widow vai criar uma instancia da classe Tk e o Label é criado dentro da instancia widow para exibir a imagem que foi pre definida como uma variavel imaagemdawslab2
#A variavel mostraAWSlab2 foi dada para a fazer o processo de abrir uma janela com a imagem
# mostraAWSlab2 = tk.Label(tk.Tk(), image=PhotoImage(file="Imagens/AWS lab 02.png") seria +/- a equação do codigo

mostraAWSlab2.pack()
# mostraAWSlab2 é a variavel e o .pack() é o comando que exibe graficamente a imagem em um container

window.mainloop()
#O .mainloop() é responsavel pela a interface grafica ficar ativa e interativa para receber ações do usuario

#Neste lab usei ajuda de AI para estruturar o codigo, por ser meus primeiros passos com o Python
#O motivo pelo qual estou fazendo este arquivo com observações é para futuramente eu possa estudar o que eu fiz por autolearning 