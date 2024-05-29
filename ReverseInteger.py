class Solution:
    def range32(self, y: int):
        if -2**31 <= y and y <= 2**31 - 1:
            return y
        else:
            return 0

    def reverse(self, x: int) -> int:
        if x > 0:
            x_str = str(x)
            new_int = int(x_str[::-1])
            # ctr = 0
            # while x_str:
            #     new_int += int(x_str[0]) * 10**ctr
            #     print("new int: ", new_int)
            #     x_str = x_str[1:]
            #     ctr += 1
            # print("new_int: ", new_int)
            # return new_int
            return self.range32(new_int)
        elif x < 0:
            print("less than 0")
            x_str = str(x)[1:]
            new_int = int(x_str[::-1])
            # ctr = 0
            # while x_str:
            #     new_int += int(x_str[0]) * 10**ctr
            #     print("new int: ", new_int)
            #     x_str = x_str[1:]
            #     ctr += 1
            print("new_int: ", new_int)
            # return new_int * -1
            return self.range32(new_int * -1)
        else:
            return 0

if __name__ == "__main__":
    c = Solution()
    print(c.reverse(132))
    print(c.reverse(-132))
    # print(c.reverse(1))
    # print(c.reverse(49299))
    # print(c.reverse(-2))
    # print(c.reverse(-9132))
