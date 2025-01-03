# LeetCode 2571. Minimum Operations to Reduce an Integer to 0
# 目標：把n變成0，每次可把數字「加減」2的i次方。像 1,2,4,8,16,32,...
# 看到 lee215 的解說，可用 bit 來想：最低1個1的話，就消掉。很多1個的話，就+1大量進位。
class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        while n>0:  # 還有剩下bit
            if n%4==1:  # 看末2位，只有單1個1，（花1步）消滅它
                n //= 4
                ans += 1  # 花費一步
            elif n%2==0:  # 末位是0，直接移掉，免負擔
                n //= 2
            elif n%2==1:  # 可能有很多個1結尾，+1後可進位
                n += 1
                ans += 1 # 花費一步
        return ans
