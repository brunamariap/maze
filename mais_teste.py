import os
import time
import sys
import random

mouse = 'm'
corredor = '0'
paredes = '1'
saida = 'e'
percorrido = '.'

entrada = []
fim = []


def read_map():
    with open('labirinto.txt', 'r') as file:
        mapinha = file.read()
    mapinha = mapinha.split('\n')  # Separa em sublistas
    print(mapinha)
    num_col = len(mapinha[0])
    num_linhas = len(mapinha)

    for i in mapinha:
        # print(i)
        if len(i) != num_col:
            raise ValueError(
                'As linhas não pussuem o mesmo total de colunas')

    pos_mouse = None
    pos_saida = None
    for i, linha in enumerate(mapinha):
        if pos_mouse is None:
            try:
                pos_mouse = linha.index(mouse)
                if pos_mouse:
                    entrada.extend((i, pos_mouse))
            except:
                if i == num_linhas - 1:
                    raise ValueError("O mapa não possui entrada")

        if pos_saida is None:
            try:
                pos_saida = linha.index(saida)
                if pos_saida:
                    fim = (i, pos_saida)
            except:
                if i == num_linhas - 1:
                    raise ValueError("O mapa não possui saída")
    return mapinha


def display_maze(m, path):
    m2 = m[:]
    # os.system('cls')  # windows use 'cls'

    for item in path:
        #m2[item[0]][item[1]] = "."
        aux = list(m2[item[0]])

        aux[item[1]] = percorrido
        aux = ''.join(i for i in aux)
        m2[item[0]] = aux
    #m2[path[-1][0]][path[-1][1]] = "M"
    aux = list(m2[path[-1][0]])
    aux[path[-1][1]] = percorrido
    aux = ''.join(i for i in aux)
    m2[path[-1][0]] = aux

    draw = ""

    for row in m2:
        for item in row:
            item = str(item).replace("1", "█")
            item = str(item).replace("2", " ")
            item = str(item).replace("0", " ")

            draw += item
        draw += "\n"
    print(draw)


def move(path):
    time.sleep(0.3)
    cur = path[-1]
    display_maze(maze, path)
    possibles = [(cur[0], cur[1] + 1), (cur[0], cur[1] - 1),
                 (cur[0] + 1, cur[1]), (cur[0]-1, cur[1])]
    #random.shuffle(possibles)

    for item in possibles:
        if item[0] < 0 or item[1] < 0 or item[0] > len(maze) or item[1] > len(maze[0]):
            continue
        elif maze[item[0]][item[1]] in ["1", "2"]:
            continue
        elif item in path:
            continue
        elif maze[item[0]][item[1]] == saida:
            path = path + (item,)
            display_maze(maze, path)
            input("Solution found! Press enter to finish")
            #os.system('cls')  # windows use 'cls'
            sys.exit()
        else:
            newpath = path + (item,)
            move(newpath)
            #maze[item[0]][item[1]] = "2"
            aux_maze = list(maze[item[0]])
            aux_maze[item[1]] = '2'
            aux_maze = ''.join(i for i in aux_maze)
            maze[item[0]] = aux_maze
            display_maze(maze, path)
            time.sleep(0.3)


maze = read_map()
move(((entrada[0], entrada[1]),))
