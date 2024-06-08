'''Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?


Answer:'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_ = str(x)[::-1]
        if str(x) == x_:
            return True
        else:
            return False


a = Solution()
print(a.isPalindrom(123))


'''
Another approach is without converting it to string ---

Answer:
'''
def is_palindrome(x: int) -> bool:
    # Negative numbers and numbers ending with 0 but not 0 itself are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_number = 0
    original_number = x

    while x > 0:
        digit = x % 10
        reversed_number = reversed_number * 10 + digit
        x //= 10 #initialized the number after dividing the number with 10

    return original_number == reversed_number

if __name__ == "__main__":
    number = 123
    print(f"The number {number} is palindrom ? Answer:-> {is_palindrome(number)}")
