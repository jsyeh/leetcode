# 字母可能會重覆。把第1個（沒有重覆的）字母的位置記起來
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s) # 統計字母出現次數
        for i,c in enumerate(s): # 再巡一次全部的字母
            if counter[c]==1: return i # 若出現1次，找到
        return -1 # 都沒有找到，回傳 -1
