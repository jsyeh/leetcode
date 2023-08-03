class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        # 'digits' must consist of values from 2 to 9 only
        # 所以字母對照表中， 0 和 1 就不用考慮
        N = len(digits)
        if N==0: # 如果題目是空字串，那答案是空集合
            return []

        def helper(start, N) -> List[str]:
            if start==N:
                return [""] # 裡面有空字串，方便前一層helper()可結合答案
            ans = []
            i = int(digits[start]) # 用來查 table[i]
            for c in table[i]: # table[i]裡的每個字母c逐一取出，以便結合
                lists = helper(start+1, N) # 問後續的答案
                for temp in lists:
                    ans.append(c+temp) # c+temp 可把字母結合出更長字母
            return ans
        
        return helper(0, N)
