# LeetCode 93. Restore IP Addresses
# 有一堆數字，轉換成「所有可能的IP」字串
# 也就是把「3個句點」，加入字串中，讓每個數字字串「介於0-255之間」
# Editorial 用了 backtracking 及 iteration 兩種作法，我試著用「函式呼叫函式」解
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        @cache
        def helper(start, N, dot):  # 會把所有可能的子字串回傳
            if dot>4: return []  # 超過範圍，不行（只能有4組數字）
            if dot==4 and start==N: return ['']  # 完美走到最後(可接上suffix)
            ans = []
            for i in range(1,4):  # 每段的字串長度1-3字母 (0..255 是1-3位數)
                now = s[start:start+i]  # 目前切的數字
                if now=='': continue  # 字串太短（發生在最後 start+i 不夠切的狀況）
                if i>1 and now[0]=='0': continue  # 不能 leading zero （多位數、第1位為0）
                if int(now)>255: continue  # 不能數字太大，要介於0..255間
                for suffix in helper(start+i, N, dot+1):  # 函式呼叫函式，得到suffix字串
                    if suffix=='': ans.append(now)  # 如果是最後1個數字，就不用加句點
                    else: ans.append(now+'.'+suffix)  # 中間的數字，要加「句點」
            return ans
        return helper(0, len(s), 0)  # 從頭開始、總長是N，目前得到「0組數字」
