""" A double ended linklist is a linklist that has information both of its previus and next objects
    A <--> B <--> c <--> D
    Its mostly used in creating double ended queue"""

## -------------------------
## Author : - Abhishek Hazra
## -------------------------

## A class that can represents a node in the link list and give it all the necessary attributes

class Node(object):     # All Classes in python3+ bydefault inherites from object class
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

# Implementing the double ended queue class using a double ended linked list

class Deque:
    def __init__(self):
        self.fstnode = None
        self.lastnode = None
        self.__len = 0
    def appendleft(self,value):
        if self.fstnode is not None:
            newnode =  Node(value)
            self.fstnode.prev = newnode
            newnode.next = self.fstnode
            self.fstnode = newnode
            self.__len +=1
        else:
            newnode = Node(value)
            self.fstnode = newnode
            self.lastnode = self.fstnode
            self.__len +=1

    def append(self,value):
        if self.lastnode:
            newnode = Node(value)
            self.lastnode.next = newnode
            newnode.prev =  self.lastnode
            self.lastnode = newnode
            self.__len +=1
        else:
            newnode = Node(value)
            self.lastnode = newnode
            self.fstnode = self.lastnode
            self.__len += 1             

    def popleft(self):
        if self.fstnode:
            val = self.fstnode.value
            self.fstnode = self.fstnode.next
            if self.fstnode:
                self.fstnode.prev = None
        else:
            raise ValueError('Empty object')
        self.__len -=1
        return val
    
    def popright(self):
        if self.lastnode:
            val = self.lastnode.value
            self.lastnode =  self.lastnode.prev
            if self.lastnode:
                self.lastnode.next =  None

        else:
            raise ValueError('empty queue')
        self.__len -=1
        return val
    
    def reverse(self):
        pass
    
    def __len__(self):
        return self.__len
    
    def __repr__(self):
        curr_node = self.fstnode
        path = str(curr_node.value)
        while curr_node.next:
            curr_node = curr_node.next
            path =path + ' <--> ' + str(curr_node.value)
        return path
        

# Driver code

o = Deque()
o.appendleft("fist")
o.appendleft("second")
print(o)
o.appendleft("3rd")
o.appendleft("forth")
o.appendleft("fifth")
o.appendleft('sixth')
o.append(123)
print(o)
print(o.popleft())
print(o.popleft())
print(o)
print(len(o))
