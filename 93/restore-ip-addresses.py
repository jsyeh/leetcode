# LeetCode 93. Restore IP Addresses
# 有一堆數字，轉換成「所有可能的IP」字串
# 也就是把3個句號，加入字串中，讓每個字字串的數字介於0-255之間
# Editorial 用了 backtracking 及 iteration 兩種作法
# Solutions 裡 mitbbs8080 提出一個「易理解」的暴力法，決定位數
# 簡潔明瞭，試試看吧
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        N = len(s)
        for a in range(1,4): # 0-255 是1-3位數
            for b in range(1,4):
                for c in range(1,4):
                    for d in range(1,4):
                        if a+b+c+d != N: continue # 長度不對，不行
                        A = int(s[:a])
                        B = int(s[a:a+b])
                        C = int(s[a+b:a+b+c])
                        D = int(s[a+b+c:])
                        if a>1 and s[0]=='0': continue # 避leading zero
                        if b>1 and s[a]=='0': continue
                        if c>1 and s[a+b]=='0': continue
                        if d>1 and s[a+b+c]=='0': continue
                        # 但如果遇到 leading zero 怎麼辦？ 前面4行解決
                        if A<=255 and B<=255 and C<=255 and D<=255: # 合理
                            ans.append(s[:a]+'.'+s[a:a+b]+'.'+s[a+b:a+b+c]+'.'+s[a+b+c:])
        return ans        
