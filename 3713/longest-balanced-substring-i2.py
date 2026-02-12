# LeetCode 3713. Longest Balanced Substring I
# 找出 s 的子字串，裡面字母出現次數一樣多。
class Solution:
    def longestBalanced(self, s: str) -> int:
        ans = 1  # 初始值是1，因長度為1的字串，剛好也是答案
        for i in range(len(s)):  # 字串開始位置 s[i]
            counter = Counter()  # 針對s[i]開始，統計字母
            for j in range(i, len(s)):  # 字串結束位置 s[j]
                counter[s[j]] += 1  # 現在增加的字母 s[j]
                if j-i+1 < ans: continue  # 字串長度太短，不更新
                for v1, v2 in pairwise(counter.values()):
                    if v1 != v2: break  # 兩兩比較，不相同就失敗
                else:  # 沒有失敗，就成功，太好了
                    ans = j-i+1  # 現在字串長度「更長」更新答案
        return ans
