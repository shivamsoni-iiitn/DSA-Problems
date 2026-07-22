class myStack:
    def __init__(self, n):
        # Define Data Structures
        self.st=[0]*n
        self.size=n
        self.top=-1
        
    def isEmpty(self):
        # Check if stack is empty
        return self.top==-1
    
    def isFull(self):
        # Check if stack is full
        x=False
        if self.top>=self.size-1:
            x=True
        return x
    
    def push(self, x):
        # Insert x at the top of the stack
        if self.isFull():
            return 
        self.top+=1
        self.st[self.top]=x
    
    def pop(self):
        # Removes an element from the top of the stack
        if self.isEmpty():
            return 
        x=self.st[self.top]
        self.top-=1
        return x
        

    
    def peek(self):
        # Returns the top element of the stack
        if self.top==-1:
            return -1
        return self.st[self.top]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna