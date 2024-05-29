class Solution:
    # def __init__(self):
        # self.pal_d = {}
    def longestPalindrome(self, s: str) -> str:
        """
        # Works but nested for, not DP
        pal_d = {}
        s_l = len(s)
        if len(s) > 0:
            # min_pal = 1
            # for l in s:
            #     pal_d[l] = 1
            for i in range(s_l):
                pal_d[s[i]] = 1
                # print("i: ", i)
                temp_st = s[i]
                for y in range(1, s_l - i):
                    j = i + y
                    # print("j: ", j)
                    # if i != j:
                    temp_st += s[j]
                    # print("temp: ", temp_st)
                    # pal_test = s[i:i+1]
                    # if s[i] == s[j]:
                    if len(temp_st) > 1:
                        if temp_st[0] == temp_st[-1]:
                            pal_d[temp_st] = self.pal_check(temp_st)
                        else:
                            # print("temp_st[0]:", temp_st[0]," & temp_st[-1]:", temp_st[-1])
                            pal_d[temp_st] = 0
                # print(pal_d)
                # print("\n")
            # print("pal dict: \n", pal_d)
            # max_pal = max(pal_d.values())
            # max_ret = max(max_pal, min_pal)
            # max_pal_list = [k for k, v in pal_d.items() if v == max(pal_d.values())]
            # if len(max_pal_list) > 1:
            #     max_pal_k = max_pal_list[0]
            # else:
            #     print("max_pal_list: ", max_pal_list)
            #     # max_pal = max_pal
        else:
            return ""
        # ans_str = [k for k, v in pal_d.items() if v == max(pal_d.values())][0]
        # print(ans_str)
        return [k for k, v in pal_d.items() if v == max(pal_d.values())][0] #ans_str


    def pal_check(self, ts):
        # # print("ts: ", ts)
        # if len(ts) == 1:
        #     return 1
        # else:
        ts_l = len(ts)
        ts_hl = ts_l // 2
        ts_1 = ts[:ts_hl]
        # print("ts_1: ", ts_1)
        if ts_l % 2 == 1 and ts_hl > 1:
            # ts_2 = ts[::-1][j]
            ts_2 = ts[ts_hl + 1:]
        elif ts_hl == 1:
            ts_2 = ts[-1]
        else:
            ts_2 = ts[ts_hl:]
        # print("ts_2: ", ts_2)
        if ts_1 == ts_2[::-1]:
            return ts_l
        else:
            return 0
        # return 0
        # elif ss[i] == ss[j]:
        #     print("ss[i:j]: ", ss[i:j])
        #     print("len: ", len(ss[i:j]))
        #     if i + 1 < j - 1:
        #         # return ((ss[j-1] - ss[i+1]) + 2)
        #         return len(ss[i:j])
        #     else:
        #         return 2
        # else:
        #     fwd = j - i+1
        #     bkwd = j-1 - i
        #     return max(fwd, bkwd)
    """
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
            # # while len(sub_s) > 2:
            #     self.longPalDP(sub_s)
            #     # if sub_s[0] == sub_s[-1]:
            #     #     idx_1 += 1
            #     #     idx_2 -= 1
            #     # else:
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
        # print("pal d?", self.pal_d)
        # return [k for k, v in self.pal_d.items() if v == max(self.pal_d.values())][0]

    def longPalDP(self, sub_s, i, j):
        # print(sub_s)
        if i == j:
            return 1
        if sub_s[i] == sub_s[j] and i + 1 == j:
            return 2
        if sub_s[i] == sub_s[j]:
            return self.longPalDP(sub_s, i + 1, j - 1) + 2
        # else:
        return self.max_(self.longPalDP(sub_s, i, j - 1)
                   , self.longPalDP(sub_s, i + 1, j))

    def max_(self, x, y):
        if x > y:
            return x
        return y

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

    # def longPalDP(self, sub_s, i, j):
    #     print("sub_s: ", sub_s)
    #     # if len(sub_s) == 1:
    #     if i == j:
    #         self.pal_d[sub_s] = 1
    #         return None
    #     # if len(sub_s) == 2 and sub_s[0] == sub_s[-1]:
    #     if sub_s[i] == sub_s[j] and i + 1 == j:
    #         self.pal_d[sub_s[i:j]] = 2
    #         return None
    #     if sub_s[i] == sub_s[j]:
    #         return self.longPalDP(sub_s[1:-1])
    #     self.longPalDP(sub_s[1:])
    #     self.longPalDP(sub_s[:-1])


    # def longPalDP(self, sub_s, idx_1, idx_2):
    #     print("sub_s: ", sub_s)
    #     print("idx_1: ", idx_1)
    #     print("idx_2: ", idx_2)
    #
    #     if idx_1 == idx_2:
    #         self.pal_d[sub_s] = 1
    #         return None
    #     # elif len(sub_s) == 2 and sub_s[idx_1] == sub_s[idx_2]:
    #     if sub_s[idx_1] == sub_s[idx_2] == 2 and idx_1 + 1 == idx_2:
    #         self.pal_d[sub_s] = 2
    #         return None
    #     if sub_s[idx_1] == sub_s[idx_2]:
    #         return self.longPalDP(sub_s, idx_1 + 1, idx_2 - 1)
    #     else:
    #         self.longPalDP(sub_s, idx_1, idx_2 - 1)
    #         self.longPalDP(sub_s, idx_1 + 1, idx_2)
    #     return None

if __name__ == "__main__":
    c = Solution()
    s = "civilwartestingwhetherthatnaptio" #noranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    # s = "abba"
    # s = "qabcdefgfedcbaeiakkkks"
    print(c.longestPalindrome(s))
    # print(c.pal_seq("abba"))