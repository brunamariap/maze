mouse = 'm'
corredores = '0'
paredes = '1'
saida = 'e'
percorrido = '.'

class Maze:
    def __init__(self):
        self.map = None
        self.inicio = None
        self.fim = None

    def read_map(self):
        with open('labirinto.txt', 'r') as file:
            self.map = file.read()
        self.map = self.map.split('\n') # Separa em sublistas
        print(self.map)
    
    def __current_cell(self):
        pass

    def __entry_cell(self):
        pass

    def __exit_cell(self):
        pass

""" import time
time.sleep() """
lab = Maze()
lab.read_map()