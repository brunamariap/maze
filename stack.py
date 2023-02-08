class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    
class Stack:
    def __init__(self):
        self.top = None 
        self.size = 0

    
    def push(self, elem):
        # Insere no topo da pilha
        node = Node(elem) 
        node.next = self.top 
        self.top = node
        self.size += 1

    
    def pop(self):
        if self.size > 0:
            node = self.top
            self.top = self.top.next
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