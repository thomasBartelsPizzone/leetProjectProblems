class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Faster
        new_str = ""
        # no_rpt = []
        longest = {}
        # idx_dict = {}
        # max_l = 0
        if len(s) > 0:
            for idx, l in enumerate(s):
                if l not in new_str:
                    new_str += l
                    longest[new_str] = len(new_str)
                    # idx_dict[l] = idx
                    # if len(new_str) > max_l:
                    #     max_l = len(new_str)
                else:
                    if new_str[-1] == l:
                        new_str = l
                    else:
                        l_idx = new_str.index(l)
                        new_str = new_str[l_idx + 1:] + l
                        longest[new_str] = len(new_str)
            return max(longest.values())
        else:
            return 0
    """
        # Works, slow
        no_rpt = []
        longest = {}
        idx_dict = {}
        if len(s) > 0:
            for idx, l in enumerate(s):
                if l not in no_rpt:
                    # idx_dict[l] = idx
                    no_rpt.append(l)
                    longest[str(no_rpt)] = len(no_rpt)
                    idx_dict[l] = idx
                else:
                    # no_rpt = [l]
                    # l_idx = len(no_rpt) - 1
                    # print("l_idx: ", l_idx)
                    # if no_rpt[l_idx] == l:
                    if no_rpt[-1] == l:
                        no_rpt = [l]
                    else:
                        # l_idx = idx_dict[l]
                        l_idx = no_rpt.index(l)
                        # print("L is ", l)
                        # print("L's idx is ", idx_dict[l])
                        # print("norpt[idx] : ", no_rpt[l_idx])
                        # print("norpt[idx+1] : ", no_rpt[l_idx + 1])
                        no_rpt[:] = no_rpt[l_idx + 1:] + [l]
                        # no_rpt[:] = no_rpt[l_idx:] + [l]
                        longest[str(no_rpt)] = len(no_rpt)
                # print("idx_dict\n", idx_dict)
                # print("no_rpt\n", no_rpt)
                # print(longest)
            # if longest.values():
            #     return max(longest.values())
            # else:
            #     return 1
            return max(longest.values())
        else:
            return 0
        """

if __name__ == "__main__":
    c = Solution()
    print(c.lengthOfLongestSubstring("curhauckfownvbdskwjfow"))