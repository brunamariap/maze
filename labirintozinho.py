from labirintozinho import *
from stack import Stack
from tkinter import *


mouse = 'm'
corredor = '0'
parede = '1'
saida = 'e'
percorrido = '.'


class Maze:
    def __init__(self):
        self.map = None
        self.entrada = None
        self.fim = None
        self.num_linhas = None
        self.num_colunas = None
        self.pilha = Stack()

        """ ordem dos caminhos: direita, esquerda, baixo e cima. """
        self.deslocamento_linhas = (0, 0, 1, -1)
        self.deslocamento_colunas = (1, -1, 0, 0)
        self.num_movimentos = 4

    def run(self):
        # self.read_map()
        if not self.map:
            self.read_map()
        while not self.encontrar_saida():
            self.print_map()
        self.master.destroy()

    def read_map(self):
        with open('labirinto.txt', 'r') as file:
            self.map = file.read()
        self.map = self.map.split('\n')  # Separa em sublistas
        print(self.map)
        self.num_colunas = len(self.map[0])
        self.num_linhas = len(self.map)

        for i in self.map:
            # print(i)
            if len(i) != self.num_colunas:
                raise ValueError(
                    'As linhas não pussuem o mesmo total de colunas')

        pos_mouse = None
        pos_saida = None
        for i, linha in enumerate(self.map):
            if pos_mouse is None:
                try:
                    pos_mouse = linha.index(mouse)
                    if pos_mouse:
                        self.entrada = (i, pos_mouse)
                except:
                    if i == self.num_linhas - 1:
                        raise ValueError("O mapa não possui entrada")

            if pos_saida is None:
                try:
                    pos_saida = linha.index(saida)
                    if pos_saida:
                        self.fim = (i, pos_saida)
                except:
                    if i == self.num_linhas - 1:
                        raise ValueError("O mapa não possui saída")

        self.pilha.push((self.entrada[0], self.entrada[1]))
        print(self.entrada)
        print(self.fim)

    def print_map(self):
        for linha in self.map:
            print(linha)
        print('\n')

    def posicao_valida(self, linha_atual, coluna_atual):
        if linha_atual > self.num_linhas or coluna_atual > self.num_colunas or linha_atual < 0 or coluna_atual < 0:
            print("Posição inválida, fora do mapa!")
            return False
        else:
            return True

    def encontrar_saida(self,):
        topo = self.pilha.peek()
        print(self.pilha)

        # while achou is False:
        """ if self.map[topo[0]][topo[1]] == 'e':
            return True """

        self.draw_interface()
    
        if topo == self.fim:
            return True

        elif self.posicao_valida(topo[0], topo[1] + 1) and self.map[topo[0]][topo[1] + 1] in (corredor, saida):
            self.print_percorrido()
            aux = list(self.map[topo[0]])
            aux[topo[1] + 1] = mouse
            aux = ''.join(i for i in aux)
            self.map[topo[0]] = aux
            self.pilha.push((topo[0], topo[1] + 1))

        elif self.posicao_valida(topo[0], topo[1] - 1) and self.map[topo[0]][topo[1] - 1] in (corredor, saida):
            self.print_percorrido()
            aux = list(self.map[topo[0]])
            aux[topo[1] - 1] = mouse
            aux = ''.join(i for i in aux)
            self.map[topo[0]] = aux
            self.pilha.push((topo[0], topo[1] - 1))

        elif self.posicao_valida(topo[0] + 1, topo[1]) and self.map[topo[0] + 1][topo[1]] in (corredor, saida):
            self.print_percorrido()
            aux = list(self.map[topo[0] + 1])
            aux[topo[1]] = mouse
            aux = ''.join(i for i in aux)
            self.map[topo[0] + 1] = aux
            self.pilha.push((topo[0] + 1, topo[1]))

        elif self.posicao_valida(topo[0] - 1, topo[1]) and self.map[topo[0] - 1][topo[1]] in (corredor, saida):
            self.print_percorrido()
            aux = list(self.map[topo[0] - 1])
            aux[topo[1]] = mouse
            aux = ''.join(i for i in aux)
            self.map[topo[0] - 1] = aux
            self.pilha.push((topo[0] - 1, topo[1]))

        elif len(self.pilha) == 0:
            print('Não existe saída')
            return False

        else:
            aux = list(self.map[topo[0]])
            aux[topo[1]] = percorrido
            aux = ''.join(i for i in aux)
            self.map[topo[0]] = aux
            #self.pilha.push((topo[0] - 1, topo[1]))
            print('entrou')
            self.pilha.pop()

        return False

    def print_percorrido(self):
        topo_p = self.pilha.peek()
        aux = list(self.map[topo_p[0]])
        aux[topo_p[1]] = percorrido
        aux = ''.join(i for i in aux)
        self.map[topo_p[0]] = aux
        #self.pilha.push((topo[0] - 1, topo[1]))

    def draw_interface(self):
        self.master = Tk()
        self.master.title('Labirinto')
        altura = self.num_linhas * 32
        largura = self.num_colunas * 32
        mapa_inicio = self.map
        print(mapa_inicio)
        self.master.geometry(f'{largura}x{altura}')

        self.master.wm_resizable()  # não permitir que a tela possa ser redimensionada

        #paredes.place(x=50, y=10, width=100,height=20)

        for i, linha in enumerate(mapa_inicio):
            for j, coluna in enumerate(mapa_inicio[i]):
                if mapa_inicio[i][j] == parede:
                    paredes = Label(self.master, background='#000000',
                                    foreground='#999050')
                    paredes.place(x=32*j, y=32*i, width=32, height=32)

                elif mapa_inicio[i][j] == mouse:
                    rato = Label(self.master, background='#964b00')
                    rato.place(x=32*j, y=32*i, width=32, height=32)

                elif mapa_inicio[i][j] == saida:
                    final_lab = Label(self.master, background='#FFFF00')
                    final_lab.place(x=32*j, y=32*i, width=32, height=32)

                elif mapa_inicio[i][j] == corredor:
                    corredores = Label(self.master, background='#CCC')
                    corredores.place(x=32*j, y=32*i, width=32, height=32)

                elif mapa_inicio[i][j] == percorrido:
                    percorridos = Label(self.master, background='#CCCC74')
                    percorridos.place(x=32*j, y=32*i, width=32, height=32)

        self.master.mainloop()


# print(lab)
lab = Maze()
lab.run()
# print(lab)
