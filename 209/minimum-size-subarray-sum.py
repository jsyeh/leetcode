class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums)
        left, right = 0, 0 # 右不包含，所以目前是空,sum=0
        sum, ans = 0, 0
        while left<=right:
            # print(left, right)
            sum += nums[right] # 更新 sum 值
            right += 1 # right右移後，可能下次就會離開這層迴圈了

            while sum >= target: # 如果合乎題目要求
                # ans==0表示還沒存過答案、right-left<ans表示更好
                if ans==0 or right-left<ans:
                    ans = right-left # 更新，右不包含
                sum -= nums[left] # 試著左邊吐出1個數
                left += 1
            # 離開上面迴圈時，sum<target，又將是個新的開始
            if left>=N or right>=N: # 如果left 或 right 超過範圍
                break # 就離開迴圈
        return ans
