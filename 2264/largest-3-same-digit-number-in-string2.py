# LeetCode 2264. Largest 3-Same-Digit Number in String
# 字串裡有一堆數字，請問「組出的連續3個數字」最大是多少？
# 也就字串裡有沒有出現 '999', '888', ... '000' 之類的數
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""  # 如果沒有找到，就回傳「空字串」
        for i in range(len(num)-2):  # 用 for 迴圈逐一找
            if num[i]==num[i+1]==num[i+2]:  # 若連續3個字母相同
                if ans=="" or ans[0] < num[i]:  # 之前沒答案 or 「現在更大」
                    ans = num[i:i+3]  # 就把「現在更大」的連續3個字母當答案
        return ans
