mouse = 'm'
corredores = '0'
paredes = '1'
saida = 'e'
percorrido = '.'

""" ordem dos caminhos: direita, esquerda, baixo e cima. """

class Maze:
    def __init__(self):
        self.map = None
        self.entrada = None
        self.fim = None

    def read_map(self):
        with open('labirinto.txt', 'r') as file:
            self.map = file.read()
        self.map = self.map.split('\n') # Separa em sublistas
        print(self.map)
        num_colunas = len(self.map[0])
        num_linhas = len(self.map)

        for i in self.map:
            #print(i)
            if len(i) != num_colunas:
                raise ValueError('O mapa não possui as mesmas dimensões')

        pos_mouse = -1
        pos_saida = -1
        for i, linha in enumerate(self.map):
            if pos_mouse == -1:
                try:
                    pos_mouse = linha.index(mouse)
                    if pos_mouse >= 0:
                        self.entrada = (i, pos_mouse)
                except:
                    if i == num_linhas - 1:
                        raise ValueError("O mapa não possui entrada")
                
            if pos_saida == -1:
                try:
                    pos_saida = linha.index(saida)
                    if pos_saida >= 0:
                        self.fim = (i, pos_saida)
                except:
                    if i == num_linhas - 1:
                        raise ValueError("O mapa não possui saída")
        
        print(self.entrada)
        print(self.fim)


    
    def __posicao_valida(self):
        pass
    
    def __resolve_labirinto(self):
        pass

    def __resolve_labirinto_recursivo(self):
        pass

lab = Maze()
lab.read_map()