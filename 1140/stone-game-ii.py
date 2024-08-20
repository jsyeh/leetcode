# LeetCode 1140. Stone Game II
# 依序拿石頭，一開始M=1，可拿X堆石頭（1<=X<=2*M)，之後M=max(M,X)
# 兩人都想拿最多。問 Alice 最後拿了幾個石頭。（每個人的最大值，對應「留給對手最小值」）
# 可利用「函式呼叫函式」的Top-Down DP 法，全部試過一次，來找答案
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # 為快速知道「挑了多少石頭」，使用postSum[i]快速算出「某範圍」的石頭數
        N = len(piles)
        postSum = [0]*N  # preSum是左邊加總過來的陣列，postSum是右邊加到左邊的陣列
        postSum[N-1] = piles[N-1]  # 最右邊數值就是 piles最右邊
        for i in range(N-2, -1, -1):  # 從右到左，倒過來的迴圈
            postSum[i] = postSum[i+1] + piles[i] # 右項+對應的pile
        @cache
        def helper(i,M): # 函式呼叫函式，了解在i之後能取幾個最佳解
            if i+2*M>=N: return postSum[i] # 最後人可全取，答案是i後的全部
            bob = inf # 下一輪的bob，想讓他最少（找最小值，預設用「無限大」反過來）
            for X in range(1,M*2+1): # X 這輪alice可取用的量是 1...M*2
                # 取剩的，讓bob去試答案
                bob = min(bob, helper(i+X, max(X,M))) # 下一輪能取的值，希望最小
            return postSum[i] - bob # 我們能取的最多，對應bob取得最少
        return helper(0,1)
