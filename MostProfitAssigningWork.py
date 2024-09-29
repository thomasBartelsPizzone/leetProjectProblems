from typing import List
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        w_sum = 0
        # print(max(worker))
        max_d = max(difficulty)
        min_d = min(difficulty)
        max_p = max(profit)
        min_p = min(profit)
        if max(worker) < min(difficulty):
            return w_sum
        # tuple list for profit and difficulty
        p_d = sorted(list(zip(profit, difficulty)), key=lambda x: x[0])
        print(p_d)
        # sorted(p_d, key=lambda x: x[0])
        # print(p_d)
        #
        len_d = len(difficulty)
        w_sum_dict = {}
        for w in worker:
            print("w: ", w)
            max_w_sum = 0
            # visit_diff = []
            if w >= max_d:
                # max_w_sum = profit[-1]
                max_w_sum = max_p
                print("max_w_sum: ", max_w_sum)
                # w_sum_dict[w] = max_w_sum
            # elif w == min_d:
            #     max_w_sum = min_p
            #     print("max_w_sum: ", max_w_sum)
            elif w < min_d:
                max_w_sum = 0
                print("max_w_sum: ", max_w_sum)
                # w_sum_dict[w] = max_w_sum
            else: # w >= min(difficulty):
                # _idx = len_d // 2
                _idx = len_d - 1
                print("b4 while idx: ", _idx)
                # while _idx >= 0 and _idx < len_d:
                while _idx >= 0:
                    print("idx: ", _idx)
                    test_d = p_d[_idx][1]
                    print("test diff: ", test_d)
                    print("test prof: ", p_d[_idx][0])
                    if w >= test_d:
                        # test_p = profit[_idx]
                        # test_p = p_d[_idx][0]
                        # w_sum += p_d[_idx][0]
                        max_w_sum = p_d[_idx][0]
                        break
                        # w_sum_dict[w] = p_d[_idx][0]
                    _idx -= 1
                        # if test_p > max_w_sum:
                        #     max_w_sum = test_p
                        #     w_sum_dict[w] = test_p
                        # if test_p >= max_p:
                        #     break
                            # _idx += 1
                    # if cntr > 0 and def_test_d == test_d:
                    # if incr_check and decr_check:
                    # if test_d in visit_diff:
                    #     break
                    # if w == test_d:
                    #     test_p = profit[_idx]
                    #     print("test prof: ", test_p)
                    #     if test_p > max_w_sum:
                    #         max_w_sum = test_p
                    #     break
                    # elif w > test_d:
                    #     test_p = profit[_idx]
                    #     if test_p > max_w_sum:
                    #         max_w_sum = test_p
                    #     _idx += 1
                    #     # decr_check = True
                    # else:
                    #     _idx -= 1
                        # incr_check = True
                    # cntr += 1
                    # visit_diff.append(test_d)
                    # else:
                    #     w_sum_dict[w] = 0
                    # _idx += 1
            w_sum += max_w_sum
            # w_sum += max_w_sum
        # print("w_sum_dict: ", w_sum_dict)
        return w_sum

if __name__ == "__main__":
    c = Solution()
    # print(c.maxProfitAssignment([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]))
    # print(c.maxProfitAssignment([85, 47, 57], [24, 66, 99], [40, 25, 25]))
    # print(c.maxProfitAssignment([68, 35, 52, 47, 86], [67, 17, 1, 81, 3], [92, 10, 85, 84, 82]))
    print(c.maxProfitAssignment([13, 37, 58], [4, 90, 96], [34, 73, 45]))



# [(1, 52), (3, 86), (17, 35), (67, 68), (81, 47)]