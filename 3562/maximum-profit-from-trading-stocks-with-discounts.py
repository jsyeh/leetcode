# LeetCode 3562. Maximum Profit from Trading Stocks with Discounts
# 1...n 共 n 個員工，1是CEO，hierarchy 裡有 [u直屬boss,v直屬員工]
# present[i] 和 future[i] 對應員工(1-index)買股的價錢（今天買、明天賣）
# 若「直屬boss」有買股，他的直屬員工可半價floor(present[v]/2)買。
# 可能「半價優惠」的規則，讓這題變很難處理。
class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]],  budget: int) -> int:
        tree=[[] for _ in range(n)]
        for u,v in hierarchy:
            tree[u-1].append(v-1)
        dp=[[[0]*(budget+1) for _ in range(2)] for _ in range(n)]
        self.dfs(0,present,future,tree,dp,budget)
        return max(dp[0][0])
    def dfs(self,u,present,future,tree,dp,budget):
        children=tree[u]
        child_dps=[]
        for v in children:
            self.dfs(v,present,future,tree,dp,budget)
            child_dps.append((dp[v][0],dp[v][1]))
        for parentBought in range(2):
            price=present[u]//2 if parentBought else present[u]
            profit=future[u]-price
            base=[0]*(budget+1)
            for c0,_ in child_dps:
                next_base=[0]*(budget+1)
                for b in range(budget+1):
                    if base[b]==0 and b!=0:
                        continue
                    for k in range(budget - b+1):
                        next_base[b+k]=max(next_base[b+k],base[b]+c0[k])
                base=next_base
            curr=base[:]
            if price<=budget:
                base=[0]*(budget+1)
                for _,c1 in child_dps:
                    next_base=[0]*(budget+1)
                    for b in range(budget+1):
                        if base[b]==0 and b!=0:
                            continue
                        for k in range(budget-b+1):
                            next_base[b+k]=max(next_base[b+k],base[b]+c1[k])
                    base=next_base
                for b in range(price,budget+1):
                    curr[b]=max(curr[b],base[b-price]+profit)
            dp[u][parentBought]=curr
