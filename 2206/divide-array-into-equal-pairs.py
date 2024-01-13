# nums[i] 能否「兩兩一組」分光光？
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums) # 統計 nums 出現狀況
        for k in counter: # 對每一個數
            if counter[k]%2==1: return False # 只要有落單，就失敗
        return True # 沒有失敗
