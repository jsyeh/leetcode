# 隨便找到 n 個(不同的)數字，讓它們加起來是 0
# 感覺有點太隨便了，好像隨便寫，答案就可以正確了 -- 直接正負數，就搞定了
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [] # 答案放這裡
        while n>0: # 只要還要挑數字
            if n==1: # 如果只能挑1個數字，那就挑0
                ans.append(0)
                break
            else: # 兩兩一數，插入正數、數負
                ans.append(n//2)
                ans.append(-(n//2))
                n -= 2
        return ans
