""" Hash map are the key value pairs where the keys are hash values of a immutable datatype that is translated to a index number 
    of a predefined dynamic array or a linked list that actualy stores the value.
    its fast as the seaarch doesnot have to itterate through the list or array cus the index is calculated 
    for every key which is constant .In cases of colliison of indexex the key values are stored in the same index number 
    as a tuple or a array inside the array and iterated over to match the key """ 

# to implement we need to define a hash map class and instantiate a list inside it that eill hold the values.

class HashMap:
    def __init__(self,memsize = 16):
        self.bucket =[]
        for i in range(memsize):
            self.bucket.append(list())
        self.__len = 0
        self.keys = []
        self.values = []
    def get(self,key):
        hash_value =  hash(key)
        index =  hash_value % len(self.bucket)
        for ls in self.bucket[index]:
            if ls[0] == key:
                return ls[1]
        return None
    def put(self,key,value):
        hash_value = hash(key)
        index = hash_value % len(self.bucket)
        self.keys.append(key)
        self.values.append(value)
        if len(self.bucket[index]) == 0:
            self.bucket[index].append([key,value])
            self.__len += 1
        else:    
            for ls in self.bucket[index]:
                if key == ls[0]:
                    ls[1] = value
                    return
            self.bucket[index].append([key,value])
            self.__len += 1
            return
            

    def pop(self,key):
        index = hash(key) % len(self.bucket)
        for ls in self.bucket[index]:
            if ls[0] == key:
                v = ls[1]
                self.bucket[index].remove(ls)
                self.__len -=1
                return v
        raise KeyError (key)

        
    def __len__(self):
        return self.__len
    def __repr__(self):
        fs = []
        for i in self.bucket:
            s = []
            if len(i):
                for key,value in i:
                    s.append(str(key) + ':' + str(value))
                fs.append(' , '.join(s))
        return "{ " + ' , '.join(fs) + " }"

#Driver code
o = HashMap()
o.put('fa',"dada")
o.put('ffa',"dada")
o.put('a',"dada")
o.put(1,34)
o.put(1,3)
o.put(1,3)
o.put(1,77676)
o.put(3232,330303)
o.put("key","value")
print(o.pop(1))
print(len(o))
print(o)