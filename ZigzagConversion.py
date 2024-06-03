class Solution:
    #Zig zag -> down then up at 45deg

    """
    # attempt 1
    def convert(self, s: str, numRows: int) -> str:
        new_str = ""
        down_flag = True
        s_len = len(s)
        word_set = {}
        flag_count = 0
        while s:
            # print("flag_count: ", flag_count)
            if flag_count < numRows and flag_count > 0:
                if flag_count in word_set.keys():
                    word_set[flag_count] += [s[0]]
                else:
                    word_set[flag_count] = [s[0]]
                if down_flag:
                    flag_count += 1
                else:
                    flag_count -= 1
                s = s[1:]
            elif flag_count == 0:
                if flag_count in word_set.keys():
                    word_set[flag_count] += [s[0]]
                else:
                    word_set[flag_count] = [s[0]]
                flag_count += 1
                down_flag = True
                s = s[1:]
            else:
                down_flag = not down_flag
                if flag_count <= 0:
                    flag_count += 1
                else:
                    flag_count -= 2
            # print("dict: ", word_set)
        print("dict: ", word_set)
        for k in word_set.keys():
            new_str += "".join(word_set[k])
        return new_str
        """
    # attempt2: use row count as index of for loop
    def convert(self, s: str, numRows: int) -> str:
        new_str = ""
        s_len = len(s)
        if len(s) <= 1 or numRows == 1:
            return s
        col_diff = numRows + 1 + (numRows - 3)
        idx = 0
        diag_idx = 0
        for i in range(numRows):
            idx = i
            while idx < s_len:
                new_str += s[idx]
                if i != 0 and i != numRows - 1:
                    diag_idx = idx + col_diff - 2 * i
                    if diag_idx < s_len:
                        new_str += s[diag_idx]

                idx += col_diff
        return new_str
if __name__ == "__main__":
    c = Solution()

    print(c.convert("PAYPALISHIRING", 3))
    print(c.convert("PAYPALISHIRING", 4))
    print(c.convert("A", 1))

    #if 0: [0, 4, 8, 12]
    #if 1: [1, 3, 5, 7, 9, 11, 13]
    #if 2: [2, 6, 10]

    #if 0: [0, 6, 12]
    #if 1: [1, 5, 7, 11, 13]
    #if 2: [2, 4, 8, 10]
    #if 3: [3, 6, 9]

    #[0][1] = 0 + numRows + 1 + (numRows - 3) = 8
    #[1][1] = 1 + numRows + 1 + (numRows - 3) = 8
    # 0: 0	8
    # 1: 1	7	9
    # 2: 2	6	10
    # 3: 3	5	11	13
    # 4: 4	12