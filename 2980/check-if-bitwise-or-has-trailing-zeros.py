# LeetCode 2980. Check if Bitwise OR Has Trailing Zeros
# 找出 nums 裡，「有沒有機會」挑2個以上的數，互相 bitwise OR 會在右邊得到0
# 因 bitwise OR 運算，只有兩個數「最小位」「都是0」時，才能得到0
class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        even = 0  # 有幾個數的「結尾bit」是0，即「偶數」
        for num in nums:
            if num%2==0:  # 「結尾bit」是0，即「偶數」
                even += 1
                if even>=2: return True  # 收齊2個，即能成功
        return False  # 不夠用，就失敗了
