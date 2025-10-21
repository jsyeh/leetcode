# LeetCode 656. Coin Path
# coins 陣列 1-indexed（陣列從1開始）每次最多跳 maxJump 格，踩到的格子加起來
# 要用最小 cost 到達最後一格的，把路徑 return。
class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        N = len(coins)
        if coins[N-1]==-1: return []  # 目的地「無法到達」直接結束

        bestJump = [-1] * N  # 找到最佳路徑
        bestScore = [inf] * N
        bestScore[N-1] = coins[N-1]
        bestJump[N-1] = N
        @cache
        def minCoins(i):  # 能得到的最多coins
            if i==N-1: return coins[i]
            if i==N: return inf
            if i>N: return inf
            if coins[i]==-1: return inf 
            for j in range(1, maxJump+1):  # 這次跳幾步
                if i+j > N: break
                now = coins[i] + minCoins(i+j)
                if now < bestScore[i]: #if now < ans:
                    #print('bestJump', bestJump)
                    #print('bestScore', bestScore)
                    #print('now', now, 'i+j', i, j)
                    bestJump[i] = i+j
                    bestScore[i] = now
            return bestScore[i] #ans + coins[i]  # 現在踩的這格的金幣，也要加入
        minCoins(0)  # 利用「函式呼叫函式」來更新 bestJump陣列
        #print('bestJump', bestJump)
        #print('bestScore', bestScore)
        ans = []  # 因 1-indexed 從1開始走
        now = 0
        while now < N:
            ans.append(now+1)
            now = bestJump[now]
            if now==-1: return []  # 此路不通、結束
        return ans
        
