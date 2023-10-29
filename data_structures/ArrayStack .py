from ArrayList import ArrayList

class ArrayStack:
    
    def __init__(self):
        self.data = ArrayList()
        #pass
        
        
    def __len__(self): # theta(1)
        return len(self.data)
        #pass
        
    
    def is_empty(self): # theta(1)
        return len(self.data) == 0
        #pass
        

    def push(self,item): # amortized theta(1)
        self.data.append(item)
        #pass
        
        
    
    def pop(self):# amortized theta(1)
        if (self.is_empty() == True):
            raise Exception("Stack is Empty!!!")
        return self.data.pop()
        #pass
    
    def top(self): #theta(1)
        if (self.is_empty()):
            raise Exception("Stack is Empty!!!")
        return self.data[-1]
        #pass
            


stack = ArrayStack()
stack.append(5)
'''
def flaten(S):

    stack = ArrayStack()
    while len(S) != 0 :
        val = S.pop()
        if isinstance(Val, list):
            S.extend(val)

        else:
            stack.push(S)

    while not stack.isempty:
        S.append(stack.pop())

S = [1,2,3,4,1,2,3,4,1,2,3,4,[[[[[[8,7,6,5]]]]]]]
print(flaten(S))
    
    '''
    
