# LeetCode 3333. Find the Original Typed String II
# 「原本打字打什麼？」可能會不小心重覆多次按重覆鍵，得到 word 字串
# 原本的字串長度「至少k個字母」問有幾種可能的原本的字串
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9+7  # 時時記得「取餘數」
        repeat = [[word[0], 1]] # 先數一數, 「相鄰不同」的字母「重覆的次數」
        for i in range(1,len(word)):  # 每個字母, 與前一個字母相比
            if word[i-1]==word[i]: repeat[-1][1] += 1  # 相同, 舊的數量 +1
            else: repeat.append([word[i], 1])  # 不同, 就新的開始
        total = 1  # 把全部項次, 都乘起來
        for c, t in repeat:
            total = total * t % MOD  # 時時記得「取餘數」
        n = len(repeat)  # 在 repeat 資料裡, 分成幾個 groups 對應最少有多少字母
        if len(repeat)>=k:  # 運氣好，已達成「至少k個字母」規定，直接乘出答案
            return total  # 前半段「簡單」
        # 不幸「不足k項」時，要用DP算出「不足項」造成的可能減少的可能性，「難」
        table = [0] * k  # 可接受 k 個字母以上。k 字母以下「有問題、要扣掉」
        table[0] = 1  # 0個字母，算1種法，用 buttom-up 的方法來建 DP 表格
        for c, t in repeat:  # 字母 c 連續出現 t 次
            table2 = [0] * k  # 不想建 2D table，就兩個 table 交換即可省空間
            now = 0  # 考慮到現在的字母 c 時，有幾種可能
            for i in range(k):  # table2[i]的值。時時記得「取餘數」
                if i > 0: now = (now + table[i-1]) % MOD  # 從前一項生出答案
                if i > t: now = (now - table[i-t-1] + MOD) % MOD  # 比此字母數量多
                table2[i] = now  # 
            table = table2  # 1D 的兩個表格交換, 可省下 2D 的表格的空間
        bad = sum(table[n:k]) % MOD  # 「有問題、要扣掉」有幾項。時時記得「取餘數」
        return (total - bad + MOD) % MOD  # 時時記得「取餘數」

        @cache  # 沒想到「函式呼叫函式」的 DP 超過時間, 果然 Hard
        def helper(i, k):  # 現在處理 table[i] 的字母
            if i==n: return k<=0  # 字母走到盡頭, 若剛好k剛好耗盡,就是1種成功
            if k<=0: return repeat[i][1] * helper(i+1, k)  # 字母能全用、照這倍數「換下個字母」
            count = 0  # 有很多種用字母的方法
            for f in range(1, repeat[i][1]+1):  # 再換下個字母
                count = (count + helper(i+1, k-f)) % MOD
            return count % MOD
        return helper(0, k)
