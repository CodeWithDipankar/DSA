'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None

class MakeLinkedListChain:
    def __init__(self, values):
        if values:
            self.head = Node(values[0])
            current = self.head
            for value in values[1:]:
                next_node = Node(value)
                current.next = next_node
                current = next_node
        else:
            self.head = None

    def linkedlist_to_list(self) -> list:
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

class Solution(object):
    def mergeTwoLists(self, Llist1, Llist2):
        dummy = Node()
        current = dummy

        while Llist1 and Llist2:
            if Llist1.value <= Llist2.value:
                current.next = Llist1
                Llist1 = Llist1.next
            else:
                current.next = Llist2
                Llist2 = Llist2.next
            current = current.next

        if Llist1:
            current.next = Llist1
        elif Llist2:
            current.next = Llist2

        return dummy.next

# Initialization of linked lists
list1 = [1, 13, 14, 35, 47, 69]
list2 = [10, 30, 40, 50, 70, 99]
linkedList1 = MakeLinkedListChain(list1)
linkedList2 = MakeLinkedListChain(list2)

# Print initial linked lists
print("LinkedList1 elements are:-->", linkedList1.linkedlist_to_list())
print("LinkedList2 elements are:-->", linkedList2.linkedlist_to_list())

# Merge the linked lists
solution = Solution()
merged_head = solution.mergeTwoLists(linkedList1.head, linkedList2.head)

# Convert merged linked list to list and print it
merged_linked_list = MakeLinkedListChain([])
merged_linked_list.head = merged_head
print("After merging, the merged linked list is:--->", merged_linked_list.linkedlist_to_list())
