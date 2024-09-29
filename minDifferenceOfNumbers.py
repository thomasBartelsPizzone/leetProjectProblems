
class Solution:
    def minDiffList(self, nums):
        print(nums)
        nums.sort()
        print(nums)
        dict_d = {}
        min_d = nums[1] - nums[0]
        dict_d[(nums[0], nums[1])] = min_d
        for i in range(1, len(nums)-1):
            dif = nums[i+1] - nums[i]
            if dif <= min_d:
                if dif < min_d:
                    dict_d.clear()
                min_d = dif
                dict_d[(nums[i], nums[i+1])] = min_d
        print("dict_d: ", dict_d)
        # dict_d = {k: v for k, v in dict_d.items() if value == target_value}
        sorted_dict = sorted(dict_d.items(), key=lambda x: x[1], reverse=True)
        print(type(sorted_dict))
        print("sorted_dict: ", sorted_dict)
        sorted_dict.append(((24, 242), 218))
        print("sorted_dict: ", sorted_dict)
        sorted_dict_k = [k for k, v in sorted_dict if v == min_d]
        for p in sorted_dict_k:
            i, j = sorted(p)
            print(i, j)




if __name__ == "__main__":
    c = Solution()
    c.minDiffList([130, 10, 5, 4, 1, 2, 15, 18, 65, 11, 16, 131])