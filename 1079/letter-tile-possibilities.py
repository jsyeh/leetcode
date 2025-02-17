# LeetCode 1079. Letter Tile Possibilities
# 排列組合題：tiles[i] 不同的字母代表不同地磚，問有幾種排法（可長可短，但不能空字串）
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = Counter(tiles)
        
        def dfs(i):  # 現在處理到第幾個字母（使用「函式呼叫函式」）
            if i==len(tiles): return 1
            ans = 1
            for c in counter:  # 針對目前還能使用的字母，逐一嘗試
                if counter[c]==0: continue  # 用完的字母跳掉
                counter[c] -= 1  # 用掉現在的「字母」
                ans += dfs(i+1)  # 使用「函式呼叫函式」，解「小問題」
                counter[c] += 1  # 把「字母」還回去，換下一個「字母」
            return ans

        return dfs(0) - 1  # 要扣掉1個（空字串）
