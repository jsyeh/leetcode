# LeetCode 3403. Find the Lexicographically Largest String From the Box I
# 把字串, 切成 n 段, 所有可能切法中, 字典序最大的小字串回傳
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1: return word  # 就只分1段,全上即可
        N = len(word)  # 字串的長度, 會決定迴圈 i 從哪裡開始
        M = N - (numFriends - 1) 
        # 「最長」可能的字串的長度: N - (n-1) 其他(n-1)都1字母
        ans = word[0:M]  # 最左邊最長的那個字母
        for i in range(N):  # 每個可能的開始的格子 i
            ans = max(ans, word[i:i+M])  # 從 i 開始,最長的字串,是否更大
        return ans
