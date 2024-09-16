class Node:
    def __init__(self, value=0, next=None) -> None:
        self.value = value
        self.next = next

class LinkedListOperation:
    def __init__(self) -> None:
        self.head = None

    def MakeLLChain(self, nodelist: list = []):
        if nodelist:
            startIndex = 0 if self.head is not None else 1
            if startIndex == 1:
                self.head = Node(nodelist[0])
            current = self.head
            for i in nodelist[startIndex:]:
                newNode = Node(i)
                current.next = newNode
                current = newNode

    def PrintLL(self):
        output = ""
        node = self.head
        while node is not None:
            output += str(node.value) + " -> "
            node = node.next
        print("\nLL view :", output.strip(" -> "))

    def InsertionAtAnyPos(self, pos=None):
        # Check if the list is empty
        if self.head is None:
            print("The list is empty. Initializing with the new node.")
            Nodevalue = input("Please enter the value of the new node: ")
            self.head = Node(Nodevalue)
        else:
            print("Insertion at position:", "last" if pos is None else pos)
            # Handle insertion when list is not empty
            if pos is None:
                # Insert at the end
                new_value = input("Please enter the value of the new node: ")
                new_node = Node(new_value)
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = new_node
            else:
                # Insert at a specific position
                pos = int(pos)
                new_value = input("Please enter the value of the new node: ")
                new_node = Node(new_value)
                if pos == 0:
                    new_node.next = self.head
                    self.head = new_node
                else:
                    current = self.head
                    index = 0
                    while current is not None and index < pos - 1:
                        current = current.next
                        index += 1
                    if current is None:
                        print("Position out of bounds")
                    else:
                        new_node.next = current.next
                        current.next = new_node

    def FindNode(self,nodevalue= None):
        if nodevalue is not None:
            if self.head is not None:
                pass
            else:
                print("No node found.")
        else:
            value = input("Please enter the search node:")
            self.FindNode(value)



# Test the class
NodeOperation = LinkedListOperation()
# Test the case where the list is empty and insertion is called
NodeOperation.InsertionAtAnyPos()  # Should initialize with the new node
NodeOperation.PrintLL()

# Add some more elements and test insertion at specific positions
NodeOperation.MakeLLChain([1, 3, 5, 6, 7, 8, 9, 11])
NodeOperation.PrintLL()
NodeOperation.InsertionAtAnyPos()  # Insert at the end
NodeOperation.PrintLL()
NodeOperation.InsertionAtAnyPos(3)  # Insert at position 3
NodeOperation.PrintLL()


#travershal
