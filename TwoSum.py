class Solution(object):
    def twoSum(self, nums, target):
        lookup = {}   
        for i, n1 in enumerate(nums):
            # print("lookup: ", lookup)
            rem = target - n1
            if rem in lookup.keys():
                idx1 = lookup[rem]
                idx2 = i
                return [idx1, idx2]
            lookup[n1] = i
        return []
        # for idx1, n1 in enumerate(nums):
        #     temp_ = [idx1]
        #     # print("at idx", idx1, "val: ", n1)
        #     for idx2, n2 in enumerate(nums):
        #         if idx1 != idx2:
        #             if target == (n1 + n2):
        #                 temp_.append(idx2)
        #                 return temp_
        # return_list = []
        # res = 0
        # for i, n in enumerate(nums):
        #     if i > 0:
        #         if res == n:
        #             return_list.append(i)
        #             return return_list
        #         else:
        #             return_list.pop()
        #             res = target - n
        #             return_list.append(i)
        #     else:
        #         res = target - n
        #         return_list.append(i)

if __name__ == "__main__":
    c = Solution()
    print(c.twoSum([3, 3], 6))
    print(c.twoSum([2, 7, 11, 15], 9))