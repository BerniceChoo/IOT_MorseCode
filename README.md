# iotworksheet2
## Part 1

#### Task 1

I have use SSH to redirect the port (10105) to my local system in order to connect to the server via a browser running on my local machine: in my case, google chrome. SSH port forwarding is a feature of SSH that allows me to tunnel application ports from the server to the client or vice versa. This can be done straight from the command line using the ssh command, but it's far easier to do it from VS code.

After clicking on it, it will direct me to the webserver where I am able to enter text to encode and vice versa. There I will get the result of the morse code. An example is shown below, where after encoding ‘fy’, it will become  ‘..-. -.--’ in port 10105.

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
