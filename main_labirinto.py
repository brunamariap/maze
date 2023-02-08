from stack import Stack
from tkinter import *


MOUSE = 'm'
CORREDOR = '0'
PAREDE = '1'
SAIDA = 'e'
PERCORRIDO = '.'


class Maze:
    def __init__(self):
        self.__map = None
        self.entrada = None
        self.fim = None
        self.num_linhas = None
        self.num_colunas = None
        self.__stack = Stack()

    def run(self):
        self.__read_map()
        while not self.__encontrar_saida():
            self.__print_map()

    def __read_map(self):
        with open('labirinto.txt', 'r') as file:
            self.__map = file.read()
        self.__map = self.__map.split('\n')
        self.num_colunas = len(self.__map[0])
        self.num_linhas = len(self.__map)

        for i in self.__map:
            if len(i) != self.num_colunas:
                raise ValueError(
                    'As linhas não pussuem o mesmo total de colunas')

        pos_mouse = None
        pos_saida = None
        for i, row in enumerate(self.__map):
            if pos_mouse is None:
                try:
                    pos_mouse = row.index(MOUSE)
                    if pos_mouse:
                        self.entrada = (i, pos_mouse)
                except:
                    if i == self.num_linhas - 1:
                        raise ValueError("O mapa não possui entrada")

            if pos_saida is None:
                try:
                    pos_saida = row.index(SAIDA)
                    if pos_saida:
                        self.fim = (i, pos_saida)
                except:
                    if i == self.num_linhas - 1:
                        raise ValueError("O mapa não possui saída")

        self.__stack.push((self.entrada[0], self.entrada[1]))
        print('Entrada:', self.entrada)
        print('Saída:', self.fim)

    def __print_map(self):
        for linha in self.__map:
            print(linha)
        print('\n')

    def __position_valid(self, linha_atual, coluna_atual):
        if linha_atual > self.num_linhas or coluna_atual > self.num_colunas or linha_atual < 0 or coluna_atual < 0:
            return False
        else:
            return True

    def __encontrar_saida(self,):
        top = self.__stack.peek()
        print(self.__stack)

        self.__draw_interface()

        if top == self.fim:
            return True

        # right
        elif self.__position_valid(top[0], top[1] + 1) and self.__map[top[0]][top[1] + 1] in (CORREDOR, SAIDA):
            self.__parte_percorrida()
            self.__mouse_position(0, 1)

        # left
        elif self.__position_valid(top[0], top[1] - 1) and self.__map[top[0]][top[1] - 1] in (CORREDOR, SAIDA):
            self.__parte_percorrida()
            self.__mouse_position(0, -1)

        # down
        elif self.__position_valid(top[0] + 1, top[1]) and self.__map[top[0] + 1][top[1]] in (CORREDOR, SAIDA):
            self.__parte_percorrida()
            self.__mouse_position(1, 0)

        # up
        elif self.__position_valid(top[0] - 1, top[1]) and self.__map[top[0] - 1][top[1]] in (CORREDOR, SAIDA):
            self.__parte_percorrida()
            self.__mouse_position(-1, 0)

        else:
            self.__parte_percorrida()
            self.__stack.pop()

            if len(self.__stack) == 0:
                raise ValueError('Não é possível encontrar a saída')

            top = self.__stack.peek()
            aux = list(self.__map[top[0]])
            aux[top[1]] = MOUSE
            aux = ''.join(i for i in aux)
            self.__map[top[0]] = aux

        return False

    def __parte_percorrida(self):
        top_p = self.__stack.peek()
        aux = list(self.__map[top_p[0]])
        aux[top_p[1]] = PERCORRIDO
        aux = ''.join(i for i in aux)
        self.__map[top_p[0]] = aux

    def __mouse_position(self, x, y):
        top = self.__stack.peek()
        aux = list(self.__map[top[0] + x])
        aux[top[1] + y] = MOUSE
        aux = ''.join(i for i in aux)
        self.__map[top[0] + x] = aux
        self.__stack.push((top[0] + x, top[1] + y))

    def __draw_interface(self):
        self.master = Tk()
        self.master.title('Labirinto')
        self.dimensoes_quadrado = 64
        altura = self.num_linhas * self.dimensoes_quadrado
        largura = self.num_colunas * self.dimensoes_quadrado
        mapa = self.__map
        self.master.geometry(f'{largura}x{altura}+317+34')

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
