# 能成功找零錢的話，就會true。不能成功找零的話，就會false
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d5, d10, d20 = 0, 0, 0
        for n in bills:
            if n==5:
                d5 += 1
            elif n==10:
                if d5==0: return False # 無法找零
                else:
                    d10 += 1
                    d5 -= 1
            elif n==20:
                if d10>0 and d5>0:
                    d20 += 1
                    d10 -= 1
                    d5 -= 1
                elif d5>=3:
                    d20 += 1
                    d5 -= 3
                else:
                    return False # 無法找零
        return True
# [5,5,5,20]
