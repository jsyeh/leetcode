# 希望 'L' 'R' 一樣多的 balanced string
# 切越多越好 
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        L, R = 0, 0
        ans = 0
        for c in s:
            if c=='L': L += 1
            else: R += 1

            if L==R: # 每次加完，就檢查是否相同
                ans += 1 # 相同就+1
                L, R = 0, 0 # 並且都清空
        return ans
