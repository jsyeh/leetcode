# LeetCode 3405. Count the Number of Arrays with K Matching Adjacent Elements
# 有幾種 array 符合規定： n 個數（範圍是 1...m），剛好有 k 個數符合 arr[i-1] == arr[i]
# 看起來像「排列組合」的題目，再用乘法，就能算出答案。但高中「排列組合」的題目，有時候想不太到
# 有人想得到「比較有條理的解法」 --- 我忍不住偷看 lee215 的答案 --- 果然短到不可思議
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7  # 答案會超多組的，要取 10^9+7 的餘數
        # 剛好有 k 個數「與前一項相同」，所以「不用考慮這k個數」，
        # 只要先決定剩下 n-k 個數的值「相鄰不同」當基準
        # 第1項有 m 種可能，第2項有 m-1 種可能，後面都是 m-1 種可能
        # part1 = m * (m-1) * (m-1) * (m-1) * ...  共 n-k-1 個重覆，合計 n-k 個數
        part1 = m * pow(m-1, n-k-1, MOD)  # 剛好 Python pow()指數函數，可順便取餘數
        # n-k 個不同的數 vs. k 個「棒子」當間隔，代表「有 k 個數」，與「前 1 個數相同」
        # 「棒子」不能放在最前面，所以就「把最前面避開」共 n-1 個位子「挑k個數」
        part2 = comb(n-1, k)
        return part1 * part2 % MOD
