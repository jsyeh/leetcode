# 要讓繩子上面的「氣球」變成 colorful 也就是「間隔的色彩都要不同」
# 因為只能 remove 同色的氣球。不過每個氣球 neededTime[i] 不同
# 相鄰「兩兩比較」，把小的抽掉，大的移到右邊，以便下一輪比較
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        N = len(colors)
        # 相鄰「兩兩比較」，把小的抽掉，大的移到右邊，以便下一輪比較
        ans = 0
        for i in range(N-1): # 比對 colors[i] 及 colors[i+1]
            if colors[i]==colors[i+1]: # 每次有相同，就把小的刪掉
                if neededTime[i]<neededTime[i+1]: 
                    ans += neededTime[i] # 左邊把小的抽掉
                else: # 左邊大，要插掉小的，並把大的放到右邊，下輪可比
                    ans += neededTime[i+1]
                    neededTime[i+1] = neededTime[i]
        return ans
