class Solution:
    def range32(self, y: int):
        if -2**31 <= y and y <= 2**31 - 1:
            return y
        else:
            if -2**31 >= y:
                return -2**31
            if y >= 2**31 - 1:
                return 2**31 - 1

    def myAtoi(self, s: str) -> int:
        if len(s) > 0:
            # if s[0] == "0":
            #     return 0
            # non_w_str = s.replace(" ", "")
            # sign_flag = 1
            # if non_w_str[0] == ["-"]:
            #     print("a neg")
            #     sign_flag = -1
            #     non_w_str = non_w_str[1:]
            # if non_w_str[0] == ["0"]:
            #     if len(non_w_str) > 1 and non_w_str[1] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            #         non_w_str = non_w_str[1:]
            sign_flag = 1
            final_flag = False
            non_w_str = s
            new_str = ""
            # zero_check = False
            while non_w_str:
                # print("new str: ", new_str)
                # print("leftover str: ", non_w_str)
                if non_w_str[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    if non_w_str[0] == "0" and final_flag:
                        new_str += non_w_str[0]
                        non_w_str = non_w_str[1:]
                        continue
                    elif non_w_str[0] == "0":
                        non_w_str = non_w_str[1:]
                        final_flag = True
                        # zero_check = True
                        continue
                    new_str += non_w_str[0]
                    non_w_str = non_w_str[1:]
                    final_flag = True
                    continue
                else:
                    if final_flag:
                        break
                    if non_w_str[0] == " ":
                        non_w_str = non_w_str[1:]
                        continue
                    if non_w_str[0] == "+":
                        non_w_str = non_w_str[1:]
                        final_flag = True
                        continue
                    if non_w_str[0] == "-":
                        sign_flag = -1
                        non_w_str = non_w_str[1:]
                        final_flag = True
                        continue
                    # if non_w_str[0] == "0":
                    #     non_w_str = non_w_str[1:]
                    #     continue
                    else:
                        # print("i don't know why but this is neg")
                        # print("str: ", non_w_str)
                        # print("str[0]: ", non_w_str[0])
                        break
            if len(new_str) > 0:
                print("without limit check: ", int(new_str) * sign_flag)
                return self.range32(int(new_str) * sign_flag)
            # elif zero_check:
            #     return 0
            else:
                return 0
        return 0

if __name__ == "__main__":
    c = Solution()
    print(c.myAtoi("000000000000000000000000000011"))
    print(c.myAtoi("21474836460"))
    print(c.myAtoi("   -042"))
    print(c.myAtoi("+-12"))
    print(c.myAtoi("1337c0d3"))
    print(c.myAtoi("0-1"))
