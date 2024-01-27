# 利用 digits 裡的數字，組合出全部的「3位數」且是偶數
# 答案的數字需排序好。如果用「排列組合」來想，有點複雜。
# 但若用 for i in range(100,1000) 暴力測，好像答案馬上就出來了
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits = list(map(str, digits)) # 先把數字變成字串
        digits = Counter(digits) # 轉換成統計次數
        print(digits)
        ans = []
        for i in range(100,1000,2): # 全部可能的「3位數」偶數
            counter = Counter(str(i)) # 這是字串
            # print(counter)
            bad = False
            for d in counter: # 針對每一個數字，檢查是否夠用
                if d not in digits or digits[d]<counter[d]:
                    bad = True # 不存在 or 不夠用
            if not bad: # 沒有壞，能用
                ans.append(i)
        return ans
