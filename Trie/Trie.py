""" A special type of tree based data structure which is very efficient in storing and retriving words
and letters . it takes a word breaks into letters in it and stores in a chain where the 
starting of words letter is stored once and then the subsiquent is branched 

EX: "This is a trie tree"
                |--> T |--> h --> i--> s --> end_of_words = True
                |      |--> r|--> i --> e--> end_of_words = True
            R   |            |--> e--> e-->  end_of_words = True
            O   |
            O   |--> i --> s --> end_of_words = True
            T   |
                |--> a --> end_of_words = True

    we can create a trie node that represent a node contenting the letter,end of word  ,repet count
    etc as per the demand of the situation.
    EVERY TRIE STARTS FORMA ROOT NODE WHICH HAS NO VALUE"""

#-----------------------
#Author : Abhishek Hazra
#-----------------------
##========================
# time diff call generator
##========================
def timeit(f):
    diff = ''
    from datetime import datetime
    def inner(self,fun):
        d = datetime.now()
        val = f(self,fun)
        diff = datetime.now()-d
        return val,diff
    return inner

#-----------start--------------
#class representing a trie node

class PrefixError(Exception):
    pass

class Node(object):
    def __init__(self,value = None):
        self.char = value
        self.children = {}
        self.is_end_of_word = False
        self.occurance = 0
        self.word = ''

class Trie(object):
    def __init__(self):
        self.root =  Node()
    # @timeit
    def add_to_trie(self,word):
        curr_node = self.root
        for letter in word.lower():
            if curr_node.children.get(letter):
                curr_node = curr_node.children.get(letter)
            else:
                newnode =  Node(letter)
                newnode.word = curr_node.word + newnode.char
                curr_node.children[letter] = newnode
                curr_node = curr_node.children[letter]
        curr_node.is_end_of_word = True
        curr_node.occurance += 1
    @timeit
    def match_prefix(self,prefix):
        curr_node = self.root
        word_list = []
        for letter in prefix:
            if curr_node.children.get(letter) is None:
                return []
            curr_node = curr_node.children[letter]
        stack = []
        stack.append(curr_node)
        while len(stack):
            n = stack.pop()
            if n.is_end_of_word:
                word_list.append(n.word)
            for nodes in n.children.values():
                stack.append(nodes)
        print(len(word_list))
        return word_list
    
## Driver code:
if __name__ == "__main__":
    t = Trie()
    d = """ "In publishing and graphic design, lorem ipsum is a "
"filler text commonly used to demonstrate the graphic elements of a "
"document or visual presentation. Replacing meaningful content that "
"could be distracting with placeholder text may allow viewers to focus "
"on graphic aspects such as font, typography, and page layout. It also "
"reduces the need for the designer to come up with meaningful text, as "
"they can instead use hastily generated lorem ipsum text. The lorem "
"ipsum text is typically a scrambled section of De finibus bonorum et "
"malorum, a 1st-century BC Latin text by Cicero, with words altered, "
"added, and removed to make it nonsensical, improper Latin. A variation "
"of the ordinary lorem ipsum text has been used in typesetting since "
"the 1960s or earlier, when it was popularized by advertisements for "
"Letraset transfer sheets. It was introduced to the Information Age in "
"the mid-1980s by Aldus Corporation, which employed it in graphics and "
"word processing templates for its desktop publishing program, "
"PageMaker, for the Apple Macintosh. A common form of lorem ipsum "
"reads: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do "
"eiusmod tempor incididunt ut labore et dolore magna aliqua. ut enim ad "
"minim veniam, quis nostrud exercitation ullamco laboris nisi ut "
"aliquip ex ea caumodo consequat. Duis aute irure dolor in "
"reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
"pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
"culpa qui officia deserunt mollit anim id est laborum."""

    for i in d.split():
        t.add_to_trie(i.lower())

    # with open('/home/abhishek/Downloads/big.txt','r') as fd:
    #     for i in fd:
    #         for j in i.split():
    #             t.add_to_trie(j)

    print(t.match_prefix('a'))
    breakpoint()

    






