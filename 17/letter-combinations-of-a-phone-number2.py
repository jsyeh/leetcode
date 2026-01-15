# LeetCode 17. Letter Combinations of a Phone Number
# 電話鍵盤2-9可對應英文字母，給你幾個數字，找出「所有的可能」的英文
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs','tuv','wxyz']
        ans = []
        def helper(i, now):  # 函式呼叫函式
            if i==len(digits): 
                ans.append(now)  # 到䀆頭，存下答案
                return
            for c in table[ int(digits[i]) ]:  # 逐一試「對應的字母」
                helper(i+1, now+c)  # 函式呼叫函式
        helper(0, '')
        return ans
