from tkinter import *
from labirintozinho import *

corredor = '0'
parede = '1'

master = Tk()
master.title('Labirinto')
labirinto = Maze()
labirinto.read_map()
num_linhas = labirinto.num_linhas
num_colunas = labirinto.num_colunas
altura = num_linhas * 32
largura = num_colunas * 32
mapa_inicio = labirinto.map
print(mapa_inicio)
master.geometry(f'{largura}x{altura}')

master.wm_resizable() #não permitir que a tela possa ser redimensionada

#paredes.place(x=50, y=10, width=100,height=20)

for i, linha in enumerate(mapa_inicio):
    for j, coluna in enumerate(mapa_inicio[i]):
        if mapa_inicio[i][j] == parede:
            paredes = Label(master, background='#000000', foreground='#999050')
            paredes.place(x=30*j, y=30*i, width=30,height=30)

        elif mapa_inicio[i][j] == mouse:
            rato = Label(master, background='#964b00')
            rato.place(x=30*j, y=30*i, width=30,height=30)
        
        elif mapa_inicio[i][j] == saida:
            final_lab = Label(master, background='#FFFF00')
            final_lab.place(x=30*j, y=30*i, width=30,height=30)
        
        elif mapa_inicio[i][j] == corredor:
            corredores = Label(master, background='#CCC')
            corredores.place(x=30*j, y=30*i, width=30,height=30)

        elif mapa_inicio[i][j] == percorrido:           
            percorridos = Label(master, background='#CCCC74')
            percorridos.place(x=30*j, y=30*i, width=30,height=30)

master.mainloop()