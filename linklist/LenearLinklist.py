""" This is link list that starts and trace to the end of the link list A->B->c and so on 
    we cannot traverse back in this link list .
    Each Node store the address location of the next node"""

## -----------Start--------------
## Author: - Abhishek Hazra
## ------------------------------

## Create a class that represents a node in the link list and give it all the necessary attributes 

class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None
        self.node_index = -1

# Implementing the linklist logic 

class LinkList:         ## this implementaiton can be a stack , but insert at pos is implemented
    def __init__(self):
        self.fstnode = None
        self.lastnode = None
        self.__len = 0
        self.node_number = 0
    def add(self,val):
        if not self.fstnode:
            newnode = Node(val)
            self.fstnode = newnode
            self.lastnode = newnode
            self.__len +=1
        else:
            newnode =  Node(val)
            self.lastnode.next = newnode
            self.lastnode = newnode
            self.__len +=1
    def pop(self):
        self.__len -= 1
        temp = self.fstnode.value
        self.fstnode = self.fstnode.next
        return temp
    
    def insert(self,val,position):
        if position <= self.__len and position > 0:
            pos_obj = self.fstnode
            for i in range(2,position):
                pos_obj = pos_obj.next
            newnode =  Node(val)
            temp = pos_obj.next
            pos_obj.next = newnode
            newnode.next = temp
        else:
            raise ValueError("postion cannot be zero or greater than the length of the list --> {}".format(self.__len))



    def __len__(self):
        return self.__len
    def __repr__(self):
        cur_node = self.fstnode
        path = str(cur_node.value)
        while cur_node.next:
            cur_node =  cur_node.next
            path = path + '->' + str(cur_node.value)
            # cur_node =  cur_node.next
        return path
            



# Driver code

mylist =  LinkList()
mylist.add(1)
mylist.add(5)
mylist.add(4)
mylist.add(3)
mylist.add(3)

print(len(mylist))
print(mylist)

print(mylist.pop())
print(len(mylist))
print(mylist)

mylist.insert(100,0)
print(mylist)


            








