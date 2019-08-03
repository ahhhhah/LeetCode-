class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data_stack = []
        self.mini_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data_stack.append(x)
        if len(self.mini_stack)==0 or x <= self.mini_stack[-1]:
            self.mini_stack.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.mini_stack[-1] == self.data_stack[-1]:
            self.mini_stack.pop()
        self.data_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.data_stack[-1]        

    def getMin(self):
        """
        :rtype: int
        """
        return self.mini_stack[-1]