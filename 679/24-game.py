# LeetCode 679. 24 Game
# cards 裡有 4 張卡片，可能範圍 1...9，可調整順序、插入「加減乘除括號」
# 有沒有辦法「湊出」運算結果是 24 呢？
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def helper(nums):
            if len(nums)==1:  # 最後剩下1個數，就是「最後」運算結果
                return abs(nums[0]-24) < 0.000001  # 很接近24，就成功
            for a, b, *rest in permutations(nums):  # 排列組合，挑出前2項處理
                op = {a + b, a - b, a * b} # 把2項，「加減乘」
                if abs(b)>0.000001: op.add(a/b)  # 若分母不是0，可「除」
                for c in op:  # a 和 b 可結合成 c 的所有可能
                    if helper([c]+rest):  # 「函式呼叫函式」，少1項
                        return True  # 若能成功，那就成功
            return False  # 所有排列組合都不能成功，就失敗
        return helper(cards)
