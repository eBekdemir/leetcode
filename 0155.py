# URL: https://leetcode.com/problems/min-stack/                        
# TITLE: Min Stack                            
# DIFFICULTY: Medium                                
# ------------------------------------------------------
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val):
        self.stack.append(val)
        if self.mins:
            self.mins.append(min(val, self.mins[-1]))
        else: self.mins.append(val)

    def pop(self):
        self.stack.pop()
        self.mins.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
