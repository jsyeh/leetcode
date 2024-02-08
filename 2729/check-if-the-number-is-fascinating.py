# n是3位數，把 n 及 2n 及 3n 當成字串，串在一起，剛好有 1-9 各用1次，便成功
class Solution:
    def isFascinating(self, n: int) -> bool:
        now = str(n)+str(n*2)+str(n*3)
        if len(now)!=9: return False # 不是9位數，失敗
        for i in range(1,10): # 1-9各測一次
            if str(i) not in now: return False # 沒有，失敗
        return True
