# LeetCode 3330. Find the Original Typed String I
# 打字不小心最多觸發1次「重覆按某個字母」看到很多連續字母
# 到底原本想要打的字，有幾種可能呢?
class Solution:
    def possibleStringCount(self, word: str) -> int:
        # 所以先找出連續的重覆字母，然後加出它的可能
        ans = 1  # 一定有一種「原先的字」
        for i in range(len(word)-1):
            if word[i]==word[i+1]:  # 若有重覆
                ans += 1  # 可能這個重覆是多的, 刪掉即是一種
        return ans
        
