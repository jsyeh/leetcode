class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        self.ans = False

        def helper(s, i, table):
            if len(s)==0:
                if i==len(pattern):
                    self.ans = True
                return 
            if i==len(pattern):
                return
            
            curr_pattern = pattern[i]
            for k in range(len(s)):
                part1 = s[:k+1]
                part2 = s[k+1:]
                if curr_pattern not in table and part1 not in table.values():
                    table[curr_pattern] = part1
                    helper(part2, i+1, table)
                    del table[curr_pattern]
                elif curr_pattern in table and table[curr_pattern] == part1:
                    helper(part2, i+1, table)
            
        helper(s, 0, {})
        return self.ans
