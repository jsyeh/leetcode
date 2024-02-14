class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c,r,_,c2,r2 = s # 先拆解到 c r 變數裡
        ans = []
        for cc in range(ord(c), ord(c2)+1): # 字母
            for rr in range(int(r), int(r2)+1): # 數字
                ans.append(chr(cc)+''+str(rr))
        return ans
