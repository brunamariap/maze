from stack import Stack


mouse = 'm'
corredores = '0'
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

    def run(self):
        self.__read_map()
        self.__resolve_labirinto(self.map, self.num_linhas, self.num_colunas)

    def __read_map(self):
        with open('labirinto.txt', 'r') as file:
            self.map = file.read()
        self.map = self.map.split('\n') # Separa em sublistas
        print(self.map)
        self.num_colunas = len(self.map[0])
        self.num_linhas = len(self.map)

        for i in self.map:
            #print(i)
            if len(i) != self.num_colunas:
                raise ValueError('As linhas não pussuem o mesmo total de colunas')

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

    
    def __print_labirinto(self):
        for i in self.map:
            print(i)

    
    def __posicao_valida(self, linha_atual, coluna_atual):
        """ Verifica se a posição atual é válida """
        if (linha_atual >= 0) and (coluna_atual >= 0) and (coluna_atual < self.num_colunas):
            if self.map[linha_atual][coluna_atual] == '0': # Se ele está no corredor e pode ser percorrido
                return True
        return False
    
    def __resolve_labirinto(self, labirinto, t_linhas, t_colunas):
        """ Inicia o percurso no labirinto, definindo a posição de partida e de chegada"""
        print('\n\n Caminho percorrido')
        self.__resolve_labirinto_recursivo(labirinto, self.entrada,self.fim, t_linhas - 1, t_colunas - 1)

    def __resolve_labirinto_recursivo(self, labirinto, pos_atual, pos_final, total_linhas, total_colunas):
        achou = False
        aux = 0 # variável q vai ajudar na contagem da caminhos possíveis

        if self.__posicao_valida(pos_atual[0], pos_atual[1]):
            labirinto[pos_atual][pos_atual] = '.'
            print('\n\n' + str(pos_atual))

            if pos_atual[0] == pos_final[0] and pos_atual[0] == pos_final[1]:
                print('\n\nAchou', pos_atual)
                achou = True
            
            while achou is False and aux < self.num_movimentos:
                achou = self.__resolve_labirinto_recursivo(labirinto,(pos_atual[0] + self.deslocamento_linhas[aux], pos_atual[1] + self.deslocamento_colunas[aux]), pos_final, total_linhas, total_colunas)
                aux += 1
                self.__print_labirinto()

            labirinto[pos_atual[0]][pos_atual[1]] = 0
        
        return achou
lab = Maze()
lab.run()