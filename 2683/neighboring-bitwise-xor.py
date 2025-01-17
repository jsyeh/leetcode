# LeetCode 2683. Neighboring Bitwise XOR
# derived[i] = original[i] XOR original[i+1]）
# 給你 derived 問「有沒有可能」有這樣的 original 陣列。
# 因XOR 做兩次=沒做，所以 derived 全部 XOR 起來 = original 全部 XOR 做兩次 = 0
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        total = 0
        for num in derived:
            total ^= num
        # 最後，再看頭尾項，能不能相接
        return total == 0
