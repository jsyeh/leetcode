# 26個字母，有各自的score。給你一堆 letters（可能有重覆字母）要組出words
# 問最多可以組出多少 score？ dreamyjpl 說，和 78. Subsets 題目相似。
# 昨天寫的 2597. The Number of Beautiful Subsets 也是類似題型
# 利用「函式呼叫函式」來進行計算 helper(i) 會去問 helper(j+1)
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        counter = Counter(letters)  # 有這麼多 letters 可以使用
        N = len(words)
        def helper(i):  # 拆解到處理 words[i]，處理它及之後的字
            ans = 0
            for j in range(i,N):  # 依序決定下一個，是要用掉 words[j]
                now, bad = 0, False  # 如果要用掉 words[j]，後序最多可賺多少錢
                for c in words[j]:  # 第一種處理方式：決定使用 words[j]
                    now += score[ord(c)-ord('a')] # 賺到對應的分數
                    counter[c] -= 1  # 用掉字母c
                    if counter[c] < 0:  bad = True  # letters 若不夠用，就這組就無效，不算分數
                if not bad:  # 若有效、順利組出 words[j] 這個字
                    now += helper(j+1)  # 繼續組後面的字
                    ans = max(ans, now)  # 夠用，所以更新分數
                for c in words[j]:  # 第二種處理：決定不用 words[j]，要換下一個j
                    counter[c] += 1  # 字母再還回去，當作沒有用
            return ans  # 這一輪的答案
        return helper(0)  # 從最左邊的字開始試，
