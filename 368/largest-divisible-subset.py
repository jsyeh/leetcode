# 要找「兩兩可以互除」的集合，找到最多數的那個集合
# 做個對照表 dict {} 裡面存 table.get(i) 得到 nums[i] 對應的set長度
# prev.get(i) 得到 nums[i] 對應的 prev 內容
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N = len(nums)
        list.sort(nums) # 先排序好，因為想要
        length = {} # length of the set
        prev = {} # previous one

        ansI = 0 # 最短的話，就 nums[i]
        for i in range(N):
            length[i] = 1 # 自己本身，長度一定是1
            prev[i] = -1 # 但它沒有 prev 
            for p in range(i-1, -1, -1): # for(p=i-1; p>=0; p--)
                if nums[i]%nums[p] == 0 and length[p] +1 > length[i]: 
                # 整除，而且更長的話，要串起來
                    length[i] = length[p] + 1
                    prev[i] = p
                    if length[i] > length[ansI]:
                        ansI = i # 因為i更長，更新 ansI
        ans = []
        while True: # 把 ans 逐一串接起來
            ans.append(nums[ansI])
            ansI = prev[ansI]
            if ansI == -1: break # 接地的話，就離開

        return ans
# case 46/49: [4,8,10,240]
