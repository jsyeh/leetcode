# 有很多字串，要確認「有沒有某個字串」是別人都沒有的
# 前一版 LeetCode 521. Longest Uncommon Subsequence I
# 只要看誰最長，因為最長那個，一定是獨一無二的，並回傳len(s)
# 但本題有很多字串，照著 Editorial 的方法3，可速解
# 先把 strs 照「長度」反過來sort()，先放長的，再放短的。
# 這樣「先找到」合理、獨一無二的那個，就會是最長的
# 再來，暴力排列組合，左手 strs[i] 從長的開始測，暴力 strs[j]全測
# 只要有幸「strs[i] 都不是 strs[j] 的 subsequence」就找到答案 len(strs[i])

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubsequence(A, B): # A is subsequence of B
            N1, N2 = len(A), len(B)
            if N1 > N2: return False # 左太大，就一定不是
            i = 0
            for j in range(N2): # 逐個檢查A要全部用到
                if A[i]==B[j]:
                    i += 1
                    if i==N1: return True # 有全部用完
            return False # A[i] 沒有走完
        strs.sort(reverse = True, key=lambda x:len(x))
        N = len(strs)
        for i in range(N):
            bad = False
            for j in range(N):
                if i==j: continue # 相同時，是自己
                if isSubsequence(strs[i], strs[j]):
                    # 只要有任一個是，strs[i]就沒救了
                    bad = True
                    break
            if not bad: return len(strs[i])
        return -1
