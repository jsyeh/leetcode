# LeetCode 2094. Finding 3-Digit Even Numbers
# 使用 digits 陣列裡數字 0...9, 組出3位數偶數, 再「小到大」排序。
# 若用 for 迴圈「依序測」，答案馬上就出來了
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        counter = Counter(list(map(str, digits)))  # 數字變字母, 再數一數
        ans = []  # 放「小到大」的答案
        for i in range(100, 999, 2):  # 把3位數偶數都試過
            cnt = Counter(list(str(i)))  # 數字變字母, 再數一數
            if cnt<=counter: ans.append(i)  # counter 數量夠, 就是答案
        return ans
