# LeetCode 1411. Number of Ways to Paint N × 3 Grid
# N x 3 的格子，漆3種色彩「相鄰不同色」問有幾種漆法
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9+7  # 因答案很大，要取餘數
        set3 = set([0,1,2])  # 共有3種色彩，用「集合」算出「不能用的色彩」
        @cache  # 可用「函式呼叫函式」解決問題
        def helper(i,a0,b0,c0):  # 現處理 row i 橫條，前一條用色彩 a0, b0, c0
            if i==n: return 1  # 順利走到最後，算1種解法
            ans = 0  # 原本色彩 set3 扣掉不能用的色彩，便是「剩下」能用的色彩
            for a in (set3 - set([a0])):  # 要和 a0 不同
                for b in (set3 - set([a,b0])):  # 要和 a 與 b0 不同
                    for c in (set3 - set([b,c0])):  # 要和 b 與 c0 不同
                        now = helper(i+1, a,b,c)  # 這層用(a,b,c)換下一層 i+1
                        ans = (ans + now) % MOD  # 累加這次的可能，記得取餘數
            return ans
        return helper(0,-1,-1,-1)  # -1 當色彩，等於不受限、可自由挑 0,1,2三色
        
