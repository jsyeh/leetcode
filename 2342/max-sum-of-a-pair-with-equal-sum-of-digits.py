# LeetCode 2342. Max Sum of a Pair With Equal Sum of Digits
# 把 nums[i] 「每個位數」加起來（ex. 2025 加起來變9）叫 Sum of Digits
# 若 nums[i] 和 nums[j] 的 Sum of Digits 相等，叫Equal Sum of Digits
# 想找 Equal Sum of Digits 的兩數「加起來最大」
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        SOD_best = {}  # Sum of Digts 對應的「原始數」最大值
        def SOD(num):  # 利用「函式呼叫函式」將「每個位數」加起來（使用剝皮法）
            if num==0: return 0  # 終止條件：把皮都剝光、沒有數了
            return num%10 + SOD(num//10)  # 再用「函式呼叫函式」剝完為止
        ans = -1
        for num in nums:
            now = SOD(num)
            if now in SOD_best: # 這個 SOD 曾經出現過
                prev_best = SOD_best[now]  # 之前對應的「最大」原始數
                ans = max(ans, num + prev_best)  # 更新答案
                SOD_best[now] = max(prev_best, num)  # 更新對應的「最大」原始數
            else:  # 這個 SOD 之前沒出現過
                SOD_best[now] = num  # 就第一次設定
        return ans
