class Deque:

    def __init__(self):
        self.items = []

    def add_right(self,item):
        self.items.append(item)

    def add_left(self,item):
        self.items.insert(0,item)  # left <---- [] ----> right

    def remove_right(self):
        if self.is_Empty():
            raise Exception("Deque is empty!")
        else:
            self.items.pop()

    def remove_left(self):
        if self.is_Empty():
            raise Exception("Deque is empty!")
        else:
            self.items.pop(0)

    def is_Empty(self):
        return self.items==[]

    def size(self):
        return len(self.items)

   	

