# LeetCode 1910. Remove All Occurrences of a Substring
# 持續從 s 字串裡除掉 part 字串（小心「刪掉後」可能會再組出 part 字串）
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        ans = []  # 可用 stack 來組出「目前為止處理的字母」
        part = list(part)  # 改用 list 和 list 相比
        N = len(part)
        for c in s:
            ans.append(c)
            while len(ans)>=N and ans[-N:]==part:
            # 若收集足夠多的字母，且「後面N個字母」剛好與 part 相同
                ans = ans[:-N]  # 就吐掉「後面N個字母」
        return ''.join(ans)
