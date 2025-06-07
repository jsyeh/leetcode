# LeetCode 3170. Lexicographically Minimum String After Removing Stars
# 字串每次遇到星號，可把星號左邊挑1個「最小的字母」刪掉（其實就刪最右邊最小的那個）
class Solution:
    def clearStars(self, s: str) -> str:
        ans = list(s)  # 把字串變成 list，之後遇到 '*' 可將之前「最小字母」的格子塗掉
        prevPos = [-1] * len(s)  # 字母 s[i]「前一次出現的 index 位置」在 prevPos[i]
        prev = {c:-1 for c in "abcdefghijklmnopqrstuvwxyz*"} # 每種字母「之次」出現位置
        counter = Counter()  # 統計迴圈 s[i] 之前，字母出現次數，以便找到「之前」最小的字母
        for i, c in enumerate(s):  # 依序處理 字串 s 的第 i 個字母 c 
            prevPos[i] = prev[c]  # 現在 s[i] 的字母 c 之前曾出現在 prevPos[i]
            prev[c] = i  # 以後再查「字母 c」之前出現在位置 i
            counter[c] += 1 
            if c=='*':  # 若要「刪掉」之前最小的字母
                for c2 in "abcdefghijklmnopqrstuvwxyz":  # 先找到「之前最小的字母」c2 是誰
                    if counter[c2]>0:  # 只要「數量>0」就代表「找到最小的字母」c2
                        i2 = prev[c2]  # 最小的字母 c2 之前出現在 i2 
                        ans[i2] = '*'  # 把之前出現的位置，打上 '*' 代表這個字母被刪掉了
                        prev[c2] = prevPos[i2]  # prev[c2] 要換到「更早之前」出現的位置
                        counter[c2] -= 1  # 因為刪掉 c2 所以數量 -1
                        break  # 處理完，便可離開 c2 迴圈
        # 最後把星號再刪掉即可
        return ''.join([ans[i] for i in range(len(ans)) if ans[i]!='*'])
