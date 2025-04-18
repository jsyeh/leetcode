# LeetCode 38. Count and Say
# 數字連續出現, 就模依RLE方法「壓縮」成「數字+字母」的形式
class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1: return '1'  # 可利用「函式呼叫函式」來解這題
        prev = self.countAndSay(n-1)  # 把大問題變小問題
        ans = ''
        prevN, prevC = 1, prev[0]
        for i in range(1,len(prev)): 
            c = prev[i]
            if c==prevC:
                prevN += 1
            else:
                ans += str(prevN) +  prevC
                prevC = c
                prevN = 1
        if prevN>0: ans += str(prevN) + prevC
        return ans  # 看結果, 好像沒有壓縮效果
