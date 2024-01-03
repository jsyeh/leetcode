# 銀行的監控系統, 有laser devices, 會從上往下射。
# 如果整個 row 全空, 就跳過它。
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        M, N = len(bank), len(bank[0])

        ans = 0
        prev = 0 # 前一個 row 的 laser devices 的數量
        for i in range(M):
            count = 0 # 想知道這一層的 laser devices 有幾支
            for k in range(N):
                if bank[i][k]=='1': count += 1 # 找到一支
            if count==0: continue # 空的 row 就跳過
            ans += prev * count # 目前新增的 laser beams 數量
            prev = count # 換下一層
        return ans
