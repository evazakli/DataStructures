class Queue():

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self,item):    # adds one element to the rear of the queue
        self.items.insert(0,item)   

    def dequeue(self):    # removes one element from the front of the queue
        if self.items == []:
            raise Exception("Queue is empty")
        else:
            return self.items.pop()
        
    def size(self):
        return len(self.items)
        
    
# Time complexity in big O notation

#   Operation      Average      Worst case
#    Search          O(n)         O(n)
#    Insert          O(1)         O(1)
#    Delete          O(1)         O(1)

# Space complexity 
# O(n) ---> average and worst case 
