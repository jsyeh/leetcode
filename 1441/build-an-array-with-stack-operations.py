# 題目理解後，好像很簡單，很像模擬題
# 就target有一堆數字，是stack的內容，1,2,3,...,n 是 input
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        targetN = len(target)
        ans = []
        i = 0 # target[i] vs. i
        for k in range(1,n+1):
            ans.append('Push') # 數字k依序推入stack
            if k != target[i]: # 但 k 不屬於 target
                ans.append('Pop') # 就要 pop 出去
            else: # 如果屬於 target
                i += 1 # 就往下個數字前進
            if k == target[-1]: # 若已到達最後的數字
                return ans # 就結束，並回傳答案

        return ans # 這行應該可以不用寫，因前面應已 return
        
