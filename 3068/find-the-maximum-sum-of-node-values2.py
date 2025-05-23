# LeetCode 3068. Find the Maximum Sum of Node Values
# 每次，可挑某個 edge，把2端node都經過 XOR k 運算
# 其實就是每次挑2個，一起 XOR 看能抬昇多少（tree結構一點都不重要）
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        ans = 0  # 放「加總」的結果
        min_diff = inf  # 會存放「最小的變化量」abs(num - (num ^ k))
        up = 0  # 抬昇幾次
        for num in nums:  # 每個數，逐一測試
            if num ^ k > num:  # 若 XOR 後「變大」，就 XOR
                num ^= k  # 讓數變大
                up += 1  # 有抬昇1次
            ans += num  # 加總的結果
            min_diff = min(min_diff, abs(num - (num ^ k)))  # 最小的變化量
        if up%2==0: return ans  # 若是「偶數」次抬昇，答案直接拿來用
        else: return ans - min_diff  # 最小的變化量「要扣掉」以湊齊「偶數」
