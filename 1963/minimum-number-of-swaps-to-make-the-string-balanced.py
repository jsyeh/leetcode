# LeetCode 1963. Minimum Number of Swaps to Make the String Balanced
# 一堆括號，要交換幾次，才能 balanced 括號正確括好？
class Solution:
    def minSwaps(self, s: str) -> int:
        ans = 0  # 有幾組 mismatch
        depth = 0  # 目前括號的深度
        for c in s:  # 針對每個字母分析
            if c=='[':  # 太好了，是上括號
                depth += 1  # 增加上括號的「深度」，容忍度增加！
            else:  # 糟糕，是下括號，要用掉「容忍度」哦！
                if depth>0:  # 容忍度夠用
                    depth -= 1  # 簡單用掉
                else:  # 但是不夠時，怎麼辦？
                    ans += 1  # 遇到不夠時，這組要換掉。
                    depth += 1 # 把後面某'['移來，會加大「容忍度」
        return ans

