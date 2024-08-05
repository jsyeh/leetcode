# LeetCode 2053. Kth Distinct String in an Array
# 找出「第k個」單獨的數（也就是，不是「只出現一次」的數，當作沒看到）
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr) # 先統計字出現的次數
        for now in counter:  # counter 裡會照原本順序存起來
            if counter[now]==1:  # 遇到「只出現一次」的數
                k -= 1  # 就減少k
            if k==0: return now # 用完k時，就是找到題目要的第k個數字
        return "" # 如果找不到，就回傳「空字串」
