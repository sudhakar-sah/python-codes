class Dequeue:

	def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)



#
#
# Function to check Palindrome
# 
# 

def Palindrome(word):
    dq = Dequeue()

    for ch in word:
        dq.addRear(ch)

    stillOK = True

    while dq.size() > 1 and stillOK:

        front = dq.removeFront()
        rear = dq.removeRear()


        if front != rear:
            stillOK = False 

    return stillOK 

print(Palindrome("lsdkjfskf"))
print(Palindrome("jahaj"))


