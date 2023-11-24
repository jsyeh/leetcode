# 好像玩遊戲一樣的模擬題: 你挑3個 piles, Alice先挑, 換你挑, 再換 Bob 挑
# 你希望得到最多。但別忘了 Alice 比你先挑。先以要設計一個greedy的過程。
# 先排好序, 最大、次大、最小, 持續做, 便是你能拿最多的方法。
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        N = len(piles)//3 # 3個人, 每個人會拿 N 個 piles
        print(N, piles)
        ans = 0
        # for i in range(N-1, -1, -1): # 倒過來的迴圈
        for i in range(3*N-2, N-1, -2): # 修改過的迴圈, 你挑的是每一個「次大」,最小的N個都不取
            ans += piles[i]
        return ans
        
