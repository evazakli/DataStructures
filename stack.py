class Stack():

    def __init__(self):
        self.items = []

    def is_empty(self): #Status Check ---> True/False
        return self.items == []

    def push(self,item): #Insert Operation
        self.items.append(item)

    def pop(self): #Delete Operation ---> Removes Top Item
        if self.items == []:
            raise Exception("Stack is empty")
        else:
            return self.items.pop()
    
    def peek(self): #Inspect Operatiom ---> Returns The TopItem
        if self.items == []:
            raise Exception("Stack is empty")
        else:
            return self.items[-1]

    def size(self): #Size Check 
        return len(self.items)
