# 這題的解法，等價於：能接受 one 最多有一個 的 two-pointer 題目
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = 0, 0 # 右不包含
        zero, one, ans = 0, 0, 0
        while right<N: # 右邊還沒撞到邊界
            if nums[right]==1: # 是1，太好了
                right += 1
                one += 1
            elif nums[right]==0 and zero==0: # 是0也是可以啦，但只有1個quota
                right += 1
                zero += 1
            else: # 這是 zero超標的狀況
                right += 1
                zero += 1 # 很遺憾，現在 zero 超標了
                while zero > 1: # 只要超標，就持續吐出 nums[left]
                    if nums[left]==0:
                        zero -= 1 # 吐出 zero
                    else:
                        one -= 1 # 吐出 one
                    left += 1 # 吐出後，改變 left 的位置
            # print("left:", left, " right:", right, " zero:", zero, " one:", one)
            if one + zero > ans:
                ans = one + zero        
        return ans
