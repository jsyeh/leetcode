# LeetCode 1925. Count Square Sum Triples
# 計算 <=n 的 a*a+b*b==c*c 有幾組
class Solution:
    def countTriples(self, n: int) -> int:
        # 如果用「空間換取時間」可以更快一點
        # 也就是「先把全部的 c平方記起來」
        n2 = n*n
        c_square = [False] * (n2+1)
        for c in range(1,n+1):
            c_square[c*c] = True  # 是平方的數,記起來

        # 用暴力2層迴圈 1 <= a,b,c <= n
        ans = 0
        for a in range(1,c):  # 調整界限, 以便提早結束
            for b in range(a+1,c):  # 因為
                if a*a+b*b<=n2 and c_square[a*a+b*b]: ans += 1
        return ans*2  # 兩倍的可能, 也就是 a,b交換
