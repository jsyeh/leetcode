# 有一堆括號和英文字母，但可能不是「合理的括號配對」。
# 問「刪掉幾個括號」後，便能合理
# 沒什麼靈感，看了 dreamcoder21 的 Solution 清楚明瞭，收穫很多
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s) # 先轉成 list 才能修改、刪除
        stack = [] # 用來存 括號的位置
        # 最誇張的狀況，是括號全刪。但若能組出合法配對，其實就不用刪
        for i,c in enumerate(s):
            if c=='(': # 上括號，放入 stack 
                stack.append(i) # 記下位置i
            if c==')': # 在收尾時，可能成功、可能失敗
                if len(stack)>0: # 有上括號可配對，成功
                    stack.pop() # 括號配對完成，安全下崗，不需處理
                else: # 括號對不起來，失敗
                    s[i] = '' # 清掉它
        # 最後收尾時，沒配對到的上括號，都要清空
        for i in stack:
            s[i] = '' # 清空
        return ''.join(s)
