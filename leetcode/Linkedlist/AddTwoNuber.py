'''

Code
Testcase
Test Result
Test Result
2. Add Two Numbers
Medium
Topics
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

Answer:
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MakeLLChain:

    head: ListNode = None
    def __init__(self) -> None:
        self.head = None
    
    def MakeChain(self,llList:list)->None:
        self.head = ListNode(llList[0])
        current = self.head
        for i in llList[1:]:
            newNone = ListNode(i)
            current.next = newNone
            current = current.next
        return self.head

    def PrintLL(self):
        current = self.head
        while current:
            print(" ",current.val)
            current = current.next

class Solution(MakeLLChain):
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        spareList = []
        inHand = 0
        current1 = l1.head
        current2 = l2.head
        
        while (current1 or current2):
            if current1 and current2:
                value = current1.val + current2.val + inHand
                if value > 9:
                    inHand = 1
                    spareList.append(value%10)
                else:
                    inHand = 0
                    spareList.append(value)
                current1 = current1.next
                current2 = current2.next
            elif current1 or current2:
                if current1:
                    value = current1.val + inHand
                    if value > 9:
                        inHand = 1
                        spareList.append(value%10)
                    else:
                        inHand = 0
                        spareList.append(value)
                    current1 = current1.next
                if current2:
                    value = current2.val + inHand
                    if value > 9:
                        inHand = 1
                        spareList.append(value%10)
                    else:
                        inHand = 0
                        spareList.append(value)
                    current2 = current2.next

        if inHand == 1:
            spareList.append(1)

        return self.MakeChain(spareList)

# l1 = [2,4,3]
# l2 = [5,6,4]
# l1 = [0]
# l2 = [0]
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

print("1st:")
A = MakeLLChain()
A.MakeChain(l1)
A.PrintLL()
print("2nd:")
B = MakeLLChain()
B.MakeChain(l2)
B.PrintLL()
print("Final:")
s = Solution()
s.addTwoNumbers(A,B)
s.PrintLL()

