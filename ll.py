class Node:
    def __init__(self, data):
        # El diccionario contiene: Nombre de canción, Artista, Álbum
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"| {self.data['nombre']} |"


class LinkedList:
    def __init__(self):
        self.start = None
        self.current = None

    def append(self, data):
        new_node = Node(data)
        
        #Si la lista está vacía
        if self.start is None:
            self.start = new_node
            self.current = new_node
            return
        
        # Recorreshasta el final para insertar (Estilo Clase)
        actual = self.start
        while actual.next is not None:
            actual = actual.next
        
        # Conexión doble (punteros next y prev)
        actual.next = new_node
        new_node.prev = actual

    def next_song(self):
        if self.current and self.current.next:
            self.current = self.current.next
        return self.current

    def prev_song(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
        return self.current