class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    
class Stack:
    def __init__(self):
        self.top = None # Topo da pilha
        self.size = 0

    
    def push(self, elem):
        # Insere no topo da pilha
        node = Node(elem) # Cria novo nó
        node.next = self.top # Liga ao restante da pilha, quando existe mais de um elemento liga o nó que era o antigo topo
        self.top = node # O topo agora será o novo nó
        self.size += 1

    
    def pop(self):
        # Remove o elemento do topo da pilha
        if self.size > 0:
            node = self.top
            self.top = self.top.next # O topo vira o próximo elemento 
            self.size -= 1
            return node.data
        raise IndexError('A pilha está vazia')

    
    def peek(self):
        # Retorna o topo sem remover
        if self.size > 0:
            return self.top.data
        raise IndexError('A pilha está vazia')


    def __len__(self):
        return self.size

    
    def __repr__(self):
        string = ''
        pointer = self.top
        print('\nElementos da pilha:')
        while pointer:
            string = string + str(pointer.data) + '\n'
            pointer = pointer.next
        return string
    

    def __str__(self):
        return self.__repr__()