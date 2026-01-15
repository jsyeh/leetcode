# LeetCode 17. Letter Combinations of a Phone Number
# 電話鍵盤2-9可對應英文字母，給你幾個數字，找出「所有的可能」的英文
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        ans = []
        def helper(i, now):
            if i==len(digits):
                ans.append(now)
                return
            for c in table[int(digits[i])]:
                helper(i+1, now+c)
        helper(0, "")
        return ans
