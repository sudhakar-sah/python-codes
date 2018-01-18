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
        
        
class OrderedList:
    
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        
        temp = Node(item)
        print "item:", item
        if(self.head == None):
            self.head= temp
            return 
            
        while current != None and not stop:
            if(current.getData() > item):
                print "stop iteration"
                stop = True
            else:
                previous = current 
                current = current.getNext()
        
        
        
        if(previous == None):
            temp.setNext(self.head)
            self.head = temp 
        else:
            temp.setNext(current)
            previous.setNext(temp)
            
        return   
            
                

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
        print current
        output = "head" + "->"
        while current != None:
            print current.getData()
            output = output + str(current.getData()) + "->"
            current = current.getNext()
        output = output + "None"
        print output
        
    def remove(self, rem_data):
        current = self.head
        found = False
        previous = None
        
        if(current == None): # empty list 
            return
        
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
            
l1 = OrderedList()
l1.add(10)
# l1.display()
l1.add(5)
# l1.display()
l1.add(20)
l1.add(3)
l1.add(50)
l1.add(23)

l1.display()
l1.remove(20)
l1.display()

print l1.size()