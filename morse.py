#This class is to implement a Node
class Node:
    def __init__(self, char):
        self.char = char
        self.dot = None
        self.dash = None

def getMorseCode(node, character, code):
  if node==None:
    return False
  elif node.char==character:
    return True
  else:  
    if getMorseCode(node.dot,character,code)==True:
      code.insert(0,".")
      return True
    elif getMorseCode(node.dash,character,code)==True:
      code.insert(0,"-")
      return True
  
#initialise the binary tree with the root node
root = Node("START")

# 1st Level of the binary tree
root.dot = Node('E')
root.dash = Node('T')

# 2nd Level of the binary tree
root.dot.dot = Node('I')
root.dot.dash = Node('A')
root.dash.dot = Node('N')
root.dash.dash =Node('M')

# 3rd Level of the binary tree
root.dot.dot.dot = Node('S')
root.dot.dot.dash = Node('U')
root.dot.dash.dot = Node('R')
root.dot.dash.dash = Node('W')
root.dash.dot.dot = Node('D')
root.dash.dot.dash = Node('K')
root.dash.dash.dot = Node('G')
root.dash.dash.dash = Node('O')

# 4th Level of the binary tree
root.dot.dot.dot.dot = Node('H')
root.dot.dot.dot.dash = Node('V')
root.dot.dot.dot.dash = Node("NULL")
root.dot.dot.dash.dot = Node('F')
root.dot.dot.dash.dash = Node("NULL")
root.dot.dash.dot.dot = Node('L')
root.dot.dash.dot.dash = Node('NULL')
root.dot.dash.dash.dot = Node('P')
root.dot.dash.dash.dash = Node('J')
root.dash.dot.dot.dot = Node('B')
root.dash.dot.dot.dash = Node('X')
root.dash.dot.dash.dot = Node('C')
root.dash.dot.dash.dash = Node('Y')
root.dash.dash.dot.dot = Node('Z')
root.dash.dash.dot.dash = Node('Q')
root.dash.dash.dash.dot = Node("NULL")
root.dash.dash.dash.dash = Node("NULL")

# 5th Level of the the binary tree
root.dot.dot.dot.dot.dot = Node('5')
root.dot.dot.dot.dot.dash = Node('4')
root.dot.dot.dot.dash.dot = Node('NULL')
root.dot.dot.dot.dash.dash = Node('3')
root.dot.dot.dash.dot.dot = Node('¿')
root.dot.dot.dash.dash.dot = Node('?')
root.dot.dot.dash.dash.dash = Node('2')
root.dot.dash.dot.dot.dot = Node('&')
root.dot.dash.dot.dot.dash = Node('NULL')
root.dot.dash.dot.dash.dot = Node('+')
root.dot.dash.dot.dash.dash = Node ('NULL')
root.dot.dash.dash.dash.dash = Node('1')
root.dash.dot.dot.dot.dot = Node('6')
root.dash.dot.dot.dot.dash = Node('=')
root.dash.dot.dot.dash.dot = Node('/')
root.dash.dot.dash.dot.dash = Node('NULL')
root.dash.dot.dash.dash.dot = Node('(')
root.dash.dash.dot.dot.dot = Node('7')
root.dash.dash.dot.dot.dash = Node('NULL')
root.dash.dash.dash.dot.dot = Node('8')
root.dash.dash.dash.dash.dot = Node('9')
root.dash.dash.dash.dash.dash = Node('0')

# 6th Level of the binary tree
# most of the puntuations and symbols (worksheet2 task 4) are in this level
root.dot.dot.dash.dash.dot.dash = Node('_')
root.dot.dot.dot.dash.dot.dot = Node('NULL')
root.dot.dash.dot.dot.dash.dot = Node('"')
root.dot.dash.dot.dash.dot.dash = Node('.')
root.dot.dash.dash.dash.dash.dash = Node('-')
root.dot.dash.dash.dash.dash.dot = Node("'")
root.dash.dot.dash.dot.dash.dot = Node(';')
root.dash.dot.dash.dot.dash.dash = Node('!')
root.dash.dot.dash.dash.dot.dash = Node(')')
root.dash.dash.dot.dot.dash.dash= Node(',')
root.dash.dash.dash.dot.dot.dot = Node(':')

# 7th Level of the binary tree
root.dot.dot.dot.dash.dot.dot.dash = Node('$')
root.dot.dot.dash.dash.dot.dash = Node('_')

encode = "FOON "

#Convert the message to morse with one character at a time
for character in encode:
  dotsanddashes = []
  getMorseCode(root,character,dotsanddashes)
  code = "".join(dotsanddashes)
  encode = encode + code + " "

print("\nBelow are encode of ")
print(encode)

#decode from morse's to messages
def decode(tree, morse):
    current = tree
    
    for symbol in morse:
        if(symbol =='.'):
            current = current.dot

        elif(symbol == '-'):
            current = current.dash

    return current.char

def morsestring(root, morsestring):
    returnstring = ""
    morsestring = morsestring.split()
    
    for c in morsestring:
        returnstring = returnstring + decode(root, c)
    return returnstring

def find(self, data):
    if self.data:
        if data == self.data:
            return True
        if data > self.data:
            if self.left:
                return self.left.find(data)
        elif data > self.data:
            if self.right:
                return self.right.find(data)
        print("Error: invalid input")
    return False

def outputdecode(self):
    if self.left:
        self.left.output()
    print (self.data)
    if self.right:
        self.right.output()    

print("\nBelow are decode of ..-. -.--")
outputdecode = morsestring(root, "..-. -.--") 
print (outputdecode)
print("\n")


#codes for testing in worksheet 2 task 3
def isEmpty(root):
    if root:
        return False
    else:
        if root.dot or root.dash:
            return False

        if root.dot != None or root.dash != None:
            return (isEmpty(root.dot) and isEmpty(root.dash))

        return True

def preorderInsert(root, input):
    if root.dot == None:
        root.dot = Node(input)
        return True
    elif root.dash == None:
        root.dash = Node(input)
        return True
    else:
        if preorderInsert(root.dot, input) == True:
            return True
        if preorderInsert(root.dash, input) == True:
            return True
    return False

def deletePreorder(root, char):
    if root == None:
        return False
    elif root.char == char:
        root.char == None
        print(char, "has been deleted from the tree")
        return True
    else:
        if deletePreorder(root.dot, char) == True:
            return True
        elif deletePreorder(root.dash, char) == True:
            return True
    return False

def preorderSearch(root, char):
    if root == None:
        return False
    elif root.char == char:
        print(char, "has been found")
        return True
    else:
        if preorderSearch(root.dot, char) == True:
            return True
        elif preorderSearch(root.dash, char) == True:
            return True
    return False


# Functions for testing in worksheet 2 Task 3
def checkIsEmpty():
    return isEmpty(root)

def checkIsNotEmpty():
    return not isEmpty(root)

def insert(input):
    input.upper()
    if find(input) == True:
        return False
    else:
        return preorderInsert(root, input)
    
def delete(input):
    return deletePreorder(root, input)

def find(input):
    input.upper()
    return preorderSearch(root, input)