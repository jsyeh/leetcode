class Solution:
    def numTrees(self, n: int) -> int:
        table = [-1]*(n+1)
        def helper(k)->int:
            if k==0: return 1
            if k==1: return 1
            if k==2: return 2
            if table[k]!=-1: return table[k]
        
            sum = 0
            for i in range(k):
                part1 = helper(i)
                part2 = helper(k-1-i)
                sum += part1 * part2
            table[k] = sum
            return table[k]
        
        return helper(n)
