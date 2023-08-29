# 研究votrubac的解法，先把左端、右端的最長先找出來，
# 再逐一滑動比對，直到「能接起來」，再回傳「要刪掉幾個數」
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N = len(arr)
        left, right = N, 0 # 若全部都沒逆向，就會到底
        for i in range(1,N):
            if arr[i-1]>arr[i]: # 有逆向的話
                left = i-1 # 就記下逆向前的位置
                break
        if left==N: return 0 # 全部排序好，不用刪(0)即完成

        for i in range(N-2,-1,-1):
            if arr[i]>arr[i+1]: # 有逆向的話
                right = i+1 # 就記下逆向前的位置
                break

        ans = min(N-left, right) # 若只留最左 or 最右 
        for left2 in range(left+1): # 給定 left2
            while right < N and arr[left2]>arr[right]:
                right += 1 # 就往右移，直到底 or 不再逆向
            now = right - left2 - 1 # 這次要刪掉多少數字
            if now < ans: ans = now # 更少更好，就更新
        return ans
# case 105/118: [16,10,0,3,22,1,14,7,1,12,15]
# case 117/118: [58,68,54,45,52,21,33,35,54,22,58,13,67,31,25,66,27,75,57,81,30,44,22,45,34,21,8,11,82,60,37,35,3,44,31,80,40,74,1,2,47]
