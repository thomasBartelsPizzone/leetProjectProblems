from typing import List


class Solution:
    def merge_sort(self, x: List[int], m, y: List[int], n) -> List[int]:
        if m == 0: return y
        if n == 0: return x
        if x[0] <= y[0]:
            m -= 1
            return [x[0]] + self.merge_sort(x[1:], m, y, n)
        else:
            n -= 1
            return [y[0]] + self.merge_sort(x, m, y[1:], n)

    def retMed(self, nums3: List[int]) -> float:
        l_nums3 = len(nums3)
        h_l_nums3 = l_nums3 // 2
        if l_nums3 % 2 == 0:
            sum1 = nums3[h_l_nums3 - 1]
            sum2 = nums3[h_l_nums3]
            return (sum1 + sum2) / 2
        else:
            return nums3[h_l_nums3]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m == 0:
            return self.retMed(nums2)
        if n == 0:
            return self.retMed(nums1)
        # nl = self.merge_sort(nums1, m, nums2, n)
        # print(nl)
        # return self.retMed(nl)
        return self.retMed(self.merge_sort(nums1, m, nums2, n))


if __name__ == "__main__":
    c = Solution()
    print(c.findMedianSortedArrays([1, 3], [2]))
    print(c.findMedianSortedArrays([1, 2], [3, 4]))
    print(c.findMedianSortedArrays([1, 2, 6, 9, 10], [3, 4, 5, 7]))