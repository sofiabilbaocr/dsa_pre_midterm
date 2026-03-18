class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "| " + str(self.data) + " |"

class LinkedList:
    def __init__(self):
        self.start = None

    def append(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            return
        
        actual = self.start
        while actual.next is not None:
            actual = actual.next
        actual.next = new_node