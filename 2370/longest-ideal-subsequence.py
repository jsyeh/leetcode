# 題目的縮寫 LIS 可能是致敬 Longest Increasing Subsequence 的意思
# 相鄰的字母, 要符合「距離<=k」的限制。可建個表格 table[i], 記錄s[i]結尾的最長的值
# 但想想不對, 這樣的話table太大, 在找 table 時, 就會超時。
# 後來看了 lee215 的解法, 他的 table 是建 table = [0]*26 對應26個字母
# c = s[i], 更新 table[c] 介於 max(table[c-k]...table[c+k])+1 的值
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        N = len(s)
        table = [0]*26
        
        for c in s: # 逐個字母更新
            now = ord(c) - ord('a')
            left = max(0,now-k) # 左界包含
            right = min(26,now+k+1) # 右界不包含
            table[now] = max(table[left:right]) + 1
        return max(table)

        
