# LeetCode 2416. Sum of Prefix Scores of Strings
# words 有一堆字，對應的 scores 是 「有幾個 prefix」剛好是words裡的prefix
# 可用 Trie 像字典的樹狀資料結構，逐字分析。程式參考 Solution tojuna 的解法
class Trie:  # 自己建立 Trie 資料結構
    def __init__(self):  # 物件的建構子，在 Trie() 時會用到
        self.child = defaultdict(Trie)  # 下面可能有26種字母對應的子樹 
        self.score = 0
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()  # 像字典的樹狀資料結構
        for word in words:  # 針對每個字word分析
            t = trie  # 每次從樹根/頭開始
            for c in word:  # 這個字裡，每個字母「逐一」往下走
                t.child[c].score += 1  # 累積「多1個」經過這個prefix
                t = t.child[c]  # 樹狀結構往下
        # 前面「建構」 words 對應的 Trie 資料結構。下面逐一「統計分數」
        ans = []
        for word in words:
            t = trie  # 每次從樹根/頭開始
            score = 0  # 累積 word 這個字的分數
            for c in word:  # 這個字裡，每個字母「逐一」往下走
                score += t.child[c].score  # 收集這個prefix node的分數
                t = t.child[c]  # 樹狀結構往下
            ans.append(score)  # 收集完的分數，放入 ans 裡
        return ans
