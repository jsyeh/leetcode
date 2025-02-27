# LeetCode 873. Length of Longest Fibonacci Subsequence
# x[i] + x[i+1] == x[i+2] 符合 Fibonacci 性質
# 如果 arr 裡挑些數「符合」性質，問「最長」能有多長？
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        ans = 0
        exist = set(arr)  # 有哪些數字，存在 arr 裡
        for i in range(len(arr)):  # 兩層迴圈，暴力試 左手a 右手b 兩數
            for j in range(i+1, len(arr)):
                a, b, length = arr[i], arr[j], 2
                # 利用迴圈，暴力試a,b兩數，「能長出多長的數列」
                while a+b in exist:  # 若存在「相加」的數，可試著「繼續試下一個數」
                    a, b, length = b, a+b, length+1  # 長度越試越長
                ans = max(ans, length)
        if ans <= 2: return 0  # 如果答案只有 2個數，就還稱不上答案
        return ans
