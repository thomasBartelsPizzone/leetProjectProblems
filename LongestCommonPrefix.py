from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_str = ""
        # if l_strs == 1:
        #     if strs[0] == "":
        #         return ""
        #     else:
        #         return strs[0]
        for i in range(len(strs[0])):
            # for j in range(1, len(strs)):
            for j in strs[1:]:
                # if strs[0][:i+1] == strs[j][:i+1]:
                # if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                if i >= len(j) or strs[0][i] != j[i]:
                    # print("strs[j][:i]: ", strs[j][:i])
                    return max_str
            max_str += strs[0][i]
        return max_str


    """
        def longestCommonPrefix(self, strs: List[str]) -> str:
        # common_dict = {}
        max_str = ""
        max_len = 0
        l_strs = len(strs)
        if l_strs == 1:
            if strs[0] == "":
                return ""
            else:
                return strs[0]
        fw = strs[0]
        if len(fw) == 0:
            return max_str
        for i in range(len(fw)):
            # print("fw[:i]: ", fw[:i+1])
            # max_len = len(fw[i])
            match_cnt = 0
            for j in range(1, len(strs)):
                # print("strs[j][:i+1]: ", strs[j][:i+1])
                if fw[:i+1] == strs[j][:i+1]:
                    # print("strs[j][:i]: ", strs[j][:i])
                    match_cnt += 1
            # print("match count? ", match_cnt)
            if match_cnt == l_strs - 1:
                max_len = len(fw[:i+1])
        # print("here: ", fw[:max_len])
        return fw[:max_len]
    """
    """
            common_dict = {}
        max_str = ""
        max_len = 0
        l_strs = len(strs)
        if l_strs == 1:
            if strs[0] == "":
                return ""
            else:
                return strs[0]
        else:
            fw = strs[0]
            if len(fw) == 0:
                return max_str
            while fw:
                common_dict[fw] = 0
                fw = fw[:-1]
            print("what is the dict: ", common_dict)
            for i in range(l_strs):
                nw = strs[i]
                print("nw: ", nw)
                if i > 0:
                    while nw:
                        if nw in common_dict:
                            if common_dict[nw] == 0:
                                common_dict[nw] += 2
                            else:
                                common_dict[nw] += 1
                            if len(nw) > max_len:
                                max_len = len(nw)
                        nw = nw[:-1]
            print("what was the dict: ", common_dict)
        max_common = max(common_dict.values())
        if max_len > 0 and max_common == l_strs:
            # ks = [k for k, v in common_dict.items() if (v == max(common_dict.values()) and v == max_len)]
            # return ks[0]
            return [k for k, v in common_dict.items() if v == max_common][0]
        else:
            return max_str
    """

if __name__ == "__main__":
    c = Solution()
    print(c.longestCommonPrefix(["flower","flow","flight"]))
    print(c.longestCommonPrefix(["dog","racecar","car"]))
    print(c.longestCommonPrefix(["flower", "flower", "flower", "flower"]))
