from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        new_arr = []
        phone_dict = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }
        str_dict = {}
        ctr = 0
        for d in digits:
            if d not in str_dict:
                str_dict[d] = phone_dict[int(d)]
            else:
                str_dict[d + str(ctr)] = phone_dict[int(d)]
            ctr += 1

        print("str_dict")
        print(str_dict)
        len_dict = len(str_dict)

        if len_dict == 0:
            return new_arr
        elif len_dict == 1:
            k, v = next(iter(str_dict.items()))
            return v
        else:
            for i in range(len_dict - 1):
                if i == 0:
                    l1 = str_dict[digits[i]]
                else:
                    l1 = new_arr
                l2 = str_dict[digits[i + 1]]
                # new_arr += [l1i + l2i for l1i, l2i in zip(l1, l2)]
                new_arr = [l1i + l2i for l1i in l1 for l2i in l2]
                print(new_arr)
        return new_arr

if __name__ == "__main__":
    c = Solution()
    # print(c.twoSum([3, 3], 6))
    # print(c.twoSum([2, 7, 11, 15], 9))
    # print(c.twoSum([3, 2, 4], 6))

    print(c.letterCombinations("23"))
    print(c.letterCombinations(""))
    print(c.letterCombinations("2"))

