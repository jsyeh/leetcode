# 規則：字串裡，只有數字的話，以10進位表示。不然就以「字串長度」來表示。
# 問 strs 裡最大數值是多少。就逐一處理即可
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = 0
        for s in strs: # 每個字串，逐一處理
            try: # 試試能不能將「字串s」轉成整數
                ans = max(ans, int(s)) # 能轉成整數，很好
            except: # 若不能轉成整數
                ans = max(ans, len(s)) # 就以「字串長度」來更新 ans
        return ans
