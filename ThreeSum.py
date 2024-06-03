from typing import List
from collections import defaultdict


class Solution(object):
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lookup = {}
        ret_arr = []
        for i, n1 in enumerate(nums):
            # print("lookup: ", lookup)
            rem = -n1
            # rem = 0 - n1
            if rem in lookup:
                for val in lookup[rem]:
                    if i != val:
                        ret_arr.append([val, n1, rem])
                # idx1 = lookup[rem]
                # idx2 = i
                # # return [nums[idx1], nums[idx2]]
                # # ret_arr.append([start_num, nums[idx1], nums[idx2]])
                # temp_list = [start_num, nums[idx1], nums[idx2]]
                # temp_list.sort()
                # if temp_list not in self.ans_list:
                #     self.ans_list.append(temp_list)
            # lookup[n1] = i
            lookup.setdefault(n1, []).append(i)
        # return []
        return ret_arr"""

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret_arr = set()
        nums_l = len(nums)
        for i in range(nums_l - 2):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            sum_val1 = nums[i]
            sum_idx2 = i + 1
            sum_idx3 = nums_l - 1
            while sum_idx2 < sum_idx3:
                # if nums[sum_idx2] == nums[sum_idx2 - 1]:
                #     sum_idx2 += 1
                #     continue
                # if nums[sum_idx3] == nums[sum_idx3 + 1]:
                #     sum_idx3 -= 1
                #     continue
                sum_of_three = sum_val1 + nums[sum_idx2] + nums[sum_idx3]
                if sum_of_three == 0:
                    ret_arr.add((sum_val1, nums[sum_idx2], nums[sum_idx3]))
                    sum_idx2 += 1
                    sum_idx3 -= 1
                    # while sum_idx2 < sum_idx3:
                    #     if nums[sum_idx2] == nums[sum_idx2 - 1]:
                    #         sum_idx2 += 1
                    #     if nums[sum_idx3] == nums[sum_idx3 + 1]:
                    #         sum_idx3 -= 1
                    while sum_idx2 < sum_idx3 and nums[sum_idx2] == nums[sum_idx2 - 1]:
                        sum_idx2 += 1
                    while sum_idx2 < sum_idx3 and nums[sum_idx3] == nums[sum_idx3 + 1]:
                        sum_idx3 -= 1
                elif sum_of_three < 0:
                    sum_idx2 += 1
                else:
                    sum_idx3 -= 1
        # return ret_arr
        new_arr = []
        for a in ret_arr:
            new_arr.append(list(a))
        return new_arr

    """    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        neg_dict = {}
        neg_dict.setdefault(nums)
        pos_dict = {}
        pos_dict.setdefault(nums)
        zero_cnt = 0
        ret_arr = []
        n = len(nums)
        for n in nums:
            if n < 0:
                neg_dict[n] += 1
            elif n > 0:
                pos_dict[n] += 1
            else:
                zero_cnt += 1

        if zero_cnt > 0:
            for nv in neg_dict.keys():
                if -1 * nv in pos_dict.keys():
                    ret_arr.append([nv, 0, -1 * nv])
            if zero_cnt > 2:
                ret_arr.append([0, 0, 0])

        for set1, set2 in ((neg_dict, pos_dict), (pos_dict, neg_dict)):
            set1Items = list(set1.items())
            for i, (j, k) in enumerate(set1Items):
                for j2, k2 in set1Items[i:]:
                    if j != j2 or (j == j2 and k > 1):
                        if -j-j2 in set2:
                            ret_arr.append([j, j2, -j-j2])
        return ret_arr
    """

    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret_arr = []
        n = len(nums)
        for i in range(n - 2):
            # Skip duplicates
            # if i > 0 and nums[i] == nums[i - 1]:
            #     continue
            left, right = i + 1, n - 1
            while left < right:
                sum_of_three = nums[i] + nums[left] + nums[right]
                if sum_of_three == 0:
                    ret_arr.append([nums[i], nums[left], nums[right]])
                    left += 1
                    # # Skip duplicates
                    # while left < right and nums[left] == nums[left - 1]:
                    #     left += 1
                elif sum_of_three < 0:
                    left += 1
                else:
                    right -= 1
        return ret_arr
    """


    """
    def __init__(self):
        self.ans_list = []

    def twoSum(self, nums, target, start_num):
        lookup = {}
        ret_arr = []
        for i, n1 in enumerate(nums):
            # print("lookup: ", lookup)
            rem = target - n1
            if rem in lookup.keys():
                idx1 = lookup[rem]
                idx2 = i
                # return [nums[idx1], nums[idx2]]
                # ret_arr.append([start_num, nums[idx1], nums[idx2]])
                temp_list = [start_num, nums[idx1], nums[idx2]]
                temp_list.sort()
                if temp_list not in self.ans_list:
                    self.ans_list.append(temp_list)
            lookup[n1] = i
        # return []
        # return ret_arr
        return None
    #
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        ans_list = []
        ret_list = []
        nums.sort()
        #
        if sum(nums) == 0:
            # print(nums)
            # print(ans_list.append(nums))
            # l = ans_list.append(nums)
            return [nums]
        #
        # for i, n in enumerate(nums):
        for i in range(len(nums)//2):
            n = nums[i]
            new_target = target - n
            new_list = nums[0:i] + nums[i+1:]
            # ret_arr = self.twoSum(new_list, new_target, n)
            self.twoSum(new_list, new_target, n)
            # if ret_arr:
            #     # print("ret array: ", ret_arr)
            #     # if ret_arr not in ans_list:
            #     # ans_list.append(ret_arr)
            #     ret_list.append(ret_arr)
            #     # for r in ret_arr:
            #     #     # print(r)
            #     #     # ret_list += (r.append(n))
            #     #     r.append(n)
            #     #     # print(r)
            #     #     ret_list.append(r)
            #     # ret_list += ret_arr
        #
        # ans_set = set()
        # for l in ret_list:
        #     print(l)
        #     l.sort()
        #     print(l)
        #     if l not in ans_list:
        #         ans_list.append(l)
        # #     ans_set.
        # # return list(ans_set)
        # return
        ans_list = self.ans_list
        self.ans_list = []
        return ans_list
    """

"""
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lookup = {}
        ret_arr = []
        for i, n1 in enumerate(nums):
            # print("lookup: ", lookup)
            rem = 0 - n1
            if rem in lookup.keys():
                idx1 = lookup[rem]
                idx2 = i
                # return [nums[idx1], nums[idx2]]
                # ret_arr.append([start_num, nums[idx1], nums[idx2]])
                temp_list = [n1, nums[idx1], nums[idx2]]
                temp_list.sort()
                if temp_list not in self.ans_list:
                    self.ans_list.append(temp_list)
            lookup[n1] = i
        # return []
        # return ret_arr
        # return None
        ans_list = self.ans_list
        self.ans_list = []
        return ans_list
"""

if __name__ == "__main__":
    c = Solution()
    # print(c.twoSum([3, 3], 6))
    # print(c.twoSum([2, 7, 11, 15], 9))
    # print(c.twoSum([3, 2, 4], 6))

    print(c.threeSum([-1, 0, 1, 2, -1, -4]))
    print(c.threeSum([0, 1, 1]))
    print(c.threeSum([0, 0, 0]))
