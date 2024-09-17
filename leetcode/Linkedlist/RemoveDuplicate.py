'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.



Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
Answer:
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    head: ListNode

    def __init__(self)->None:
        self.head = None

    def MakeChain(self,llList:list)->None:
        self.head = ListNode(llList[0])
        current = self.head
        for i in llList[1:]:
            newNode = ListNode(i)
            current.next = newNode
            current = current.next
        return self.head

    def PrintLL(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next


    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        spareList = []

        if head:
            current = head
            beforecurrent = head
            while current:
                if current.val not in spareList:
                    spareList.append(current.val)
                    beforecurrent = current
                else:
                    beforecurrent.next = current.next
                current = current.next

        return  head


A = Solution()
head = A.MakeChain([1,1,2])
A.PrintLL()
A.deleteDuplicates(head)
print("later data:")
A.PrintLL()