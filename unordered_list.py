class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data 

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext 
    
    def display(self):
        print "data:", self.data
        print "next:", self.next
        
        
class UnorderedList:
    
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    def size(self):
        
        current = self.head
        count = 0 
        while current != None:
            count +=1 
            current = current.getNext()
        
        return count 
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if(current.getData() == item):
                found = True
            else:
                current = current.getNext()
        
        return found 
    
    def display(self):
        current = self.head
        output = "head" + "->"
        while current != None:
            output = output + str(current.getData()) + "->"
            current = current.getNext()
        output = output + "None"
        print output
        
    def remove(self, rem_data):
        current = self.head
        found = False
        previous = None
        while current != None and not found:
             
            if(current.getData() == rem_data):
                found = True
            else:
                previous = current
                current = current.getNext()
        # if it is the first one 
        if(previous == None):
            self.head = current.getNext()
        else: # other nodes 
            previous.setNext(current.getNext())
            
            
mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print mylist.search(94)

mylist.display()

print mylist.size()

mylist.remove(26)

mylist.display()