# 可以想像成毛毛蟲：右邊往右伸，左邊往右縮
# 主要迴圈，是要「左邊往右縮」還是「右邊往右伸」呢？
# 我一開始試「左邊往右縮」當成主要迴圈，結果程式要多2個if
# 所以我就改成「右邊往右伸」當成主要迴圈
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0 # 會往右縮的左邊界
        p = 1 # 乘積
        ans = 0 # 有幾組答案
        for right in range(len(nums)):
            p *= nums[right] # 現在先「右邊往右伸」
            while p>=k and left<=right: # 太大的話，且還能左邊往右縮時
                p //= nums[left] # 再「左邊往右縮」
                left += 1 
            ans += right-left+1
        return ans

        ''' # 左邊往右縮 的方法，比較多邊界問題要處理
        for left in range(N):
            while right<N and p*nums[right]<k:
                p *= nums[right]
                right += 1
            if p<k: ans += right-left
            if left==right:
                p *= nums[right]
                right += 1
            p //= nums[left]
        return ans
        '''
