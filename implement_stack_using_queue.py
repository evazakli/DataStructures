from collections import deque

# it consist of push, pop, top, empty methods
# use 2 queue

class Stack_w2_Queue:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()


    def push(self,item):                            # push(1): q1=[1], q2=[] -> q1=[], q2=[1]
        self.q1.appendleft(item)                    # push(2): q1=[2], q2[1] -> q1=[1,2], q2=[] -> q1=[], q2[1,2]
                                                    # push(3): q1=[3], q2[1,2] -> q1 =[1,2,3], q2=[] -> q1=[], q2[1,2,3] 
        while self.q2:                              # ... 
            self.q1.appendleft(self.q2.pop())       # O(N)

        self.q1,self.q2 = self.q2,self.q1



    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")
        else:
            return self.q2.pop()
        

    def top(self):
        if self.empty():
            raise Exception("Stack is empty")
        else:
            return self.q2[-1]


    def empty(self):
        return len(self.q2) == 0

        


    