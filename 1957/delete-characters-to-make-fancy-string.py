# LeetCode 1957. Delete Characters to Make Fancy String
# 「不可連續3個相同字母」的字串，要把 s 刪掉幾個字母才行？
# 就直接 for迴圈，如果重覆的字 < 3 就 ans.append(c) 放入答案
class Solution:
    def makeFancyString(self, s: str) -> str:
        prevC, prevN = 0, 0  # 前一次出現的字母、累積出現幾次
        ans = []  # 使用 list 會比字串快。最後再 ''.join(ans)
        for c in s:  # 逐個字母處理
            if c == prevC:  # 字母相同時，累加「累積出現次數」
                prevN += 1  # 次數+1
            else:  # 字母不相同時，換新的字母
                prevC = c  # 換新的字母
                prevN = 1  # 「累積出現次數」變1次
            if prevN < 3:  # 只要不超過3個，就可加入 ans
                ans.append(c)
        return ''.join(ans)  # 最後再把 ans 變回「字串」
