"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?"""


class Solution:
    def getCounts(self, nums:str) -> dict:
        letterCountDict = {}
        for letter in nums:
            if letter in letterCountDict.keys():
                letterCountDict[letter] += 1
            else:
                 letterCountDict[letter] = 1 
        return letterCountDict

    def isAnagram(self, s: str, t: str) -> bool:
        sCount = self.getCounts(s)
        tCount = self.getCounts(t)
        flag = False
        for item in s:
            if item in tCount.keys() and sCount[item] == tCount[item]:
                flag = True  
            else:
                return False   

        return len(sCount.keys()) == len(tCount.keys()) if flag else flag