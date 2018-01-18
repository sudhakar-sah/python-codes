import numpy as np 

def anagramSolution(s1, s2):
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
print anagramSolution("star", "rats")