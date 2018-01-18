def bubbleSort(alist):
    
    
    for i in range(len(alist)):
        exchanges = False 
        if(exchanges):
            break
        last = len(alist)-i
        for j in range(0, last-1, 1):
            if(alist[j] > alist[j+1]):
                alist[j], alist[j+1] = alist[j+1], alist[j]
                exchanges = True
    
    return alist

bubbleSort([45,23,67,89,12,1,34,56])


def selectionSort(alist):
    

    for i in range(len(alist)-1):
        last = len(alist)-i-1
        max_val = -0xfffff
        max_loc = -1
        for j in range(0,last, 1):
            if(alist[j] >= max_val):
                max_val = alist[j]
                max_loc = j
        
        if(max_loc <= last):        
            alist[last], alist[max_loc] = alist[max_loc], alist[last]
   
    return alist
print selectionSort([45,23,67,89,12,1,34,56,34])