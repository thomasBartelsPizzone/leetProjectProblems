from typing import List

class Solution:
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            nums1[:] = nums2
        else:
            if n > 0:
                i = 0
                while i < m + n and nums2:
                    print(f"@{i}, nums1: \n{nums1}")
                    print("nums1[i]: ", nums1[i])
                    # if nums1[i] < nums2[0] and i > 0:
                    #     nums1[i+1] = nums1[i]
                    #     nums1[i] = nums2[0]
                    # if nums1[0] == 0:
                    # if nums1[i] <= nums2[0] and nums1[i] > 0:
                    if i > 0:
                        if nums1[i] >= nums1[i-1]:
                            if nums1[i] <= nums2[0]:
                                i += 1
                            # elif nums1[i] == 0:
                            #     nums1[i] = nums2[0]
                            #     nums2 = nums2[1:]
                            #     i += 1
                            else:
                                # elif nums1[i] > nums2[0] or (nums1[i] == 0 and i > 0):
                                # print("nums1[i]: ", nums1[i])
                                # print("nums1[i+1:]: ", nums1[i+1:])
                                # print("nums1[i+2:]: ", nums1[i+2:])
                                nums1[i+1:] = nums1[i:-1]
                                # print("nums1[i+1:]: ", nums1[i+1:])
                                # print("nums1[i+2:]: ", nums1[i+2:])
                                # nums1[i + 1] = nums1[i]
                                nums1[i] = nums2[0]
                                nums2 = nums2[1:]
                        else:
                            nums1[i+1:] = nums1[i:-1]
                            nums1[i] = nums2[0]
                            nums2 = nums2[1:]
                    else:
                        if nums1[i] <= nums2[0]:
                            i += 1
                        else:
                            nums1[i+1:] = nums1[i:-1]
                            nums1[i] = nums2[0]
                            nums2 = nums2[1:]

        print("@end, nums1: \n", nums1)


    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            nums1[:] = nums2
        elif n > 0:
            i = 0
            while nums2:
                # print(f"@{i}, nums1: \n{nums1}")
                # print(f"@{i}, nums2: \n{nums2}")
                # print(f"@{i}, {nums1[i]}")
                if i < m:
                    if nums1[i] > nums2[0]:
                        nums1[i+1:] = nums1[i:-1]
                        nums1[i] = nums2[0]
                        nums2 = nums2[1:]
                        m += 1
                    else:
                        i += 1
                else:
                    nums1[i+1:] = nums1[i:-1]
                    nums1[i] = nums2[0]
                    nums2 = nums2[1:]
                    i += 1
                # i += 1
            ## IF a num2 is inserted, then the length to loop through is greater than m
            # for i in range(m):
            #     print(f"@{i}, nums1: \n{nums1}")
            #     print(f"@{i}, nums2: \n{nums2}")
            #     print(f"@{i}, {nums1[i]}")
            #     if nums1[i] > nums2[0]:
            #         nums1[i+1:] = nums1[i:-1]
            #         # nums1[i] = nums2[i]
            #         nums1[i] = nums2[0]
            #         nums2 = nums2[1:]
            # # print("nums1: ", nums1)
            # print("nums1[m:]: ", nums1[m:])
            # print("nums1[m+1:]: ", nums1[m+1:])
            # print("nums2: ", nums2)
            # # print("nums1[m+1:]: ", nums1[m+1:])
            # nums1[m+1:] = nums2

        print(f"@{n+m}, nums1: \n{nums1}")






if __name__ == "__main__":
    c = Solution()
    nums1 = [-12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    nums2 = [-49, -45, -42, -41, -40, -39, -39, -39, -38, -36, -34, -34, -33, -33, -32, -31, -29, -28, -26, -26, -24, -21, -20,
     -20, -18, -16, -16, -14, -11, -7, -6, -5, -4, -4, -3, -3, -2, -2, -1, 0, 0, 0, 2, 2, 6, 7, 7, 8, 10, 10, 13, 13,
     15, 15, 16, 17, 17, 19, 19, 20, 20, 20, 21, 21, 22, 22, 24, 24, 25, 26, 27, 29, 30, 30, 30, 35, 36, 36, 36, 37, 39,
     40, 41, 42, 45, 46, 46, 46, 47, 48]
    # print(c.merge(nums1, 1, nums2, 90))
    print(c.merge([1, 0], 1, [2], 1))
    print(c.merge([-1,0,0,3,3,3,0,0,0], 6, [1, 2, 2], 3))
    print(c.merge([1,2,3,0,0,0], 3, [2, 5, 6], 3))
    print(c.merge([1], 1, [], 0))
    print(c.merge([0], 0, [1], 1))