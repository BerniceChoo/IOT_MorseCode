#This class is to implement a Node or Tree
class Node:
  def __init__(self, char, left=None, right=None):
    self.char = char
    self.left = left
    self.right = right
    
#Convert Character by finding the character using a pre-order traversal of the Binary Tree
def getMorseCode(node, character, code):
  if node==None:
    return False
  elif node.char==character:
    return True
  else:  
    if getMorseCode(node.left,character,code)==True:
      code.insert(0,".")
      return True
    elif getMorseCode(node.right,character,code)==True:
      code.insert(0,"-")
      return True
      
#initialise the binary tree with the root node
tree = Node("START")

# 1st Level of the binary tree
tree.left = Node("E")
tree.right = Node("T")

# 2nd Level of the binary tree
tree.left.left = Node("I")
tree.left.right = Node("A")
tree.right.left = Node("N")
tree.right.right = Node("M")

# 3rd Level of the binary tree
tree.left.left.left = Node("S")
tree.left.left.right = Node("U")
tree.left.right.left = Node("R")
tree.left.right.right = Node("W")

tree.right.left.left = Node("D")
tree.right.left.right = Node("K")
tree.right.right.left = Node("G")
tree.right.right.right = Node("O")

# 4th Level of the binary tree
tree.left.left.left.left = Node("H")
tree.left.left.left.right = Node("V")
tree.left.left.right.left = Node("F")
tree.left.left.right.right = Node("")
tree.left.right.left.left = Node("L")
tree.left.right.left.right = Node("")
tree.left.right.right.left = Node("P")
tree.left.right.right.right = Node("J")

tree.right.left.left.left = Node("B")
tree.right.left.left.right = Node("X")
tree.right.left.right.left = Node("C")
tree.right.left.right.right = Node("Y")
tree.right.right.left.left = Node("Z")
tree.right.right.left.right = Node("Q")
tree.right.right.right.left = Node("")
tree.right.right.right.right = Node("")

#Print the input message
message = input("Enter the message to be converted into Morse Code: (e.g. IOT)").upper()
morseCode = ""

#Convert the message with one character at a time
for character in message:
  dotsdashes = []
  getMorseCode(tree,character,dotsdashes)
  code = "".join(dotsdashes)
  morseCode = morseCode + code + " "
  
print(morseCode)