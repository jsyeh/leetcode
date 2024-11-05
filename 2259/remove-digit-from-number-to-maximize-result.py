# LeetCode 2259. Remove Digit From Number to Maximize Result
# 在 number 裡，要刪掉1個 digit，問刪完後「最大的數」是什麼
# 其實就看看「刪掉之後」的數，誰比較大。
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = ""  # 最大的數
        for i in range(len(number)):  # 逐個字母分析
            if number[i]==digit:  # 若是可以刪掉的數
                if number[:i] + number[i+1:] > ans:
                    ans = number[:i] + number[i+1:] 
        return ans
