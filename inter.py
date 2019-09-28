
import numpy as np
import cv2

from tkinter import *
from oper import *

janela = Tk()
janela.geometry("550x380")
janela.title("Manipulação Formas Geometricas")
heading = Label(text="Manipulação de Imagens", bg="#cee5eb", fg="black",
                width="500", height="3")
heading.pack()

arvore = Button(janela, text="Imagem", width="10", height="2", command=imag, bg="#7dc7dc")
arvore.place(x=20, y=120)

histograma = Button(janela, text="Histograma", width="25", height="2", command=histo, bg="#7dc7dc")
histograma.place(x=150, y=120)

lb11 = Label(janela, text="DICA: Use Tab para navegar, espaço para selecionar. Alt F4 para fechar!", bg="#cee5eb")
lb11.place(x=110, y=335)

janela.mainloop()










