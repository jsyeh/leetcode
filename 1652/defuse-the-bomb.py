# LeetCode 1652. Defuse the Bomb
# 拆除炸彈：code[i] 是圓形的密碼
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        ans = [0]*N
        if k==0: return ans  # 全部都放0
        if k>0:  # 正的k，將之後 k 項加起來
            for i in range(N):
                for kk in range(k):
                    ans[i] += code[(i+1+kk)%N]
            return ans
        else:  # 負的k，將之前 k 項加起來
            for i in range(N):
                for kk in range(-k):
                    ans[i] += code[(i-1-kk)]
            return ans
