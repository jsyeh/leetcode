# LeetCode 2444. Count Subarrays With Fixed Bounds
# 數一數「有幾個 subarray」剛好有 最小值minK ... 最大值maxK 
# 可用「毛毛蟲」來決定「在範圍內」的長度極值
# 有3種尾巴：tailBad, tailHigh, tailLow 對應「失敗」「剛好是maxK」「剛好是minK」
# 答案 += tailBad ... min(tailHigh, tailLow) 合理的尾巴的可能個數
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        tailBad = tailHigh = tailLow = -1  # 一開始之前，都在左邊的左邊
        for head in range(len(nums)):  # 毛毛蟲「右邊的頭」
            if nums[head] < minK or nums[head] > maxK:  # 超過範圍
                tailBad = head  # 壞掉的尾巴
            if nums[head] == minK:  # 剛好是「minK 最小值」
                tailLow = head  # 標示「剛好是 minK 最小值」的尾巴
            if nums[head] == maxK:  # 標示「剛好是 maxK 最大值」的尾巴
                tailHigh = head  # 剛好是「maxK 最大值」
            # bad...high...llow...head
            #    ^^^^ possible 可能的範圍
            # bad...low...high...head
            #    ^^^& possible 可能的範圍
            possible = min(tailLow, tailHigh) - tailBad  # 頭在 head 時，有幾種合理的尾巴位置
            if possible>0: ans += possible  # 必須是「正數」才能加入答案中
        return ans

