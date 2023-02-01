from stack import Stack


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

    def run(self):
        self.__read_map()
        self.resolve()

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

    def posicao_valida(self, linha_atual, coluna_atual):
        if linha_atual > self.num_linhas or coluna_atual > self.num_colunas or linha_atual < 0 or coluna_atual < 0:
            print("Posição inválida, fora do mapa!")
            return False
        else:
            return True

    def resolve_rec(self, cur_row, cur_col):
        print(f'\n({cur_row}, {cur_col})')
        if self.map[cur_row][cur_col] == saida:
            print('Saída encontrada')
            return True
        else:

            aux = list(self.map[cur_row])
            # print(aux)
            aux[cur_col] = percorrido
            aux = ''.join(i for i in aux)
            self.map[cur_row] = aux
            # self.print_map()
            achou = False

            num_mov = 0
            # direita
            if not achou and self.posicao_valida(cur_row, cur_col + 1) and self.map[cur_row][cur_col + 1] in (corredor, saida):
                achou = self.resolve_rec(cur_row, cur_col + 1)

                # esquerda
            elif not achou and self.posicao_valida(cur_row, cur_col - 1) and self.map[cur_row][cur_col - 1] in (corredor, saida):
                achou = self.resolve_rec(cur_row, cur_col - 1)

                # baixo
            elif not achou and self.posicao_valida(cur_row + 1, cur_col) and self.map[cur_row + 1][cur_col] in (corredor, saida):
                achou = self.resolve_rec(cur_row + 1, cur_col)

                # cima
            elif not achou and self.posicao_valida(cur_row, cur_col - 1) and self.map[cur_row - 1][cur_col] in (corredor, saida):
                achou = self.resolve_rec(cur_row - 1, cur_col)
            # self.resolve_rec(cur_row, cur_col)
        #return achou

    def resolve(self):
        self.resolve_rec(self.entrada[0], self.entrada[1])


lab = Maze()
# print(lab)
lab.run()
lab.print_map()
# print(lab)
