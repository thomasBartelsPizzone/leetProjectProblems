class Solution:
    def __init__(self):
        self.roman_dict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    def roman_update(self, power, rem_num, r_str) -> (int, str):
        # roman_dict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        rom_num = self.roman_dict[power]
        r_str += rom_num
        rem_num -= power
        return rem_num, r_str

    def intToRoman(self, num: int) -> str:
        # roman_dict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        if num in self.roman_dict.keys():
            return str(self.roman_dict[num])
        consec_check_ixcm = 0
        consec_check_vld = 0
        temp_num = num
        new_str = ""
        while temp_num > 0:
            if str(temp_num)[0] != "4" and str(temp_num)[0] != "9":
                if temp_num >= 1000:
                    # # if consec_check_ixcm <= 3:
                    # new_str += "M"
                    # # consec_check_ixcm += 1
                    # temp_num -= 1000
                    temp_num, new_str = self.roman_update(1000, temp_num, new_str)
                    # if temp_num < 1000:
                    #     consec_check_ixcm = 0
                    # else:
                    #     if new_str[-3:] == "MMM":
                elif temp_num >= 500:
                    # # if consec_check_vld < 1:
                    # new_str += "D"
                    # # consec_check_vld += 1
                    # temp_num -= 500
                    temp_num, new_str = self.roman_update(500, temp_num, new_str)
                    # if temp_num < 500:
                    #     consec_check_vld = 0
                    # else:
                    #     if new_str[-3:] == "DDD":
                elif temp_num >= 100:
                    if consec_check_ixcm <= 3:
                        # new_str += "C"
                        # consec_check_ixcm += 1
                        # temp_num -= 100
                        temp_num, new_str = self.roman_update(100, temp_num, new_str)
                        if temp_num < 100:
                            consec_check_ixcm = 0
                    else:
                        if new_str[-3:] == "CCC":
                            new_str = new_str[:-3] + "CD"
                            temp_num -= 100
                elif temp_num >= 50:
                    # # if consec_check_vld < 1:
                    # new_str += "L"
                    # # consec_check_vld += 1
                    # temp_num -= 50
                    # # if temp_num < 50:
                    # #     consec_check_vld = 0
                    temp_num, new_str = self.roman_update(50, temp_num, new_str)
                elif temp_num >= 10:
                    if consec_check_ixcm <= 3:
                        # new_str += "X"
                        # consec_check_ixcm += 1
                        # temp_num -= 10
                        temp_num, new_str = self.roman_update(10, temp_num, new_str)
                        consec_check_ixcm += 1
                        if temp_num < 10:
                            consec_check_ixcm = 0
                    else:
                        if new_str[-3:] == "XXX":
                            new_str = new_str[:-3] + "XL"
                            temp_num -= 10
                elif temp_num >= 5:
                    # new_str += "V"
                    # temp_num -= 5
                    temp_num, new_str = self.roman_update(5, temp_num, new_str)
                elif temp_num >= 1:
                    if consec_check_ixcm <= 3:
                        # new_str += "I"
                        # consec_check_ixcm += 1
                        # temp_num -= 1
                        temp_num, new_str = self.roman_update(1, temp_num, new_str)
                        consec_check_ixcm += 1
                        if temp_num < 1:
                            consec_check_ixcm = 0
                    else:
                        if new_str[-3:] == "III":
                            new_str = new_str[:-3] + "IV"
                            temp_num -= 1
            else:
                if temp_num >= 500:
                    new_str += "CM"
                    temp_num -= 900
                elif temp_num >= 100:
                    new_str += "CD"
                    temp_num -= 400
                elif temp_num >= 50:
                    new_str += "XC"
                    temp_num -= 90
                elif temp_num >= 10:
                    new_str += "XL"
                    temp_num -= 40
                elif temp_num >= 5:
                    new_str += "IX"
                    temp_num -= 9
                elif temp_num >= 1:
                    new_str += "IV"
                    temp_num -= 4

        return new_str


if __name__ == "__main__":
    c = Solution()
    print(c.intToRoman(78))
    print(c.intToRoman(3749))
    print(c.intToRoman(1994))
