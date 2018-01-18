# from pythonds.basic.stack import Stack
# this is where stack is implemented but we have implmented our code here for practice 


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
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

class Stack_bottom:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.insert(0,item)

	def pop():
		self.items.pop(0)

	def peek(self):
		return self.items[0]

	def size(self):
		return len(self.items)


s = Stack()
s = Stack()
s.push('a')
s.push(1)
s.push(True)

s.display()
print s.size()
s.pop()
s.display()
print s.size()


# # # # 
# string revision 
# # # # 

def revstring(mystring):
    s = Stack()
    for ch in mystring:
        s.push(ch)

    revstr = '' 
    while not s.isEmpty():
        revstr = revstr+ s.pop()
    
    return revstr
    
revstring = revstring("sudhakar")
print revstring



# # # # 
# checking balanced paranthesis using stack 
# # # # 

def parChecker(symbolString):
    
    s = Stack()
    balanced = True 
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if(symbol == "("):
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index = index + 1
        
    if(balanced and s.isEmpty()):
        return True
    else:
        return False 
    
print parChecker('(((()))))')



# # # # 
# for combination of paranthesis 
# # # # 

def checkPar(top , symbol):    
    opens = '([{'
    closes = ')]}'
    return opens.index(top) == closes.index(symbol)
    

def parCheckerComplex(symbolString):
    
    s = Stack()
    balanced = True 
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
#                 print "here1"
                top = s.pop()
                
                if(checkPar(top, symbol)):
                    balanced = True 
                else:
                    balanced = False
                
        index = index + 1
        
    if(balanced and s.isEmpty()):
        return True
    else:
        return False 
    
print parCheckerComplex('{{({[][])}}}')
    


# # # # 
# convert a decimal number to binary
# # # # 
def decimalToBinaryConversion(decNum):

    s = Stack()
    binaryStr = "" 

    while decNum > 0:
        rem = decNum %2 
        decNum = decNum/2
        s.push(rem) 
        
    while not s.isEmpty():
        binaryStr = binaryStr + str(s.pop())
    return int(binaryStr) 
        
print decimalToBinaryConversion(55)
    

# # # # 
# convert a decimal number of any base number (8, 16 etc...)
# # # # 
def numberConversion(decNum, base):
    digits = "0123456789ABCDEF"
    s = Stack()
    binaryStr = "" 

    while decNum > 0:
        rem = decNum %base
        print rem
        rem= digits[rem]
        print rem
        decNum = decNum/base
        s.push(rem) 
        
    while not s.isEmpty():
        binaryStr = binaryStr + str(s.pop())
    return (binaryStr) 
        
print numberConversion(26, 26)



#
# Postfix expression from infix  
# 
# 

def isOperator(string):
    if string in "*+/-()":
        
        return True 
    else:
        return False 

def precedence(curr, inStack):   
    prec_list = '+-*/'
    print curr, inStack
#     return true if the current operator precedence is less than in the stack
    if prec_list.index(curr) < prec_list.index(inStack):
        print "prec True"
        return True 
    else:
        print "prec False"
        return False
    
    
def inFixToPostFix(Expr):
    
    opStack = Stack()
    exprList = Expr.split()  
    eSize = len(exprList)
    outExpr = []
    index = 0
    while index < eSize:
        curr = exprList[index]
        print "this is ", curr
        if isOperator(curr):
            print "this is operator ", curr
           
#             check if it is paranthesis 
#             if(curr in '('):
#                 operandStack.push(curr)
            if(opStack.isEmpty()):
                print "adding to the empty stack", curr
                opStack.push(curr)
            else:
                print "it is not an empty list"
                print "checking the precedence ", curr
                
                
                while(precedence(curr, opStack.peek())):
                    print curr + " is less precedence than " + opStack.peek()                    
                    outExpr.append(opStack.pop())
                    if(opStack.isEmpty()):
                        break;
                    print "ourExpr is :", outExpr
                opStack.push(curr)
                print curr, " is added to output"
        else: # operands         
            outExpr.append(curr)
                
        index = index + 1 
    print "print stack"
    opStack.display()    

    while not opStack.isEmpty():
        outExpr.append(opStack.pop())
    return outExpr
#     opStack.display()
    

outExpr = inFixToPostFix('A * B + C * D')



