# 這題超簡單, 就使用剝皮法來解決。每次 %2 都要是 2的倍數,剝到剩1就可以結束True
# 無法是2的倍數時, 就False
# 等等, 這是是 Power of 4, 也就是每次要處理的是 4 的倍數
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0: 
            return False
        while n>1:
            if n%4!=0: return False
            n //= 4
        return True
# case 778/1061: -2147483648 遇到負數,就麻煩了。負數一定不是答案
# case 1061/1061: 0 原來它也不是答案
