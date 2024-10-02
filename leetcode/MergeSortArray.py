'''
you are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


Answer:
'''

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        iL1max = m-1
        iL2max = n-1

        iL1Last = len(nums1)-1
        print("Before merging, List1:",nums1,",List2:",nums2)
        while (iL2max>=0):
            # print(iL2max,iL1max,iL1max)
            if nums2[iL2max]>nums1[iL1max]:
                nums1[iL1Last] = nums2[iL2max]
                iL1Last -= 1
                print(f"\n\t->step({n-iL2max}): ",nums1)
            else:
                i=1
                while(nums1[iL1max]>= nums2[iL2max] and iL1Last != 0):

                    if iL1max != -1:
                        nums1[iL1Last] = nums1[iL1max]
                        iL1max -= 1
                        iL1Last -=1
                    else:
                        break
                    print(f"\n\t\t->step({n-iL2max-1}.{i}): ",nums1)
                    i+=1

                nums1[iL1Last] = nums2[iL2max]
                iL1Last -= 1
                print(f"\n\t->step({n-iL2max}): ",nums1)

            iL2max -= 1
        print("\nAfter Merging List1:",nums1)




a = Solution()
# a.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
a.merge(nums1 = [4,5,6,0,0,0], m = 3, nums2 = [1,2,3], n = 3)




