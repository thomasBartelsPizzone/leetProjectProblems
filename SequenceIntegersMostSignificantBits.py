from typing import List
from collections import defaultdict
class Solution:
    def significant_bits_distance(self, num):
        # print("num: ", num)
        # print(num.bit_length())
        # print(num.to_bytes())
        # print("{num:08b} : ", f"{num:08b}")
        # sig_bits = num & -num
        # print(num & -num)
        # print(sig_bits.bit_length())
        # print("{sig_bits:08b} : ", f"{sig_bits:08b}")
        # most_sig_bit = sig_bits.bit_length() - 1
        # print(most_sig_bit)
        # print("{most_sig_bit:08b} : ", f"{most_sig_bit:08b}")
        # print(most_sig_bit.bit_length())
        # least_sig_bit = 0
        # while sig_bits >> least_sig_bit != 0:
        #     least_sig_bit += 1
        # print(least_sig_bit)
        # return most_sig_bit - least_sig_bit
        num_b = f"{num:08b}"
        print("numb: ", num_b)
        print(num_b.strip("0"))
        num_b_s = num_b.strip("0")
        print("num_b_s: ", num_b_s)
        #
        # bit_dict = defaultdict(int)
        # soFar = ans = 0
        # bit_dict[0] = 1
        # return 4
        left = 0
        right = 0
        n = len(num_b_s)
        b_delta = -1
        cnt = 0
        while right < n:
            if num_b_s[right] == "1" and cnt == 1:
                r_l = right - left + 1
                b_delta = max(b_delta, r_l)
                left = right
                cnt -= 1
            elif num_b_s[right] == "1":
                cnt += 1
            right += 1
        print(b_delta)
        return b_delta


    #
    def k_significant_bits_sequence(self, L, k):

        # Create a list of tuples (distance, num1, num2) for each pair of integers
        # pairs = [(significant_bits_distance(num1, num2), num1, num2) for num1, num2 in zip(L[:-1], L[1:])]

        # dist = []
        dist_d = {}
        for n in L:
            dist_d[n] = self.significant_bits_distance(n)
            # dist.append((self.significant_bits_distance(n), n))

        sorted_dict = sorted(dist_d.items(), key=lambda x: x[1], reverse=True)
        # dist_d.sort(reverse=True)
        # sequences = [num for _, num in dist[:k]]
        sequences = [k for k, v in sorted_dict[:k]]
        return sequences

if __name__ == "__main__":
    c = Solution()
    print(c.k_significant_bits_sequence([130, 10, 5, 4, 12], 3))



# [(1, 52), (3, 86), (17, 35), (67, 68), (81, 47)]