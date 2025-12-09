# LeetCode 3583. Count Special Triplets
# 挑選 0 <= i < j < k < n 希望左邊nums[i]及右邊nums[k]是中間nums[j]的兩倍
# ex. nums: 6,3,6 就有一組。問「總共有幾組 i,j,k」
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9+7  # 答案會太大，要取餘數
        N = len(nums)  # 陣列大小，方便建（左到右、右到左）count 陣列
        countDoubleLeft = [0]*N  # 左到右，記錄「中間的數」左邊出現幾次「兩倍」
        # countDoubleRight = [0]*N  # 這個陣列可不用宣告、省空間

        counter = Counter() 
        for i in range(N):  # 左到右，能查看「左邊」有幾個「兩倍」
            now = nums[i]
            countDoubleLeft[i] = counter[now*2]  # 需要用這個陣列，供下面迴圈查表
            counter[now] += 1  # 順手記下「這個數」出現1次
        
        ans = 0
        counter = Counter()  # 新的 counter 計算「右到左」
        for i in range(N-1,-1,-1):  # 右到左，能查看「右邊」有幾個「兩倍」
            now = nums[i]
            # countDoubleRight[i] = counter[now*2]  # 可不用這個陣列、省空間
            # ans = (ans + countDoubleLeft[i] * countDoubleRight[i]) % MOD
            rightCount = counter[now*2]  # 改用這個變數
            ans = (ans + countDoubleLeft[i] * rightCount) % MOD  # 改用這個變數
            counter[now] += 1  # 順手記下「這個數」出現1次
        return ans
