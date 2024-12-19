# LeetCode 769. Max Chunks To Make Sorted
# 把 arr 分段斷開，分別sort() 再合起來，要是 sorted，問能分幾段
# 因為數字是 0..n-1 去排列，Hint 1 說前i項的最大值是i就合理
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        nowMax = 0
        ans = 0
        for i, now in enumerate(arr):
            nowMax = max(nowMax, now)
            if nowMax==i:  # 太好了，符合「最大值」就是i
                ans += 1  # 代表「切在這裡」是合理的。
                # 因為切了之後，排序，再接起來，是sorted
        return ans
