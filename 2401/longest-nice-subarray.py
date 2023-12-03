# 題目找「連續的數」互相「AND」都是0
# 這題不能暴力試，因 10^5 * 10^5 要試太多會超時
# 觀察規律：AND的反過來是OR，聯集出「目前用到的bit」不能再用
# 可以用 two pointers 像毛毛蟲一樣的「儘量伸長」即是答案
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        i, j = 0, 1 # 左邊i 右邊j 左包含、右不包含
        bits = nums[0] # 先有個bit
        ans = 1 # 最少都有1當答案
        while j<N: # 右邊界還在範圍內
            # if bits & nums[j] == 0: # 很好，可以加
            #     bits = bits | nums[j] # 增加它
            # else: # 糟，要縮短左邊界
            #     while bits & nums[j] != 0: # 持續縮短
            #         bits = bits ^ nums[i] # 消掉i的bit
            #         i += 1 # 左界往右移
            #     bits = bits | nums[j]
            # 以上太複雜，改用下面的簡化寫法
            while bits & nums[j] !=0: # 如果不幸「不合格」，持續縮短
                bits = bits ^ nums[i] # # 消掉 nums[i] 的舊bit
                i += 1 # 左界右移
            bits = bits | nums[j] # 現在可以放心加入新bit
            j += 1 # 現在右界可以順利往右移1格,右j不包含，以便探索新世界
            ans = max(ans, j-i)
        return ans
