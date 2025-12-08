# LeetCode 1925. Count Square Sum Triples
# 計算 <=n 的 a*a+b*b==c*c 有幾組
class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        # 用暴力3層迴圈 1 <= a,b,c <= n
        for c in range(1,n+1):  # 調一下順序, 讓迴圈快一點
            for a in range(1,c):  # 調整界限, 以便提早結束
                for b in range(1,c):
                        if a*a+b*b==c*c:  # 合條件
                            ans += 1
                        elif a*a+b*b>c*c:  # 爆表的話
                            break  # 提早結束
        return ans
