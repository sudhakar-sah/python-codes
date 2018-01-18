from timeit import Timer
_SIZE = 1000
def test1():
    l = []
    for i in range(_SIZE):
        l = l + [i]

def test2():
    l = []
    for i in range(_SIZE):
        l.append(i)
        
def test3():
    l = []
    l = [i for i in range(_SIZE)]

def test4():
    l = list(range(_SIZE))
    
# test timing 

t1= Timer("test1()", "from __main__ import test1")
print ("concat ", t1.timeit(number=1000), "milliseconds")

t2 = Timer("test2()", "from __main__ import test2")
print ("concat ", t2.timeit(number=1000), "milliseconds")

t3 = Timer("test3()", "from __main__ import test3")
print ("concat ", t3.timeit(number=1000), "milliseconds")

t4 = Timer("test4()", "from __main__ import test4")
print ("concat ", t4.timeit(number=1000), "milliseconds")


"""
Operation	Big-O Efficiency
index []	O(1)
index assignment	O(1)
append	O(1)
pop()	O(1)
pop(i)	O(n)
insert(i,item)	O(n)
del operator	O(n)
iteration	O(n)
contains (in)	O(n)
get slice [x:y]	O(k)
del slice	O(n)
set slice	O(n+k)
reverse	O(n)
concatenate	O(k)
sort	O(n log n)
multiply	O(nk)


"""