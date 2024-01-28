# Nodes
# 1. Value - anythin strings, integers, objects
# 2. The Next Node

class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

# '3' -> '7' -> '10'

node1 = linkedListNode('3') # '3'
node2 = linkedListNode('7') # '7'
node3 = linkedListNode('10') # '10'

node1.nextNode = node2 # node1 -> node2 , '3' -> '7'
node2.nextNode = node3 # node2 -> node3 , '7' -> '10'

# node1 -> node2 -> node3


currentNode = node1
while True:
    print(currentNode.value, '->', end=' ')
    if currentNode.nextNode is None:
        print('None')
        break
    currentNode = currentNode.nextNode