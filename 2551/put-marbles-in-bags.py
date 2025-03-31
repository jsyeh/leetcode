# LeetCode 2551. Put Marbles in Bags
# 不同重量的彈珠 weights[i] 分到 k 袋子裡，每袋裝 weights[i]...weights[j] 範圍的彈珠
# 每袋分數是「頭+尾」，問 k 袋分數加起來的「最大分數] 減「最小分數」
# 解題：「頭+尾」+「頭+尾」+「頭+尾」+「頭+尾」+...+「頭+尾」
#    第0筆+「尾+頭」+「尾+頭」+「尾+頭」+「尾+頭」+...+ 最後一筆
# 所以「兩兩相鄰」的 weights 就是「待加」的候選人，把它們排序
# 「最大分數] 減「最小分數」，就是「最大k-1筆」減「最小k-1筆」，就是答案
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # 在 Case 94/103 遇到問題 k 是 1 時，答案放0即可
        if k==1: return 0
        candidates = []  # 「兩兩相鄰」的 weights 就是「尾+頭」的「待加」候選人
        for i in range(len(weights)-1):
            candidates.append(weights[i]+weights[i+1])
        candidates.sort()  # 小到大排好
        small = sum(candidates[:k-1])  # 最小k-1筆加起來
        large = sum(candidates[-k+1:])  # 最大k-1筆加起來
        return large - small
