import numpy as np 

def anagramSolution_fastest(s1, s2):
#     s1 = list(s1)
#     s2 = list(s2)
    pos1 = np.zeros((26,1))
    pos2 = np.zeros((26,1)) 
    
    for i in range(len(s1)):
        pos1[ord(s1[i])-ord('a')] +=1 # O(n)
        
    for i in range(len(s2)):
        pos2[ord(s2[i])-ord('a')] +=1 # O(n)
    
#     print pos1, pos2
    
    return np.sum((pos1 - pos2)) # (O(26))

# Total O(n) + O(n) + O(26) ~ O(n)
print anagramSolution_fastest("star", "rats")


def anagramSolution_sorting(s1, s2):

    s1 = list(s1)
    s2 = list(s2)
    # sort both arrays 
    s1.sort()
    s2.sort()
    

#     create unique set     
    alist1 = set(s1)
    alist2 = set(s2)

#     print alist1
#     print alist2
#     list1_size = len(alist1)
    list2_size = len(alist2)
    

    
#     print list1_size
#     print list2_size 
    
    alist1 = list(alist1)
    alist2 = list(alist2)
    
    stillOK = True 
    if(len(alist1) != len(alist2)):
        return False
    else:
        i =0
#         print i, stillOK
#         print list1_size
        while i < list1_size and stillOK is True:
            print alist1[i], alist2[i]
            
            if (alist1[i] != alist2[i]):
                stillOK = False
                break
            i+=1 
    
    return stillOK



            
anagramSolution_sorting("star", "ratsi")        
