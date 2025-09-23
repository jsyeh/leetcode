# LeetCode 165. Compare Version Numbers
# 「版本號碼」裡有數字、小數點, 像是 1.01 或 1.1.1 等
# 有兩個字串, 對應兩個版本號碼。比較兩個版本號碼，看看誰比較大：
# 如果左邊大, 就回傳1。右邊大, 就回傳-1。就很像 a-b 看正負號的意思
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))  # 把字串, 用點斷開, 變陣列
        v2 = list(map(int, version2.split('.')))
        N1, N2 = len(v1), len(v2)  # 陣列的長度，因為要補齊
        N = max(N1, N2)  # 比較長的陣列為主，以便補齊
        v1 += [0] * (N-N1)  # 補齊陣列，讓兩陣列的長度相同
        v2 += [0] * (N-N2)
        for i in range(N):  # 逐項檢查
            if v1[i] > v2[i]: return 1  # 左大
            if v1[i] < v2[i]: return -1  # 右大
        return 0  # 都相等
