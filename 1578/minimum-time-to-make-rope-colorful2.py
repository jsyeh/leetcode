# LeetCode 1578. Minimum Time to Make Rope Colorful
# 要讓繩子上面的「氣球」變成 colorful 也就是「間隔的色彩都不同」
# 但移除「同色的氣球」時, 不同氣球的難度不同、neededTime[i]不同
# 相鄰「兩兩比較」，把小的抽掉，大的移到右邊，以便下一輪比較
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        N = len(colors)  # 陣列長度
        ans = 0
        for i in range(1, N): # 比對 colors[i-1] 及 colors[i]
            if colors[i-1]==colors[i]: # 每次有相同，就把小的刪掉
                ans += min(neededTime[i-1], neededTime[i])  # 拆掉簡單的氣球
                neededTime[i] = max(neededTime[i-1], neededTime[i]) 
                # (殘留的)大的值「移到右邊」以便下一輪繼續比賽
        return ans
