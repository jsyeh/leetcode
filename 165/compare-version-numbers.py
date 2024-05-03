# 「版本號碼」裡面有數字、小數點, 像是 1.01 或 1.1.1 等
# 有兩個字串, 對應兩個版本號碼, 如果左邊大, 就回傳1。右邊大, 就回傳-1
# 就很像 a-b 看正負號的意思
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.') ))  # 把字串, 用點斷開, 變陣列
        v2 = list(map(int, version2.split('.') ))
        N1, N2 = len(v1), len(v2)  # 兩個陣列的長度
        for i in range(max(N1,N2)):  # 逐個比較
            if i<N1 and i<N2:  # i沒有超過兩個陣列的長度, 就一起比較
                if v1[i]>v2[i]: return 1
                if v1[i]<v2[i]: return -1
            elif i<N1:  # 若只剩左邊陣列長度較長, 只看左邊還有沒有數字
                if v1[i]>0: return 1
            elif i<N2:  # 若只剩右邊陣列長度較長, 只看右邊還有沒有數字
                if v2[i]>0: return -1
        return 0
