
from graphics import *
from stack import Stack

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

# def formula(x):
#     y = x*x/(x-1) # 'put your formula here'
#     return

def InfixToPostfix(infix):
    s = Stack()
    postfix = []
    for token in infix:
        if token in "0123456789x":
            postfix.append(token)
        if token in "*/":
            if not s.isEmpty() and s.peek() in "*/":
                postfix.append(s.pop())
            s.push(token)
        if token in "+-":
            while not s.isEmpty() and s.peek() in "+-":
                postfix.append(s.pop())
            s.push(token)
        if token == '(':
            s.push(token)   
        if token == ')':
            while s.peek() != '(':
                postfix.append(s.pop())
            s.pop()
    while not s.isEmpty(): postfix.append(s.pop())
    return postfix
    
def EvaluatePostfix(postfix, x):
    s = Stack()
    for token in postfix:
        if token.isdigit(): s.push(float(token))
        if token=='x': s.push(float(x))
        if token == "+":
            op2 = s.pop()
            op1 = s.pop()
            s.push(op1 + op2)
        if token == "-":
            op2 = s.pop()
            op1 = s.pop()
            s.push(op1 - op2)
        if token == "*":
            op2 = s.pop()
            op1 = s.pop()
            s.push(op1 * op2)
        if token == "/":
            op2 = s.pop()
            op1 = s.pop()
            s.push(op1 / op2)
    return s.pop()

def printInstructions():
    print("This is how it works...")
    
def main():
    printInstructions()
    win = GraphWin("My Circle", 500, 500)
    infix = input("Enter your expression (e.g., x*(x+1)/(x-2), no spaces: ")
    postfix = InfixToPostfix(infix)
    print(f"Postfix: {postfix}")
    
    xlow, ylow = -10, -10
    xhigh, yhigh = 10, 10
    step = .1
    
    win.setCoords(xlow,ylow,xhigh,yhigh)
    x = xlow
    
    while x < xhigh:
        y = EvaluatePostfix(postfix, x)
        p1 = Point(x,y)
        x2 = (x + step)
        y2 = EvaluatePostfix(postfix, x2)
        p2 = Point(x2,y2)
        l = Line(p1, p2) 
        l.draw(win)
        x+=step
        
    win.getMouse()
    win.close()    

A = "x*(x+1)/(x-2)"
B = 'x*x*x/(2*5)'
C = '(x+1)*(x-1)'
D = 'x*x - x + 3'

print(InfixToPostfix(A))
print(InfixToPostfix(B))
print(InfixToPostfix(C))
print(InfixToPostfix(D))

main()


