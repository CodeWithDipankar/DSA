class  Node:
    def __init__(self,value= 0, next = None) -> None:
        self.value = value
        self.next = next


newNode = Node(10)
print("Node address, Node value, node next addess",newNode, newNode.value,newNode.next)