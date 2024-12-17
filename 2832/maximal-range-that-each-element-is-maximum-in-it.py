# LeetCode 2832. Maximal Range That Each Element Is Maximum in It
# ans[i] 是 subarray 的最長長度，對應 nums[i] 是最大
# 可用 mono stack 來存「之前比你更大的值」
class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        monostack = []  # 裡面放 (index, val)
        ans = [0] * len(nums)
        nums.append(inf)  # 先放 inf 無限大，擋著
        for i,num in enumerate(nums):  # 依序處理
            while len(monostack)>0 and monostack[-1][1]<num: # 若有人比num小，持續清/更新舊資料
                index, val = monostack.pop()
                if len(monostack)>0:  # 回頭回去更新 ans[index]
                    ans[index] = i - monostack[-1][0] - 1 # 右邊界-左邊界 - 1
                else: # 回頭回去更新 ans[index] 
                    ans[index] = i # 現在i成為之前index的右邊界，沒有左邊界
            monostack.append((i,num))
        return ans

