# LeetCode 757. Set Intersection Size At Least Two
# intervals 陣列裡，有許多[開始,結束]範圍內的數。
# 請變出 intersection set 裡面能讓「每個範圍」都至少有2個數在裡面。
# 找出最小的 intersection set。以下解法，是用 2018 年 Renpeng Fang 的解法
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1],-x[0]))  
        # b 越來越大，b同時 a越來越小

        ans = 0  # intersection set 裡，累積要放幾個？
        largest = second = -1  # intersection set 裡的最大、次大的數，初始值-1會無效
        for a,b in intervals: # 從 [a,b]的範圍，已排序，b會越來越大
            is_largest_in = (a <= largest)  # largest 在 [a,b]內
            is_second_in = (a <= second)  # second 在 [a,b]內
            if is_largest_in and is_second_in:  # 已有2個，很好
                continue  # [a,b] 已有2個已在 intersection set，換下一筆

            if is_largest_in:  # 運氣好，largest 已在 [a,b]裡，但 second不在
                ans += 1  # 要再補新的 largest，就用最大的 b 吧！
                largest, second = b, largest  # 回收，讓舊的 largest 變成 second
            else:  # 運氣不好，都不在 [a,b] 裡
                ans += 2  # 要補2個
                largest, second = b, b-1
        return ans
