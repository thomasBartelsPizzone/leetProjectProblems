from typing import List


class Solution:
    # Works but would work out of sequence, can assume i == i+1 if any matches
    def removeDuplicates(self, nums: List[int]) -> int:
        ctr = 0
        nums_dict = {}
        for n in nums:
            if n not in nums_dict.keys():
                ctr += 1
                nums_dict[n] = ctr
        # print("dict? ", nums_dict)
        new_nums = list(nums_dict.keys())
        # print(new_nums)
        nums[0:len(new_nums)] = new_nums
        # print(nums)
        return len(new_nums)

if __name__ == "__main__":
    c = Solution()
    print(c.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))