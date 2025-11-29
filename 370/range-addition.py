# LeetCode 370. Range Addition
# updates[i]=[left,right,inc] 會把 arr[left]...arr[right] 裡面的數，都 += inc
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        N = length
        diff = [0] * (N+1)
        for left,right,inc in updates:
            diff[left] += inc
            diff[right+1] -= inc
        now = 0
        ans = [0] * N
        for i in range(N):
            now += diff[i]
            ans[i] = now
        return ans
