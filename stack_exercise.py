class Stack:
    def init(self):
        self.my_stack = []

    def push(self, item):
        if len(self.my_stack) < self.length:
            self.my_stack.append(item)
        else:
            raise Exception("Stack Overflow!")

    def pop(self):
        self.my_stack.pop()

    def size(self, size=0):
        self.length = size

