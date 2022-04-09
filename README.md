# iotworksheet2
## Part 1

#### Task 1

I have use SSH to redirect the port (10105) to my local system in order to connect to the server via a browser running on my local machine: in my case, google chrome. SSH port forwarding is a feature of SSH that allows me to tunnel application ports from the server to the client or vice versa. This can be done straight from the command line using the ssh command, but it's far easier to do it from VS code.

After clicking on it, it will direct me to the webserver where I am able to enter text to encode and vice versa. There I will get the result of the morse code. An example is shown below, where after encoding ‘fy’, it will become  ‘..-. -.--’ in port 10105.

#######

#######

Above image shows ‘fy’ to morse code on port 10105

#### Task 2

In this task, where the primary code, morse.py includes the binary tree, encode and decode functions, and some binary tree testing functions for unit testing in task 3.

    root = Node("START")

    root.dot = Node('E')
    root.dash = Node('T')

    root.dot.dot = Node('I')
    root.dot.dash = Node('A')
    root.dash.dot = Node('N')
    root.dash.dash =Node('M')

    root.dot.dot.dot = Node('S')
    root.dot.dot.dash = Node('U')
    root.dot.dash.dot = Node('R')
    root.dot.dash.dash = Node('W')
    root.dash.dot.dot = Node('D')
    root.dash.dot.dash = Node('K')
    root.dash.dash.dot = Node('G')
    root.dash.dash.dash = Node('O')

There is a total of 7 levels in the binary tree. The codes for the binary tree is based on the diagram provided in the worksheet where it started with ‘START’ and then split into 2 part which is left and right, where dots are left and dashed are right.

######

##### Encode

The input to the encoding function is a string. It then runs through the input string, doing pre-order traversal on each character. This traversal records the path it took to locate the char in the tree. This will be the result.

##### Decode

As an argument, the decoding function will accept the morse to decode as a string. It begins by breaking down the morse code into individual letters and words. When it encounters single whitespace, for example, it separates it into letters; however, three whitespaces in a row signal the gap between words, and it splits appropriately. It then loops over the list of words, and then through each word's characters.

addition functions are in morse.py as requested in task 3

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

The below image is the output of morse.py where it encodes the message FOON and decodes ‘..-. -.—'
#####

#### Task 3
Unit test is used for testing a unit, which is the smallest amount of code in a system that can be logically separated. That is a function, a subroutine, a method, or a property in most programming languages. It's crucial to focus on the solitary component of the term.

Below image is the output of assert_tests.py
#####

There are 5 tests for encoding and 5 for decoding. The pictures below are 2 of the test functions out of 10. 

   class TestMorse(unittest.TestCase):
    def test_encode_us(self):
        self.assertEqual( morse.encode('us'), '..- ...')

    def test_encode_fy(self):
        self.assertEqual( morse.encode('FY'), '..-. -.--')

Also, I’ve added tests for the binary tree implementation which test: 

1. that a tree is correctly empty 
2. that a tree is not empty 
3. the insert function 
4. the delete function 
5. find function

 
            # Other tests
            # Test tree
        def test_isTreeEmpty(self):
            self.assertEqual(morse.checkIsEmpty(), False)

        def test_isTreeNotEmpty(self):
        self.assertEqual(morse.checkIsNotEmpty(), True)

        # Test insertion
        def test_insert_false(self):
            self.assertEqual(morse.insert('E'), False)

        def test_insert_true(self):
            self.assertEqual(morse.insert('choo'), True)

        # Tests Deletion
        def test_delete_true(self):
            self.assertEqual(morse.delete('E'), True)

        def test_delete_false(self):
            self.assertEqual(morse.delete('choo'), False)

        def test_delete_fail(self):
            self.assertEqual(morse.delete('choo'), True)

        # Test Search
        def test_find_true(self):
            self.assertEqual(morse.find('E'), True)

        def test_find_false(self):
            self.assertEqual(morse.find('choo'), False)

        def test_find_fail(self):
            self.assertEqual(morse.find('choo'), True)

#### Task 4

Most of the punctuations and symbols are in the 5th and 6th level of the binary tree as there are 6 characters for its morse code. Meanwhile ‘&’ and ‘_’ are in the 7th level of the binary tree. This is because both of the symbols have 7 characters in morse codes

The codes below shows 5th, 6th and 7th levels of the binary tree in morse.py

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

and Unit test for punctuations and symbols in morseunit.py
    # Task 4 Testing
    def test_encode_task4(self):
    self.assertEqual(morse.encode('(+&,:"!)'), '-.--. .-.-. .-... --..-- ---... .-..-. -.-.-- -.--.-')

    def test_decode_task4(self):
    self.assertEqual(morse.decode('-.--. .-.-. .-... --..-- ---... .-..-. -.-.-- -.--.-'), '(+&,:"!)')
