# 要加入 k 個（沒出現過的）正整數，且 total sum最小，回傳 k數的sum
# 因為k極大，所以不能逐項加。
# 其實可將 nums.sort()排序好，再看看 k項+nums[i]項，加到何時剛好達標
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = list(set(nums)) # 可以去除「重覆」的數
        nums.sort() # 把 nums 排序好，再逐項查看「大k」是否夠大
        print(nums)
        for i,n in enumerate(nums):
            if n>k+i: # 如果數字夠大，答案便含在裡面
                # 梯形公式：(上底+下底)*高//2 再扣到「nums[:i]」的數
                return (1+k+i)*(k+i)//2 - sum(nums[:i])
        N = len(nums) # 因k遠超過nums範圍，所以(大)梯形公式-nums和
        return (1+k+N)*(k+N)//2 - sum(nums)
# case 61/108: [96,44,99,25,61,84,88,18,19,33,60,86,52,19,32,47,35,50,94,17,29,98,22,21,72,100,40,84] k=35 
# 竟然 nums[i] 有重覆的數，導致公式有錯。應先把 nums 去除重覆的數
        ''' # 下面的解法會超時，所以重寫
        used = set(nums) # 使用過的數字，要避開
        ans = 0
        # 不能逐項加，因k有10^8這麼多!
        for i in range(1,len(nums)+k+1): # 最多可能要用到這麼多數
            # 從1開始，逐一試「有沒有用過」
            if i not in used: # 數字沒有被用過
                ans += i # 要加進來
                k -= 1 # k 用到1個囉
                if k==0: return ans # k個數字全部塞完，就結束了
# case 73/108: 超時 [1000000000] 100000000 要加太多數字
#其實不用逐項加哦！可能有公式可解
        '''
