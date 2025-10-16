# LeetCode 2598. Smallest Missing Non-negative Integer After Operations
# nums 陣列裡，每次可挑個數 +value 或 -value，找出「0開始漏掉最小的數」
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        nums = [(num+value)%value for num in nums]  # 先變 0~value-1 間的數
        counter = Counter(nums)  # 累積對應的數量
        for i in range(value):
            if counter[i]==0: return i  # 如果有缺的數，漏洞缺的就是它！

        target = min(counter.values())  # 找到關鍵的最小數量, 會有漏洞
        for i in range(value):  # 逐一檢查, 看「誰」是最小數量
            if counter[i] == target:  # 找到 i 符合「最小數量」
                return value * counter[i] + i  # 下次漏洞缺的就是它
