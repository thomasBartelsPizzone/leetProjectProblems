class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #         ansDict1 = {}
        #         ansDict2 = {}
        #         for s in ransomNote:
        #             ansDict1[s] = ansDict1.get(s, 0) + 1

        #         for s in magazine:
        #             ansDict2[s] = ansDict2.get(s, 0) + 1

        #         for k, v in ansDict1.items():
        #             if v > ansDict2.get(k, 0):
        #                 return False
        #         return True
        for r in ransomNote:
            if r in magazine:
                magazine = magazine.replace(r, '', 1)
            else:
                return False
        return True

#             ansDict1[tuple(row)] = ansDict1.get(tuple(row), 0) + 1
#         lr = len(ransomNote)
#         lm = len(magazine)
#         if lr > lm:
#             return False

#         r = sorted(ransomNote)
#         m = sorted(magazine)

#         # for i in range(len(m)):

#         # if r == m:
#         #     return True
#         print("m[:lr]: ", m[:lr])
#         if r == m[:lr]:
#             return True

# #         return False

# from collections import Counter
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         count_r=Counter(ransomNote)
#         count_m=Counter(magazine)
#         if count_r <= count_m:
#             return True
#         return False

if __name__ == "__main__":
    c = Solution()
    c.canConstruct("a", "b")
    c.canConstruct("aa", "ab")
    c.canConstruct("aa", "aab")