# LeetCode 260. Single Number III
# 今天題目, 要找出「只出現一次」的數字, 應有多種寫法
# 這裡使用 Python 字典 dict 來看「數字出現幾次」
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        table = {}  # 這個 table 裡, 放數字出現次數 (大括號是 Python 的字典)
        for num in nums:  # 針對每個數, 逐一分析
            if num not in table:  # 如果字典裡還沒有這個數字
                table[num] = 1  # 那就是第1次出現
            else:  # 如果之前有出現過
                table[num] += 1  # 就讓「出現次數」再+1
        ans = []  # 用來放答案
        for num in table:  # 針對 table 裡的每一個 key
            if table[num]==1:  # 如果對應的次數, 剛好是1, 就是題目要的數
                ans.append(num)  # 就把答案放入 ans 裡
        return ans  # 答案算完了, 真開心
