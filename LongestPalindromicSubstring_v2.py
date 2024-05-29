class Solution:
    # def __init__(self):
        # self.pal_d = {}
    def longestPalindrome(self, s: str) -> str:
        s_l = len(s)
        if len(s) > 0:
            # for l in s:
            #     self.pal_d[l] = 1
            # self.longPalDP(s)
            # sub_s = s
            if self.pal_check(s):
                return s
            idx_1 = 0
            idx_2 = s_l - 1
            max_l = self.longPalDP(s, idx_1, idx_2)
            print("max_l: ", max_l)
            # print(s_l - max_l)
            for i in range(0, s_l - max_l):
                # print(s[i])
                # print(s[i+max_l-1])
                # print("loop?")
                if s[i] == s[i+max_l-1]:
                    print(s[i])
                    print(s[i+max_l-1])
                    sol_pal = s[i:i+max_l]
                    if self.pal_check(sol_pal):
                        return sol_pal
            return s[0]
                # else:
                #     print("check: \n", s[i],"\n", s[i+max_l])
        else:
            return ""

    def longPalDP(self, sub_s, i, j):
        # print(sub_s)
        if i == j:
            return 1
        if sub_s[i] == sub_s[j] and i + 1 == j:
            return 2
        if sub_s[i] == sub_s[j]:
            return self.longPalDP(sub_s, i + 1, j - 1) + 2
        # else:
        return max(self.longPalDP(sub_s, i, j - 1)
                   , self.longPalDP(sub_s, i + 1, j))

    def pal_check(self, ts):
        ts_l = len(ts)
        ts_hl = ts_l // 2
        ts_1 = ts[:ts_hl]
        if ts_l % 2 == 1 and ts_hl > 1:
            ts_2 = ts[ts_hl + 1:]
        elif ts_hl == 1:
            ts_2 = ts[-1]
        else:
            ts_2 = ts[ts_hl:]
        if ts_1 == ts_2[::-1]:
            return True
        else:
            return False

if __name__ == "__main__":
    c = Solution()
    s = "civilwartestingwhetherthatnaptio" #noranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    # s = "abba"
    # s = "qabcdefgfedcbaeiakkkks"
    print(c.longestPalindrome(s))
    # print(c.pal_seq("abba"))