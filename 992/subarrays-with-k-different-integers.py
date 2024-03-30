# 有幾個substring，裡面湊齊「剛好」k個不同的字母
# 還是想到「毛毛蟲」的解法。但是我想到的方法，是「至少」k個不同字母，答案就錯了。
# lee215在Solutions裡說，其實就「至少k個」-「至少k-1個」就能得到「剛好k個」
# 有夠帥的作法，我試看看！不過我的程式架構要改成「至少k個」-「至少k+1個」
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        N = len(nums)
        def atMost(kk): # 因為要做2次，所以另外發明函式，簡化程式
            ans = 0 # 函式等一下的回傳值
            counter = collections.Counter() # 用 counter hashmap 來加速
            counterN = 0 # 用counterN 加速 len(counter)的計算
            left = 0
            for right in range(N): # 毛毛蟲的頭，逐步右移
                counter[nums[right]] += 1
                if counter[nums[right]]==1: 
                    counterN += 1 # 用counterN 加速 len(counter)的計算
                while counterN>=kk: #毛毛蟲的尾巴left將逐步右移
                    counter[nums[left]] -= 1
                    if counter[nums[left]]==0:
                        counterN -= 1 # 用counterN 加速 len(counter)的計算
                    left += 1 # 尾巴left逐步右移
                ans += left # 至少有kk個的可能性
            return ans
        return atMost(k) - atMost(k+1) # 「至少k個」-「至少k+1個」
        ''' # 這裡的 while len(counter+coolections.Counter())>=k 沒效率，重寫
        ans = 0
        counter = collections.Counter()
        left = 0
        for right in range(len(nums)):
            counter[nums[right]] += 1
            while len(counter+collections.Counter())>=k:
                counter[nums[left]] -= 1
                left += 1
            ans += left
        # 前面算出「至少k個」，再減掉下面「至少k+1個」就是答案了
        counter = collections.Counter()
        left = 0
        for right in range(len(nums)):
            counter[nums[right]] += 1
            while len(counter+collections.Counter())>=k+1:
                counter[nums[left]] -= 1
                left += 1
            ans -= left
        return ans
        '''
# case 40/55: 測資數目超多的，k是360，所以我的 counter 計算長度的部分要改方法
