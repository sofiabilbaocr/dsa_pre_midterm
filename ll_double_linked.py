class Node:
    def __init__(self, data):
        # El data sera el diccionario: Nombre, Artista, Album
        self.data = data
        self.next = None
        self.prev = None  # Agregamos el puntero anterior

    def __repr__(self):
        return "| " + self.data["nombre"] + " |"

class LinkedList:
    def __init__(self):
        self.start = None
        self.current = None  # Para saber que cancion suena

    def append(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            self.current = new_node
            return
        
        actual = self.start
        while actual.next is not None:
            actual = actual.next
        
        # Aqui la hace DOBLE
        actual.next = new_node
        new_node.prev = actual

    def next_song(self):
        if self.current is not None:
            if self.current.next is not None:
                self.current = self.current.next
        return self.current

    def prev_song(self):
        if self.current is not None:
            if self.current.prev is not None:
                self.current = self.current.prev
        return self.current