# 3068. Find the Maximum Sum of Node Values
# 這個題目標示 Hard 看起來好難，尤其是一堆英文，而且 Examples 又看不懂
# 後來，靜下心來，把英文的描述，找重點看，看到 nums[u] = nums[u] XOR k
# 了解這是「計算機概論」二進位的 bit 運算 XOR 會變來變去
# 然後看懂題目，原來是每個 node 的數字，需要時可變另一個數。
# 那「每個node都有2種可能的數值」，怎麼「加起來最大」呢？
# Description 的 Hint 1,2,3越看越複雜，但 Hint 4 說，簡單把大的加起來就好了
# 但直接「每個數字挑大的」加起來，答案可能會稍大。看了 lee215 的解法，說「只能偶數個」XOR
# 所以，把 XOR 的總數數一數，若是奇數次的話，要把「最小的差距」扣掉即可
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        ans, move = 0, 0  # 多1個變數 move 記錄「XOR了幾次」
        min_diff = inf  # 每次 XOR 時，會增加的值，最少是多少（供最後修正用的）
        for num in nums:
            if num ^ k > num:
                num = num ^ k
                move += 1  # 又做了1次 XOR，最後只能偶數次
            min_diff = min(min_diff, abs((num^k) - num))
            ans += num
        if move % 2 == 1: ans -= min_diff  # 修正多做的那1次
        return ans
