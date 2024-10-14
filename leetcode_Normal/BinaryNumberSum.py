'''
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

'''

# Answer:

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        _a = a

        if (len(b)>len(a)):
            a = b
            b = _a
        res = ""
        carry = 0
        diff = len(a)-len(b)
        for i in range(diff):
            b = "0" + b

        for i in range(len(a)-1,-1,-1):
            if a[i] == "1" and b[i] == "1":
                if carry == 1:
                    res = "1" + res
                    carry = 1
                else:
                    res = "0" + res
                    carry = 1
            elif (a[i] == "0" and b[i] == "1") or (a[i] == "1" and b[i] == "0"):
                if carry == 1:
                    res = "0" + res
                    carry = 1
                else:
                    res = "1" + res
            elif a[i] == "0" and b[i] == "0":
                if carry == 1:
                    res = "1" + res
                    carry = 0
                else:
                    res = "0" + res

        if carry == 1:
            res = "1" + res

        return res



A = Solution()
print(A.addBinary(a = "1111", b = "1111"))