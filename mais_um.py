from stack import Stack
import os
import time
import sys
import random


mouse = 'm'
corredor = '0'
paredes = '1'
saida = 'e'
percorrido = '.'


class Maze:
    def __init__(self):
        self.map = None
        self.entrada = None
        self.fim = None
        self.num_linhas = None
        self.num_colunas = None

        """ ordem dos caminhos: direita, esquerda, baixo e cima. """
        self.deslocamento_linhas = (0, 0, 1, -1)
        self.deslocamento_colunas = (1, -1, 0, 0)
        self.num_movimentos = 4

        self.pilha = Stack()

    def run(self):
        self.__read_map()

    def __read_map(self):
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

        print(self.entrada)
        print(self.fim)

    def print_map(self):
        for linha in self.map:
            print(linha)
        print('\n')

    def display_maze(self, m, path):
        m2 = m[:]
        os.system('cls')  # windows use 'cls'

        for item in path:
            m2[item[0]][item[1]] = "."
        m2[path[-1][0]][path[-1][1]] = "M"

        draw = ""

        for row in m2:
            for item in row:
                item = str(item).replace("1", "█")
                item = str(item).replace("2", " ")
                item = str(item).replace("0", " ")

                draw += item
            draw += "\n"
        print(draw)


    def move(self, path):
        time.sleep(0.3)
        cur = path[-1]
        self.display_maze(maze, path)
        possibles = [(cur[0], cur[1] + 1), (cur[0], cur[1] - 1),
                    (cur[0] + 1, cur[1]), (cur[0]-1, cur[1])]
        random.shuffle(possibles)

        for item in possibles:
            if item[0] < 0 or item[1] < 0 or item[0] > len(maze) or item[1] > len(maze[0]):
                continue
            elif maze[item[0]][item[1]] in ["1", "2"]:
                continue
            elif item in path:
                continue
            elif maze[item[0]][item[1]] == "B":
                path = path + (item,)
                self.display_maze(maze, path)
                input("Solution found! Press enter to finish")
                os.system('clear')  # windows use 'cls'
                sys.exit()
            else:
                newpath = path + (item,)
                self.move(newpath)
                maze[item[0]][item[1]] = "2"
                self.display_maze(maze, path)
                time.sleep(0.3)


    maze = get_maze('maze1.csv')

move(((1, 0),))
maze = Maze()
# print(lab)
maze.run()
# print(lab)
