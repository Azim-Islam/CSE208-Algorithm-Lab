class stack:
    def __init__(self):
        self.stack = list()

    def is_empty(self):
        """
            Returns true if the stack is empty.
        """
        if len(self.stack) == 0:
            return True
        else:
            return False
    
    def pop(self):
        """
            Pop the last data out of the stack.
        """
        return self.stack.pop()
    
    def push(self, data:any):
        """
            Push any kind of data into the stack.
        """
        self.stack.append(data)
    
    def top(self):
        """
            Returns the last item in the stack
        """
        return self.stack[-1]
    