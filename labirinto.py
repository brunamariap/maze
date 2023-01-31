from stack import Stack


mouse = 'm'
corredor = '0'
paredes = '1'
saida = 'e'
percorrido = '.'
solucao = 'S'
errado = 'X'


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
        self.resolve()

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

    
    def print_map(self):
        for linha in self.map:
            print(linha)
        print('\n')

    def resolve(self):
        #pilha = Stack()
        def posicao_valida(linha_atual, coluna_atual):
            if linha_atual > self.num_linhas or coluna_atual > self.num_colunas or linha_atual < 0 or coluna_atual < 0:
                print("Posição inválida, fora do mapa!")
                return False
            else:
                return True

        def encontra_saida(linha_atual, coluna_atual):
            """Função recursiva para encontrar a saída"""
            if self.map[linha_atual][coluna_atual] == saida:
                print("saída")
                self.print_map()
                return True
            else:
                """
                Marcar o caminho como percorrido
                ordem dos caminhos: direita, esquerda, baixo e cima. """
                #print(self.map[linha_atual][coluna_atual])
                aux = list(self.map[linha_atual])
                #print(aux)
                aux[coluna_atual] = percorrido
                aux = ''.join(i for i in aux)
                self.map[linha_atual] = aux
                #print(self.map)
                self.print_map()
                #self.map[linha_atual]
                achou = False

                #direita
                if not achou and posicao_valida(linha_atual, coluna_atual + 1) and self.map[linha_atual][coluna_atual + 1] == corredor: 
                    achou = encontra_saida(linha_atual, coluna_atual + 1)
                
                #esquerda
                elif not achou and posicao_valida(linha_atual, coluna_atual - 1) and self.map[linha_atual][coluna_atual - 1] == corredor: 
                    achou = encontra_saida(linha_atual, coluna_atual - 1)
                
                #baixo
                elif not achou and posicao_valida(linha_atual + 1, coluna_atual) and self.map[linha_atual + 1][coluna_atual] == corredor: 
                    achou = encontra_saida(linha_atual + 1, coluna_atual)
                
                #cima
                elif not achou and posicao_valida(linha_atual, coluna_atual - 1) and self.map[linha_atual - 1][coluna_atual] == corredor: 
                    achou = encontra_saida(linha_atual - 1, coluna_atual)

            """ if achou:
                #self.map[linha_atual][coluna_atual] = solucao
                aux = list(self.map[linha_atual])
                #print(aux)
                aux[coluna_atual] = solucao
                aux = ''.join(i for i in aux)
                self.map[linha_atual] = aux
                print("achou2")
            else:
                aux = list(self.map[linha_atual])
                #print(aux)
                aux[coluna_atual] = errado
                aux = ''.join(i for i in aux)
                self.map[linha_atual] = aux """
            
        return encontra_saida(self.entrada[0], self.entrada[1])

lab = Maze()
#print(lab)
lab.run()
lab.print_map()
#print(lab)