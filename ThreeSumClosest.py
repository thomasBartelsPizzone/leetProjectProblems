from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # nums.sort()
        # ret_arr = set()
        min_dist = {}
        min_so_far = float('inf')
        nums_l = len(nums)
        for i in range(nums_l - 2):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            sum_val1 = nums[i]
            sum_idx2 = i + 1
            sum_idx3 = nums_l - 1
            while sum_idx2 < sum_idx3:
                sum_of_three = sum_val1 + nums[sum_idx2] + nums[sum_idx3]
                # print("val1: ", sum_val1)
                # print("val2: ", nums[sum_idx2])
                # print("val3: ", nums[sum_idx3])
                # print("sum_of_three: ", sum_of_three)
                # diff_target = abs(sum_of_three - target)
                diff_target = abs(target - sum_of_three)
                min_dist[sum_of_three] = diff_target
                if min_so_far > diff_target:
                    min_so_far = diff_target
                if diff_target == 0:
                    # if sum_of_three == 0:
                    # ret_arr.add((sum_val1, nums[sum_idx2], nums[sum_idx3]))
                    sum_idx2 += 1
                    sum_idx3 -= 1
                    while sum_idx2 < sum_idx3 and nums[sum_idx2] == nums[sum_idx2 - 1]:
                        sum_idx2 += 1
                    while sum_idx2 < sum_idx3 and nums[sum_idx3] == nums[sum_idx3 + 1]:
                        sum_idx3 -= 1
                elif diff_target < 0:
                    sum_idx2 += 1
                else:
                    sum_idx3 -= 1
        if min_so_far in min_dist.values():
            return [k for k, v in min_dist.items() if v == min_so_far][0]
        return 0

if __name__ == "__main__":
    c = Solution()
    # print(c.threeSumClosest([-1,2,1,-4], 1))
    print(c.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))