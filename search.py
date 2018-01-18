def sequentialSearch(alist, item):
    found = False
    i = 0
    while i < len(alist) and not found:
        if(i == item):
            found = True
        i +=1
        
    return found
    
print sequentialSearch([1,2,3,4,5,6,7], 12)


def sequentialSearch_ordered(alist, item):
    found = False
    i = 0
    while i < len(alist) and not found :
        if(alist[i] == item):
            found = True
        i +=1
   
    return found
    
print sequentialSearch_ordered([1,2,3,5,6,7], 12)



def binarySearch(alist, item):
    list_size = len(alist)
    
    
    first = 0 
    last = list_size 
    
    found = False 
    
    if(item > alist[len(alist)-1] or item < alist[0]):
        return False
    while last > first and not found:
        pivot = (first + last)/2 
        if(item == alist[pivot]):
            found = True 
        else:
            if(item < alist[pivot]):
                last = pivot
            else:
                first = pivot
            

    
    return found

print binarySearch([1,2,3,4,5,6,7,8,9,10,11,12,13], 15)


        