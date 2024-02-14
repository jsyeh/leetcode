# 不同色的房子，最遠離多遠？（別擔心，至少有2色）
# 最多100間房子，暴力算也不會太久。
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        N = len(colors)
        ans = 0
        for i in range(N): # 左手i
            for j in range(i+1, N): # 右手j
                # 色彩不同，且距離更遠
                if colors[i]!=colors[j] and j-i>ans:
                    ans = j-i # 就更新答案
        return ans
