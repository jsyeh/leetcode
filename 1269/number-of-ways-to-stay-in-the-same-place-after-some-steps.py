# 題目雖然是 Hard，但應該算簡單：要在 steps步之後，還留在 index 0 的走法
# 看起來就典型的 Dynamic Programming 可以解。記得要 % 1000000007 。
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def helper(pos, remain)->int:
            # 你在 pos 這個位置，還剩 remain 步要走，有幾種走法
            if remain==0: # 走完了
                if pos == 0: return 1 # 走到目的地0，剛好沒剩步，太好了
                else: return 0 # 你沒有到達目的地0，失敗了
            
            # 如果是留在原地
            ans = helper(pos, remain-1) # 耗掉一步，沒問題

            # 如果能往左移
            if pos>0: ans += helper(pos-1, remain-1) # 耗掉一步，沒問題

            # 如果能往右移
            if pos<arrLen-1: ans += helper(pos+1, remain-1) # 耗掉一步
            
            return ans % 1000000007
        
        return helper(0, steps)
        
