# LeetCode 330. Patching Array
# 要在 nums 裡，加入一些值，使得1...n的任何數字，都能用 nums[i] 加起來
# 這題我沒有解題的思緒，看付費的Editorial解釋，
# 「若miss缺某個數，那就要補它」，不管如何，都能「抬昇」下一個可能的洞
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # nums[i] 已經從小到大排好。現在要 patch 補洞
        ans = 0
        i = 0 # 從小到大，逐一補洞/提昇，先從 nums[0] 開始
        miss = 1  # 題目希望從1開始 1...n 逐一補起來，先檢查 1 這個數
        while miss <= n:  # 從 1...n 逐一檢查
            if i < len(nums) and nums[i] <= miss: # 剛好可補，洞「可再抬昇」
                miss += nums[i]  # nums[i] 可幫忙提昇「洞」候選人的高度
                i += 1  # 換下一個 nums[i]
            else: # 跳過去了、補不了洞，只要 ans+1 起來
                ans += 1  # 需要多一個數來補 （就是 miss 這個數）
                miss += miss  # 因為有了 miss 後，又「抬昇」到新的層次
        return ans  # 最後需要補的數有幾個

