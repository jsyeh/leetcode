# LeetCode 1304. Find N Unique Integers Sum up to Zero
# 隨便找到 n 個(不同的)數字，讓它們加起來是 0
# 感覺有點太隨便了，好像隨便寫，答案就可以正確了 -- 直接正負數，就搞定了
class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n%2==1:
            return [i for i in range( -n//2+1, n//2+1 )]
        else:
            return [i for i in range( -n+1, +n+1, 2)]

        if n%2==1:
            return [0] + [-i for i in range(1,n//2+1)] + [i for i in range(1,n//2+1)]
        else:
            return [-i for i in range(1,n//2+1)] + [i for i in range(1,n //2+1)]
