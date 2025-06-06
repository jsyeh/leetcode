# LeetCode 2434. Using a Robot to Print the Lexicographically Smallest String
# 「逐一搬字母」，有2種搬法：把字母搬到 stack 倉庫、把字母從 stack 倉庫「最上面」搬到ans
# 問能組合出「字典序最小」的字串是什麼？ 這題就用 Stack 來模擬即可
class Solution:
    def robotWithString(self, s: str) -> str:
        counter = Counter(s)  # s 裡全部字母的「統計數量」
        ans = []  # 答案
        t = []  # stack 倉庫
        now = 'a'  # 目前最小字母 now（要儘速搬到 ans 裡）
        for c in s:  # 每個字母，逐一處理
            t.append(c)  # 搬法1：先搬到 stack 倉庫
            counter[c] -= 1  # 搬走後，s 剩下的字母(更新「統計數量」)
            while counter[now]==0 and now < 'z':  # 目前最小的字母「用盡」
                now = chr(ord(now)+1) # 且能換下個字母，就換下一個字母 now
            while t and t[-1] <= now:  # 如果 stack 倉庫裡，「最上面」的字母「比now更小」
                ans.append( t.pop() )  # 就吐出來、塞到答案 ans 裡
        ans += reversed(t)  # 剩下在 stack 倉庫的字母，就「倒著」依序塞入答案
        return ''.join(ans)  # 把答案「接成字串」
