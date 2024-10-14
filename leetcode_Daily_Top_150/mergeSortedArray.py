class Solution:
  def merge(self, nums1, m, nums2, n) -> None:
      """
      Do not return anything, modify nums1 in-place instead.
      """

      i_max_num1 = m-1
      i_max_num2 = n-1

      len_total = (m + n) - 1

      print(nums1)
      while(i_max_num2 >= 0):
          if (nums1[i_max_num1] < nums2[i_max_num2]):
              nums1[len_total] = nums2[i_max_num2]
              len_total -= 1
          else:
              while(nums1[i_max_num1] >= nums2[i_max_num2] and len_total != 0):
                  if len_total != -1:
                      nums1[len_total] = nums1[i_max_num1]
                      len_total -= 1
                      i_max_num1 -= 1
                  else:
                      break

              nums1[len_total] = nums2[i_max_num2]
              len_total -= 1
          i_max_num2 -= 1
      print(nums1)
a = Solution()
a.merge(nums1 = [2,0], m = 1, nums2 = [1], n = 1)

# a.merge([1,2,3,0,0,0], 3, [2,5,6], 3)