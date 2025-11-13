# LeetCode 1441. Build an Array With Stack Operations
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        s = []
        j = 0
        for i in range(1,n+1):
            if len(s) and s[-1] == target[-1]: break
            ans.append('Push')
            s.append(i)
            if j<len(target) and s[-1] != target[j]:
                ans.append('Pop')
                s.pop()
            else: j += 1
        return ans
