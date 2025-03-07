# LeetCode 2523. Closest Prime Numbers in Range
# 在 [left, right] 範圍內，找到「最接近」的兩個質數
# 可先用「篩子法」找到 10^6 以下的全部質數，並把它們的距離都算好
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        table = [True] * (right+1)  # 用篩子法「找質數」
        prime = []  # 裡面放 left...right 之間的質數
        for i in range(2, right+1):
            if table[i]:  # 是質數
                if i>=left: prime.append(i)
                for k in range(i*i, right+1, i):
                    table[k] = False
        # 上方重覆用「篩子法」算質數，浪費一些時間，有機會省下來
        ans = [-1, -1]  # 若失敗的預設值
        dist = inf  # 先設「無限大」，再更新「質數的距離」
        for i in range(len(prime)-1):
            if prime[i+1] - prime[i] < dist:  # 距離更小
                dist = prime[i+1] - prime[i]  # 就更新
                ans = [prime[i], prime[i+1]]
        return ans
