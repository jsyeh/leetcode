# 這題直接用build-in函式就行
# 不過我猜它想讓我們試binary切額的方法吧
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return pow(x,n)
# 刁鑽的測資
'''
2.00000
-2147483648
-1.00000
-2147483648
1.0000000000001
-2147483648
'''
