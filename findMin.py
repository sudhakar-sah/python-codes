import time 
from random import randrange
list1 = [23,4,89,4,56,1,2,13,46]


def findMin(alist):
    min = 0xffffff
    for i in range(len(alist)):
        for j in (range(i+1, len(alist))):
            if(alist[j] < min ):
                min = alist[i]
    return min

def findMin_n(alist):
    alist.sort()
    return alist[0]

for listSize in range(1000,10001,1000):
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print (findMin(alist))    
    end = time.time()
    print "elapsedTime (Complexity O(n2):",(end-start)

    start = time.time()
    print (findMin_n(alist))    
    end = time.time()
    print "elapsedTime (Complexity Olog(n)):",(end-start)

    
# print findMin(list1)
# print findMin_n(list1)


