# LeetCode 995. Minimum Number of K Consecutive Bit Flips
# 有一堆 bits 是0或1，可挑「k個bits」進行flip（變成1或0）
# 最後希望全部變成1，問需要幾次 k-bit flip 
# 可想像有個 sliding window 的寬度是k，再「從左到右」巡，就做完了
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        ans = 0  # 累積 flip 的次數
        flip, flip2 = 0, 0  # flip會累積，flip2是現在nums[i]是否要flip
        flipped = []  # 記錄「累積flip」的奇偶數
        for i, num in enumerate(nums): # 從左到右巡
            if i<k: flip2 = flip # 沒超過 sliding window 就不用減
            else: flip2 = flip ^ flipped[i-k]  # 應扣掉 i-k 的 flipped效果
            if nums[i] ^ flip2 == 0:  # 不能是0，但現在效果是0
                if len(nums) -i < k: # 剩下bit不夠「做一組flip」
                    return -1 # 就失敗了
                flip ^= 1 # 累積又做一次flip
                ans += 1 # 累積flip次數
            flipped.append(flip) # 備份歷史記錄
        return ans  # 累積flip次數
