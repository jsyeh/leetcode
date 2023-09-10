class Solution:
    def countOrders(self, n: int) -> int:
        @cache
        # 去問「還要pick幾個，還要deliver幾個」的排列組合數
        def helper(p, d)->int:
            if p==0 and d==0: # 終止條件，完成任務
                return 1 # 基礎的一種
            
            if p<0: return 0
            if d<0: return 0
            if d<p: return 0 # 不合理（p後才能d,竟然剩的p比d還多）

            # 挑一件來pick，之後是 helper(p-1,d)
            # 而挑的可能有 p 種，所以 p * helper(p-1,d)
            ans1 = p * helper(p-1, d) # 挑1件來pick
            # 挑一件來deliver, 之後是 helper(p,d-1)
            # 而能挑的可能是 (d-p) 件貨
            ans2 = (d-p) * helper(p, d-1) # 挑1件來deliver
            return (ans1+ans2) % 1000000007
        return helper(n, n)
        
