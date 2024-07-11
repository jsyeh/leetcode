# LeetCode 1190. Reverse Substrings Between Each Pair of Parentheses
# 括號裡的內容，全部要「反過來」。然後再反過來，再反過來。
# 可以使用 list 的「最後一個元素」，裡面放括號裡「要反過來」的內容。
# 上括號時準備，下括號時，執行「反過來」的任務。
class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans = ['']  # 最後一項，是空字串，方便後面要加字母
        for c in s:
            if c == '(': # 新的上括號，讓最後1個元素，收集「將要反過來」的元素
                ans.append('') # 加一個新的開始
            elif c==')': # 收成的下括號，把最後1個元素的內容，全部「反過來」
                # print(ans)
                now = ans.pop() # 取出最後的全部元素
                last = ans.pop() # 要用來結合（後方反過來）答案的最後元素
                ans.append(last + now[::-1]) # 反過來的部分，再接到後來的最後一項
            else:
                last = ans.pop()  # 最後1項，要再加長
                ans.append(last + c)
        # print(ans)
        return ans[0]  # 取出最後的結果
''' 以下是過程的模擬，在 ')'時，印出 ans 裡的結果
s =
"(ed(et(oc))el)"
Stdout
['', 'ed', 'et', 'oc']
['', 'ed', 'etco']
['', 'edocteel']
['leetcode']
'''
