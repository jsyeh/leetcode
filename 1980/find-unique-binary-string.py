# 題目 input 是 n 個字串，長度也是n, 隨便找個長度也是n、但沒出現過的字串。
# n<=16, 對應 16 bit 的字串。隨便做個字串，看它有沒有在 nums 裡面即可
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums) # 先了解題目的 N：同時對應數量、字串長度

        def toStr(n:int)->str: # 能把任何整數，變成 binary 的字串
            ans = ''
            for i in range(N): # 剝皮法
                ans = str(n%2) + ans # 慢慢組出 binary 的字串
                n = n // 2 # 剝皮法
            return ans # binary 字串

        # 如果有 N 個字串，那試 N+1個數，一定會有一個是答案
        for i in range(N+1):
            now = toStr(i) # 把整數轉成 binary 字串
            if now not in nums: # 現在這個字串，如果沒有在 nums 裡
                return now # 太好了，題目就是要這個(不在nums裡的)東西

        
