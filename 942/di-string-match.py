# LeetCode 942. DI String Match
# 字串 s 很長 10^5，裡面 'I' 增加 ans[i] < ans[i+1]
# 'D' 減少 ans[i] > ans[i+1]，ans 有0...N 共 N+1 個數，
# 排列組列，請回傳任何「合理」的陣列。
# 本來想不出解法，但看 lee215 的想法，覺得很帥：從中間出發、往上往下加，就湊出答案了！
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ans = [0]  # 一開始，從中間0出發
        up, down = 0, 0  # 出發點，做出「上界」和「下界」
        for c in s:
            if c=='I':  # 還到增加，就挑「更大的數」
                up += 1  # 大要變「更大」
                ans.append(up)  # 塞入答案
            if c=='D':  # 遇到減少，就挑「最小的數」
                down -= 1  # 小要變「更小」
                ans.append(down)  # 塞入答案
        # 湊完答案後，有負的，怎麼辦？就把全部的數「往上挪抬」
        return [now - down for now in ans ]
        # 「要把 down 抬高變0」，就需要「每個數都-down」（負負得正）
