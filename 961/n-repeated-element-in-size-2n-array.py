# LeetCode 961. N-Repeated Element in Size 2N Array
# 在 nums 陣列裡，有一半的數「不相同」、有一半的數「相同」，找出來。
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        table = set()  # 把出現過的數，放在 table 裡
        for num in nums:
            if num not in table:  # 之前沒出現過
                table.add(num)  # 就記在 table 裡
            else:  # 那如果有出現過的話
                return num  # 那這個數就是那個「相同」的數
