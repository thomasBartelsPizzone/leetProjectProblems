class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        #     return False
        x_str = str(x)
        # len_x = len(x_str)
        # # even_check := True if len_x %2 == 0 else even_check := False
        # if len_x %2 == 0:
        #     even_check = True
        # else:
        #     even_check = False
        # # print("x_str[:len_x//2]: ", x_str[:len_x//2])
        # # print("x_str[len_x//2:]: ", x_str[len_x//2:])
        # if even_check:
        #     return True if x_str[:len_x//2] == x_str[len_x//2:][::-1] else False
        # else:
        #     return True if x_str[:len_x//2] == x_str[len_x//2 + 1:][::-1] else False
        return x_str == x_str[::-1]

if __name__ == "__main__":
    c = Solution()
    print(c.isPalindrome(121))
    print(c.isPalindrome(-121))
    print(c.isPalindrome(10))