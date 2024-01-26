# 找出「第k個」單獨的數
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr) # 先統計字出現的次數
        for now in arr:
            if counter[now]==1:
                k -= 1
            if k==0: return now # 找到第k個數字
        return "" # 如果找不到，就回傳「空字串」
