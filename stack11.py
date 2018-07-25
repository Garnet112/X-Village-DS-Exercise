from stack import Stack
s = Stack()

class stack:
    def __init__(self):
        n = input("Numbers:")
        self.n = int(n)
    
    def dec_to_bin(self):
        while self.n >= 0:
            if self.n // 2 != 0 and self.n % 2 == 1:
                s.push(1)
                #print(1)
                self.n = self.n // 2
            if self.n // 2 != 0 and self.n % 2 == 0:
                s.push(0)
                #print(0)
                self.n = self.n // 2
            if self.n // 2 == 0 and self.n % 2 == 1:
                s.push(1)
                #print(1)
                break
            if self.n // 2 == 0 and self.n % 2 == 0:
                s.push(0)
                #print(0)
                break
        return self.n

stack = stack()
#stack.__init__()
stack.dec_to_bin()
#rint(s.items)

b = []
for i in range(len(s.items)):
    b.append(s.pop())

print(b)














