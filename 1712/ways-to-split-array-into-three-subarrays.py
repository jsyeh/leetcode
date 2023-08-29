# 分3群: sum(left)<=sum(mid) and sum(mid)<=sum(right)
# sum(0,i)<=sum(i+1,j)的j 與 
#           sum(i+1,k-1)<=sum(k,n) 的 k 將決定ways數目
# 先用 running sum 來加速，再利用 binary search 來找「斷開點」
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        N = len(nums)
        runSum = [0]*N # runSum[i] 表示 num[0]...num[i-1]加起來
        runSum[0] = nums[0]
        for i in range(1,N):
            runSum[i] = nums[i] + runSum[i-1]
        
        ans = 0
        # 要找到2個值： sum(left)==sum(mid) 到 切一半 sum(mid)==sum(right)
        for i in range(N-2): # O(N)，決定第1刀切在哪裡
            # j 是左界，使得 runSum[j] >= 2*runSum[i]
            # k 是右界，使得 runSum[k]-runSum[i] <= runSum[N]-runSum[k]
            left, right = i+1, N
            while left<right:
                mid = (left+right)//2
                if runSum[mid] < 2*runSum[i]: # 不夠的話
                    left = mid + 1
                else:
                    right = mid
            j = left
            left, right = i+1, N-1 # 這裡改寫 N-1 以免滑到邊界外
            while left<right:
                mid = (left+right)//2
                if runSum[mid]-runSum[i] <= runSum[N-1]-runSum[mid]:
                    left = mid + 1
                else:
                    right = mid
            k = left
            print(i,j,k)
            if j<=k: 
                ans += k-j
        return ans % 1000000007
# case 86/89: 100000 個 0, 

