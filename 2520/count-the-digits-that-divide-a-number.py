# 想知道 1248 裡, 有幾個位數可整除 1248 (答案是4個,分別是1,2,4,8)
# 想知道 121 裡, 有幾個位數可以整除 121 (答案是2個1)
class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        for c in str(num): # 先轉成字串, 再把每一位數取出來
            if num%int(c)==0: ans += 1 # 可整除
        return ans
