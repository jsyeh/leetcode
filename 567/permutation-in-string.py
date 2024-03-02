# s1短字串，任意排列組合後，有在s2出現，便是True
# 可用 Counter(s1) 配合 running/sliding window 來解
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        N1, N2 = len(s1), len(s2)
        if N1 > N2: return False # 長度不夠
        H1 = Counter(s1)
        H2 = Counter(s2[:N1]) # 前面 N1 個字母，長度與s1相同的部分
        if H1-H2 == Counter(): return True # 如果完全相同，就找到
        for i in range(N2-N1): # 後續繼續移動
            H2[s2[i]] -= 1 # 扣掉前一項
            H2[s2[i+N1]] += 1 # 加上後一項
            if H1-H2 == Counter(): return True # 完全相同，就找到
        return False # 沒有找到
