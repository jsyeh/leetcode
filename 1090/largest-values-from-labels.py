# 有 N 個標籤 及對應的 N 個 value值，
# 在裡面挑一些東西，不能挑超過 numWanted 個
# 相同 label 的東西 最多只能挑 userLimit 個，找最高的 score
# 像 greedy 題目，就value從大到小挑，但若label用超過，就不挑它
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        N = len(values)
        items = [(values[i],labels[i]) for i in range(N)]
        items.sort(reverse=True) # 照 values[i] 大到小排序
        used = defaultdict(int) # 使用的個數
        ans = 0
        for i in range(N): # 再逐一取出
            value, label = items[i]
            if used[label]<useLimit: # 用量還沒超過
                ans += value
                used[label] += 1 # label類增加一個
                numWanted -= 1 # 用掉1個，剩下變少了
            if numWanted == 0: # 取完要取的數目
                break # 就可以離開了
        return ans
