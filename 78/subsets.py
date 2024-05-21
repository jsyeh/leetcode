# LeetCode 78. Subsets
# 要把全部排列組合的可能，都return出來
# 和昨天的挑戰題類似，都有用到 bit mask 的技巧
# 也就是for迴圈的mask，bit是1代表挑選，剛好可對應「某一種挑選的組合」
# N 不超過 10 所以還好，不會超時。
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = []
        for mask in range(2**N):
            # mask 裡，某bit i 是1的話，代表要挑選它
            now = []
            for i in range(N):  # 查看 bit i
                if mask & (1 << i) != 0:  # 對應bit有亮起來
                    now.append(nums[i])
            ans.append(now)
        return ans

