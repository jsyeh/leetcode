# LeetCode 425. Word Squares
# 用 words 建出 word square 直的讀、橫的讀，竟然剛好一樣
# ball
# area
# lead
# lady
# 找出所有的 word squres。解答中 lzb700m 畫了很棒的示意圖，方便理解
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        # 先製作 prefix hash map
        N = len(words[0])  # 字的長度 N 都相同
        table = defaultdict(list)  # 找出 table[prefix] 全部相關的字
        for word in words:
            for i in range(N):
                table[word[:i+1]].append(word)
        ans = []  # 累積放答案
        def helper(now, i):  # 利用「函式呼叫函式」來解這題，有參考 Stefan Pochmann 的解法
            if i==N:  # 順利走到最後
                ans.append(now)  # 代表 now 符合 word square 規則，放入「答案」裡
                return
            # now 裡每個字第 i 個字母「組出的 prefix 字串」問 table 有哪些字 word 能試
            for word in table[''.join([now[ii][i] for ii in range(i)])]:
                helper(now + [word], i+1)  # 函式呼叫函式，多個字，再多一層
        for word in words:  # 每個字，有都「當第1個字」的機會
            helper([word], 1)  # 「函式呼叫函式」找答案
        return ans
