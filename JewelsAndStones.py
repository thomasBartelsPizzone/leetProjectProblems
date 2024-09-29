class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cntr = 0
        #         # for s in stones:
        #         #     if s in jewels:
        #         #         jewels = jewels.replace(s, '', 1)
        #         #         cntr
        #         #         ansDict1 = {}
        #         ansDict1 = {}
        #         for s in stones:
        #             ansDict1[s] = ansDict1.get(s, 0) + 1
        #         for j in jewels:
        #             cntr += ansDict1.get(j, 0)
        for s in stones:
            if s in jewels:
                cntr += 1

        return cntr

#         j = list(jewels)
#         s = list(stones)

#         return len([x for x in s if x in j])


if __name__ == "__main__":
    c = Solution()
    c.numJewelsInStones("aA", "aAAbbbb")
    c.numJewelsInStones("z", "ZZ")