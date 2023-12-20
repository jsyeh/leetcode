# 每個 move 可以把 n-1 個元素 +1
# 反過來說，就是可以把1個元素 -1
# 所以就看看最小值，每個人去減它，加總即可
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)
        # 全部加總 - 最小值*N
        # 也就是「比最小值」多出來的部分
        
