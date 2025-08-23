# LeetCode 1181. Before and After Puzzle
# 給你一堆句子 phrases，若「頭尾是同一個字」的兩句「可合併/接起來」，
# 請照「字母序」把所有能「兩兩合併」的句子找出來
class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        N = len(phrases)
        words = []  # 讓 words[i][k] 對應 phrases[i] 的第k個字
        for i in range(N):
            words.append(phrases[i].split())
        ans = set()  # 用 set() 可避開「重覆的答案」
        for i in range(N):  # 試過所有的句子組合
            for j in range(N):
                if i==j: continue  # 避開本身
                if words[i][-1] == words[j][0]:  # 字尾 接 字首
                    ans.add(' '.join(words[i] + words[j][1:]))
        return sorted(ans)  # 再排序好
