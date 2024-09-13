'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


Constraints:

0 <= x <= 231 - 1

Answer:
'''


class Solution:
    def mySqrt(self, x: int) -> int:
        _list = [i for i in range(0, x+1)]
        # need to do binary search for getting the result
        low = 0
        high = len(_list)-1

        mid = low + (high-low) //2

        if _list[mid] * _list[mid] ==


A = Solution()
A.mySqrt()