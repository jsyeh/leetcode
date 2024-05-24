# LeetCode 2597. The Number of Beautiful Subsets
# 題目給個k，希望找到的 subset 裡各數的距離，不能 == k（我稍早錯看題目，以為是 <= k）
# 所以有數字出現時， +k -k 的兩數都要避掉
# subset 的問題，不能用暴力法去試，因為排列組合很多。
# 可試 Dynamic Programming 動態規劃，可把大問題，化成小問題來解
# lee215 給的解答，是先將數字分類、sort後，再用 198 House Robber 的 DP 法。不懂。
# shivamaggarwal513 提出的解法好像更清楚，直接「函式呼叫函式」慢慢往右解。
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        N = len(nums)
        freq = Counter()  # 用來統計 挑選的 nums[i] 出現幾次
        def helper(i):
            if i==N: return 1  # 成功走到最後，終止條件（空集合）是別人的基礎
            ans = helper(i+1)  # 問下一格的答案，也就是「不挑選」nums[i]
            # 那，能挑 nums[i] 這個數嗎？
            if freq[nums[i] - k]==0 and freq[nums[i] + k]==0:  # 敵對鄰居沒出現
                freq[nums[i]] += 1  # 就可挑選 nums[i] 這個數
                ans += helper(i+1)  # 放入 nums[i]後，再問一次答案
                freq[nums[i]] -= 1  # 再拿掉、不挑選
            return ans
        return helper(0) - 1  # 從0開始往右跑，但題目說，最後要扣掉空集合
