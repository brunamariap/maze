from stack import Stack
from tkinter import *


MOUSE = 'm'
CORREDOR = '0'
PAREDE = '1'
SAIDA = 'e'
PERCORRIDO = '.'


class Maze:
    def __init__(self):
        self.map = None
        self.entrada = None
        self.fim = None
        self.num_linhas = None
        self.num_colunas = None
        self.pilha = Stack()

    def run(self):
        self.__read_map()
        while not self.__encontrar_saida():
            self.__print_map()

    def __read_map(self):
        with open('labirinto.txt', 'r') as file:
            self.map = file.read()
        self.map = self.map.split('\n')
        self.num_colunas = len(self.map[0])
        self.num_linhas = len(self.map)

        for i in self.map:
            if len(i) != self.num_colunas:
                raise ValueError(
                    'As linhas não pussuem o mesmo total de colunas')

        pos_mouse = None
        pos_saida = None
        for i, linha in enumerate(self.map):
            if pos_mouse is None:
                try:
                    pos_mouse = linha.index(MOUSE)
                    if pos_mouse:
                        self.entrada = (i, pos_mouse)
                except:
                    if i == self.num_linhas - 1:
                        raise ValueError("O mapa não possui entrada")

            if pos_saida is None:
                try:
                    pos_saida = linha.index(SAIDA)
                    if pos_saida:
                        self.fim = (i, pos_saida)
                except:
                    if i == self.num_linhas - 1:
                        raise ValueError("O mapa não possui saída")

        self.pilha.push((self.entrada[0], self.entrada[1]))
        print('Entrada:', self.entrada)
        print('Saída:', self.fim)

    def __print_map(self):
        for linha in self.map:
            print(linha)
        print('\n')

    def __position_valid(self, linha_atual, coluna_atual):
        if linha_atual > self.num_linhas or coluna_atual > self.num_colunas or linha_atual < 0 or coluna_atual < 0:
            return False
        else:
            return True

    def __encontrar_saida(self,):
        top = self.pilha.peek()
        print(self.pilha)

        self.__draw_interface()

        if top == self.fim:
            return True

        # right
        elif self.__position_valid(top[0], top[1] + 1) and self.map[top[0]][top[1] + 1] in (CORREDOR, SAIDA):
            self.__parte_percorrida()
            self.__mouse_current_position(0, 1)

        # left
        elif self.__position_valid(top[0], top[1] - 1) and self.map[top[0]][top[1] - 1] in (CORREDOR, SAIDA):
            self.__parte_percorrida()
            self.__mouse_current_position(0, -1)

        # down
        elif self.__position_valid(top[0] + 1, top[1]) and self.map[top[0] + 1][top[1]] in (CORREDOR, SAIDA):
            self.__parte_percorrida()
            self.__mouse_current_position(1, 0)

        # up
        elif self.__position_valid(top[0] - 1, top[1]) and self.map[top[0] - 1][top[1]] in (CORREDOR, SAIDA):
            self.__parte_percorrida()
            self.__mouse_current_position(-1, 0)

        else:
            self.__parte_percorrida()
            self.pilha.pop()

            if len(self.pilha) == 0:
                raise ValueError('Não é possível encontrar a saída')

            top = self.pilha.peek()
            aux = list(self.map[top[0]])
            aux[top[1]] = MOUSE
            aux = ''.join(i for i in aux)
            self.map[top[0]] = aux

        return False

    def __parte_percorrida(self):
        top_p = self.pilha.peek()
        aux = list(self.map[top_p[0]])
        aux[top_p[1]] = PERCORRIDO
        aux = ''.join(i for i in aux)
        self.map[top_p[0]] = aux

    def __mouse_current_position(self, x, y):
        top = self.pilha.peek()
        aux = list(self.map[top[0] + x])
        aux[top[1] + y] = MOUSE
        aux = ''.join(i for i in aux)
        self.map[top[0] + x] = aux
        self.pilha.push((top[0] + x, top[1] + y))

    def __draw_interface(self):
        self.master = Tk()
        self.master.title('Labirinto')
        self.dimensoes_quadrado = 64
        altura = self.num_linhas * self.dimensoes_quadrado
        largura = self.num_colunas * self.dimensoes_quadrado
        mapa = self.map
        self.master.geometry(f'{largura}x{altura}+317+34')

        # self.master.wm_resizable()

        for i, linha in enumerate(mapa):
            for j, coluna in enumerate(mapa[i]):
                if mapa[i][j] == PAREDE:
                    paredes = Label(self.master, background='#000000',
                                    foreground='#999050')
                    paredes.place(x=self.dimensoes_quadrado*j, y=self.dimensoes_quadrado*i,
                                  width=self.dimensoes_quadrado, height=self.dimensoes_quadrado)

                elif mapa[i][j] == MOUSE:
                    rato = Label(self.master, background='#964b00')
                    rato.place(x=self.dimensoes_quadrado*j, y=self.dimensoes_quadrado*i,
                               width=self.dimensoes_quadrado, height=self.dimensoes_quadrado)

                elif mapa[i][j] == SAIDA:
                    final_lab = Label(self.master, background='#FFFF00')
                    final_lab.place(x=self.dimensoes_quadrado*j, y=self.dimensoes_quadrado*i,
                                    width=self.dimensoes_quadrado, height=self.dimensoes_quadrado)

                elif mapa[i][j] == CORREDOR:
                    corredores = Label(self.master, background='#CCC')
                    corredores.place(x=self.dimensoes_quadrado*j, y=self.dimensoes_quadrado*i,
                                     width=self.dimensoes_quadrado, height=self.dimensoes_quadrado)

                elif mapa[i][j] == PERCORRIDO:
                    percorridos = Label(self.master, background='#CCCC74')
                    percorridos.place(x=self.dimensoes_quadrado*j, y=self.dimensoes_quadrado*i,
                                      width=self.dimensoes_quadrado, height=self.dimensoes_quadrado)

        self.master.mainloop()


lab = Maze()
lab.run()
