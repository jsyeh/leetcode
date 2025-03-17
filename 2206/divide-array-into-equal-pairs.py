# LeetCode 2206. Divide Array Into Equal Pairs
# 將 nums 裡的數，相同的數「兩兩一組」分好，全部分完。
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)  # 統計 nums 出現狀況
        for k in counter:  # 對每一個數
            if counter[k]%2==1:
                return False  # 只要有落單，就失敗
        return True  # 沒有失敗
