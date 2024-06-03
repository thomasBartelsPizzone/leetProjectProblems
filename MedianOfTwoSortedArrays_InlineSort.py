from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_l = nums1 + nums2
        new_l.sort()
        l_new_l = len(new_l)
        h_l_new_l = l_new_l // 2
        if l_new_l % 2 == 0:
            sum1 = new_l[h_l_new_l-1]
            sum2 = new_l[h_l_new_l]
            return (sum1 + sum2) / 2
        else:
            return new_l[h_l_new_l]


if __name__ == "__main__":
    c = Solution()
    print(c.findMedianSortedArrays([1, 3], [2]))
    print(c.findMedianSortedArrays([1, 2], [3, 4]))
    print(c.findMedianSortedArrays([1, 2, 6, 9, 10], [3, 4, 5, 7]))