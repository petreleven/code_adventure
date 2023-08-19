class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.privatenext = None
    
    def setNextNode(self, next):
        self.privatenext =  next

    def getNextNode(self):
        return self.privatenext


class LinkedList:
    def __init__(self, node : Node) -> None:
        self.head = node
        
    def insert(self, node : Node):        
        temp = self.head
        while temp.getNextNode() != None:
            temp = temp.getNextNode()
        temp.setNextNode(node)

    def iter(self):
        temp = self.head
        vals = []
        
        while temp.getNextNode() != None:
            vals.append(temp.value)
            temp = temp.getNextNode()
        
        vals.append(temp.value)
        return vals

    def pop(self):
        temp = self.head
        try:
            while temp.getNextNode().getNextNode() != None:
                temp = temp.getNextNode()
            temp.setNextNode(None)
        except AttributeError:
            print('error')
        


a = Node(1)
ll = LinkedList(a)


print(ll.iter())
ll.pop()
print(ll.iter())


