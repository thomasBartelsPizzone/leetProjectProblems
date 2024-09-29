from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        # temp_height = copy(height)
        # temp_height.sort()
        max_A = 0
        for i in range(n-1):
            for j in range(1, n):
                temp_A = (j - i) * min(height[i], height[j])
                if temp_A > max_A:
                    max_A = temp_A
        return max_A

if __name__ == "__main__":
    c = Solution()
    print(c.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(c.maxArea([1, 1]))