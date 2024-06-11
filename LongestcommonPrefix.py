'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.'''

#My stupid approach

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        elif len(strs)>1:
             
            if len(strs[0])<1:
                return "" 
            else:
                needToMatch = strs[0]
                
            
            largestCommonList = []

            for item in strs[1:]:
                largestCommon = "" 
                for index,words in enumerate(item):
                    if len(words)<1:
                        return ""
                    try:
                        value = needToMatch[index] 
                    except:
                        break
                    if index == 0:
                        if needToMatch[index] == words:
                            largestCommon += words
                        else:
                            return ""
                        

                    elif needToMatch[index] == words:
                        largestCommon += words
                    else:
                        break
                largestCommonList.append(largestCommon)
                
            length = len(largestCommonList[0])
            index = 0
            for _index,shortCommon in enumerate(largestCommonList[1:]):
                if len(shortCommon)< length:
                    length = len(shortCommon)
                    index = _index+1

            return largestCommonList[index]
        else:
            return strs[0]

a = Solution()
strs = ["a","ac"] #["flower","flow","flight"] #["","b"] #["dog","racecar","car"] #["cows","cow","co","cowes"]
print(a.longestCommonPrefix(strs))
        