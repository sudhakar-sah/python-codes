import numpy as np 

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
    
class Tree:
    def __init__(self):
        self.root = None
    
    def getRoot(self):
        return self.root
    
    def add(self, val):
        if(self.root is None):
            self.root = Node(val)
        else:
            self._add(val, self.root)
    
    def _add(self, val, node):
        if(val < node.v):
            if(node.l is not None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r is not None):
                self._add(val, node.r)
            else:
                node.r = Node(val)
    
    def find(self, val):
        if(self.root is not None):
            
            return self._find(val, self.root)
        else:
            return None
    
    def _find(self, val, node):
        if(val == node.v):
            print "found"
            return node
        elif (val < node.v and node.l is not None):
            print "left node :", node.v
            self._find(val, node.l)
        elif (val > node.v and node.r is not None):
            print "right node: " , node.v
            self._find(val,node.r)
    
    def deleteTree(self):
        # garbage collector will do this for us 
        self.root = None

    def pre_order_traversal(self):
        if(self.root is not None):
            self._pre_order_traversal(self.root)
        else:
            print "empty tree"
        
    def _pre_order_traversal(self, node):
        if(node.l is None and node.r is None):
            print "leaf_node"
        print str(node.v) + ' '
        
        if(node.l is not None):
            self._pre_order_traversal(node.l)
        if(node.r is not None):
            self._pre_order_traversal(node.r)

    def post_order_traversal(self):
        if(self.root is not None):
            self._post_order_traversal(self.root)
        else:
            print "empty tree"

    def _post_order_traversal(self, node):        
        if(node.l is not None):
            self._post_order_traversal(node.l)
        if(node.r is not None):
            self._post_order_traversal(node.r)
        print str(node.v) + ' '
        
    def in_order_traversal(self):
        if(self.root is not None):
            self._in_order_traversal(self.root)
        else:
            print "empty tree"

    def _in_order_traversal(self, node):       
        if(node.l is not None):
            self._in_order_traversal(node.l)
        print str(node.v) + ' '
        if(node.r is not None):
            self._in_order_traversal(node.r)
        
            
    def printTree(self):
        if(self.root is not None):
            self._printTree(self.root)
    
    def _printTree(self, node):
        if(node is not None):
            self._printTree(node.l)
            print str(node.v) + ' '
            self._printTree(node.r)
        
            
            
           