# 只有兩個籃子，可採2種水果，要連續採收，籃子同種水果可裝很多
# 因為陣列很長，不能用暴力法去算
# 可試試 sliding window 的作法, 不過我這裡是考 lee215 的另一種作法
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        a, b = 0, 0 # 前面是a,後面是b 
        bN = 0 # 後面的b連續的個數
        ans, cur = 0, 0 # 最後答案，目前答案
        # for i in range(1,N):
        for now in fruits: # 逐項拿出水果來檢查
            if now==b: # 和右邊項相同，b繼續連續，就是變長的意思
                cur += 1 # 目前答案變長
                bN += 1 # b 的數目變多，連續的b有幾個
            elif now==a: # 和左邊項相同，左右要交換
                cur += 1 # 答案還是會變長
                a, b = b, a # 左右要交換
                bN = 1 # b重新從1開始，連續的b有幾個
            else: # now 不是 a 也不是 b, 要把 a 淘汰掉
                cur = bN + 1 # 把 連續的b的長度，加now這1個
                a, b = b, now # 要更新 a,b 項
                bN = 1 # b重新從1開始，連續的b有幾個
            ans = max(ans, cur)
        return ans

