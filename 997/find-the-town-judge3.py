class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustCount = [0]*(n+1)
        for a,b in trust: # a信任b
            trustCount[b] += 1
            trustCount[a] = -1
        for i in range(1,n+1):
            if trustCount[i]==n-1: return i
        return -1
