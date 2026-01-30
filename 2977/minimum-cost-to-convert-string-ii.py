# LeetCode 2977. Minimum Cost to Convert String II
# 要將 source 字串變 target 字串，規則比較複雜（每次替換的字串較長）
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        parts = set(original + changed)  # 把所有的「字串片段」，變成 set，方便table迴圈 & 拆解斷字
        table = { a:{b:0 if a==b else inf for b in parts} for a in parts } 
        # 用倒裝句，先初始 table[a][b] 是 0 或 inf：若 table[a][a] 同個字串，就放0，不同字就放inf
        for a,b,c in zip(original, changed, cost):  # 逐一更新 table[a][b] 的 cost c
            table[a][b] = min(table[a][b], c)  # 依題目的參數 original changed 和 cost 來更新
        for k in parts:  # 利用 DP 每次「多用一種」中間字串 k，轉接 a 到 k 到 b
            for a in parts:  # 想更新 起點a 中間點k 終點b
                if table[a][k]==inf: continue  # 加速（避開無效的中間點 k，因 a 不能到 k）
                for b in parts:  #  a 到 b（可經過中間k）的最小 cost
                    table[a][b] = min(table[a][b], table[a][k]+table[k][b])  # 更新 cost
        # 上面完成 table[a][b] 的最新資訊；下面用 helper() 函式呼叫函式來解
        diffs = sorted(set([len(s) for s in original]))  # 各種可能字串長度，供 helper()「拆解斷字」
        N = len(source)  # source 字串的長度，供 helper()函式判斷「終止條件、字串範圍」
        @cache
        def helper(i):  # 用「函式呼叫函式」逐一處理 source 字串的各種可能「拆解斷字」
            if i == N: return 0  # 走到 source 字串最後面，順利結束
            ans = inf  # inf 對應「找不到答案」
            for d in diffs:  # 小到大，去試「拆解斷字」的各種可能長度 d 
                if i+d > N: break  # 超過 source 字串，不能拆出 source[i:i+d]，離開
                a, b = source[i:i+d], target[i:i+d]  # 拆出2個字串片斷
                if a in parts and b in parts and table[a][b] != inf:  # a 和 b 是可能的拆解法
                    ans = min(ans, table[a][b] + helper(i+d))  # 函式呼叫函式，更新答案
            for i2 in range(i,N):  # 接著觀察，若有「對應的字母相同」可保留、換下個位置 i2
                if source[i2] != target[i2]: break
                ans = min(ans, helper(i2+1))  # 函式呼叫函式，更新答案
            return ans
        ans = helper(0)  # 函式呼叫函式，從最左邊0開始，逐一測試
        if ans==inf: return -1  # 若「找不到答案」
        return ans  # 有找到答案
