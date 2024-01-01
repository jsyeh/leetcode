# 要找到「最小」 距離 的 pair
# 若答案很多組，就每組都放進來
# 一樣先排序，之後巡一次，找「最小」距離
# 再巡第二次，把答案都排進來 （因每個數字都不同，不用擔心重覆的問題）
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        N = len(arr)
        arr.sort()
        ansMin = arr[-1] - arr[0] # 先放最大的距離
        for i in range(N-1):
            ansMin = min(ansMin, arr[i+1]-arr[i])
        # 找到 ansMin 後，再巡第二之，哪些 pair 符合 ansMin
        ans = []
        for i in range(N-1):
            if arr[i+1]-arr[i]==ansMin: # 符合的話
                ans.append([arr[i],arr[i+1]])
        return ans
