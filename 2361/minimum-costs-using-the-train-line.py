class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        N = len(regular)
        ans = [0]*N
        exp = [0]*N
        ans[0] = regular[0]
        exp[0] = expressCost + express[0]
        if expressCost + ans[0] < exp[0]:
            exp[0] = expressCost + ans[0]
        if exp[0] < ans[0]:
            ans[0] = exp[0]
        # 有三種路徑：(1) regular, (2) express, (3) 剛好過馬路過來
        # 到 exp[i] 最便宜的走法，要多考量：本站過來 or 前一站過來
        # 到 ans[i] 還有多一種走法，是免費從 exp[i] 過來
        for i in range(1,N):
            ans[i] = ans[i-1] + regular[i]
            exp[i] = exp[i-1] + express[i]
            if expressCost + ans[i] < exp[i]:
                exp[i] = expressCost + ans[i]
            if expressCost + ans[i-1] + express[i] < exp[i]:
                exp[i] = expressCost + ans[i-1] + express[i]
            if exp[i] < ans[i]:
                ans[i] = exp[i]
        for i in range(N):
            if exp[i] < ans[i]:
                ans[i] = exp[i]
        return ans
