# k-beauty： 若長度為k 且可整除 num，且是 str(num)的子字串
# 請問有幾個 k-beauty 字串？
# 所以，把 num 做因式分解。或把 num變字串，再逐一往右走下去
# （可參考 Example 2的解釋
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num) # 先變字串
        ans = 0
        for i in range(len(s)-k+1): # 再逐格切看看
            now = int(s[i:i+k]) # 現在切出 now 數字
            
            # now 不能是 0 才能做除法
            if now!=0 and num % int(s[i:i+k]) == 0:
                ans += 1
        return ans
