class Solution:
    # word have been faster just to check if
    # roman_dict[s[i]] <= roman_dict[s[i-1]]
    # (bigger number earlier unless subtractive IX = 9
    # then remove it twice (bc you already added the I, need to remove it from subtractive and the running total
    # sum_r += roman_dict[s[i]] - 2 * roman_dict[2[i-1]]
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1,"V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum_r = 0
        if len(s) == 0:
            return sum_r
        elif len(s) == 1:
            return roman_dict[s[0]]
        while s:
            if len(s) > 1:
                if s[0] == "I" and s[1] == "V":
                    sum_r += 4
                    s = s[2:]
                elif s[0] == "I" and s[1] == "X":
                    sum_r += 9
                    s = s[2:]
                elif s[0] == "X" and s[1] == "L":
                    sum_r += 40
                    s = s[2:]
                elif s[0] == "X" and s[1] == "C":
                    sum_r += 90
                    s = s[2:]
                elif s[0] == "C" and s[1] == "D":
                    sum_r += 400
                    s = s[2:]
                elif s[0] == "C" and s[1] == "M":
                    sum_r += 900
                    s = s[2:]
                else:
                    sum_r += roman_dict[s[0]]
                    s = s[1:]
            else:
                # try:
                sum_r += roman_dict[s[0]]
                s = s[1:]
                # except Exception as e:
                #     print("sum failed with dict key: ", e)
        return sum_r

    """
    def __init__(self):
        self.roman_dict = {"I": 1,"V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    def romanToInt(self, s: str) -> int:
        sum_r = 0
        if len(s) == 0:
            return sum_r
        if len(s) == 1:
            return self.roman_dict[s[0]]
        while s:
            if s[0] == "I":
                if len(s) > 1 and s[1] == "V":
                    sum_r += 4
                    s = s[2:]
                elif len(s) > 1 and s[1] == "X":
                    sum_r += 9
                    s = s[2:]
                else:
                    sum_r += self.roman_dict[s[0]]
                    s = s[1:]
            elif s[0] == "X":
                if len(s) > 1 and s[1] == "L":                
                    sum_r += 40
                    s = s[2:]
                elif len(s) > 1 and s[1] == "C":                
                    sum_r += 90
                    s = s[2:]
                else:
                    sum_r += self.roman_dict[s[0]]
                    s = s[1:]
            elif s[0] == "C":
                if len(s) > 1 and s[1] == "D":                
                    sum_r += 400
                    s = s[2:]
                elif len(s) > 1 and s[1] == "M":                
                    sum_r += 900
                    s = s[2:]
                else:
                    sum_r += self.roman_dict[s[0]]
                    s = s[1:]
            else:
                # try:
                sum_r += self.roman_dict[s[0]]
                s = s[1:]
                # except Exception as e:
                #     print("sum failed with dict key: ", e)
        return sum_r
        """