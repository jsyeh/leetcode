# LeetCode 2929. Distribute Candies Among Children II
# n 個糖果分給3個小朋友，有幾種分法，能讓小朋友「不會拿超過limit個糖果」
# 因為數字很大，無法利用 2層迴圈 or 3層迴圈來解。能用1層迴圈解出來嗎？
# 第1個小朋友可拿 i 個糖果， 0 <= i <= min(limit, n) 個糖果
# 第2個小朋友可拿 j 個糖果， 0 <= j <= limit 且 i + j <= n，即 j <= n - i
# 第3個小朋友可能 n - i - j 個糖果， 0 <= n - i - j <= limit
# 移項變號，從第2條規則，知道 j 的上界是 limit 或 n - i 
# 從第2條 & 第3條規則，知道 j 的下界是 0 或 n - i - limit
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(min(limit, n)+1):
            # j 有哪些可能，就是答案。j 的最大值是 n - i 或  
            # j 的最小值是 0 或 n - i - limit
            # 答案就是 最大值 - 最小值 + 1
            if n - i > 2 * limit: continue  # j 的糖果數量 不能 > limit
            ans += min(n - i, limit) - max(0, n - i - limit) + 1
        return ans
