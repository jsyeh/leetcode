# balanced: a都在左邊 b都在右邊
# 問要「刪幾個字母」便可以 balance
# 也就是問「發生幾次不balance」的事件
# 其實有點像「左邊幾個1」「右邊幾個0」的題目
# https://leetcode.com/problems/maximum-score-after-splitting-a-string/
class Solution:
    def minimumDeletions(self, s: str) -> int:
        N = len(s)
        leftB, rightA = 0, 0 # 不合規定的 leftB rightA 各幾個
        for i in range(N): # 先算「右邊全部」有幾個a
            if s[i]=='a': rightA += 1

        ans = leftB + rightA # 一開始的狀況
        # 逐步吐出 s[i] 讓左邊變長、右邊變短，並更新leftB rightA
        for i in range(N):
            if s[i]=='a': # 右邊的 rightA 變少
                rightA -= 1
            if s[i]=='b': # 左邊的 leftB 變多
                leftB += 1
            if leftB+rightA < ans: # 不好的數目「更少」
                ans = leftB+rightA # 就更新
        return ans
# case 153/157: "b" 答案是0
