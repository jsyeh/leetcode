# LeetCode 1653. Minimum Deletions to Make String Balanced
# 目標：'a'只能在左邊、'b'只能在右邊。你要刪掉幾個字母，才能做到？
# 可簡單用迴圈，就成功了：先問「全部都是b」要做幾步？接下來迴圈把目標「讓左邊長出a」
class Solution:
    def minimumDeletions(self, s: str) -> int:
        counter = Counter(s)  # 先數數，有幾個'a'、有幾個'b'
        deleteA = counter['a']  # 把全部的'a'都刪掉，是種作法
        deleteB = 0  # 只 deleteA 且 deleteB是0，便能做出「全部都是'b'」
        ans = deleteA + deleteB
        for c in s:  # 從左到右，逐一把「不合理的b刪掉」
            if c=='a': deleteA -= 1  # 太好了，左邊'a'本來就合理，可少刪'a'
            if c=='b': deleteB += 1  # 哇，左邊有個不合理的'b',刪
            ans = min(ans, deleteA+deleteB)  # 逐步更新「最佳」的答案
        return ans
