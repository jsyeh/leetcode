# LeetCode 1007. Minimum Domino Rotations For Equal Row
# 每個骨牌有上下兩個點數。一整排骨牌，挑1些旋轉後，有一整列(tops或bottoms)都相同
# 如果能達成任務, 表示「上、下」一定會有一個是「共同」的數，先找出來，便能用迴圈解出答案
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        N = len(tops)  # N 個骨牌
        counter = Counter(tops) + Counter(bottoms)  # 數一下，統計點數「出現次數」
        k,v = counter.most_common(1)[0]  # 出現最多的點數是 k, 出現 v 次

        if v<N: return -1  # 如果出現次數「不夠」，一定失敗，return -1

        ans1 = ans2 = 0  # 有兩種可能：放上面（對應 ans1）、放下面（對應 ans2）
        for i in range(N):  # 每個骨牌巡一輪，目標是「把k移到上面 or 下面」
            if k==tops[i] and k!=bottoms[i]: ans2 += 1  # 上面是k，但下面不是k，那就要「轉1次」讓下面能有k
            if k==bottoms[i] and k!=tops[i]: ans1 += 1  # 下面是k，但上面不是k，那就要「轉1次」讓上面能有k
            if k!=tops[i] and k!=bottoms[i]: return -1  # 若上下都不是 k 那就失敗囉！
        return min(ans1, ans2)  # 放上面？放下面？哪個小，就用那個！
