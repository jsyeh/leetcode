# 題目有點抽象：有個看不到的 nums 陣列，列出一些限制條件：
# n 表示 nums 的長度，nums[i] 都是正數，相鄰數字差-1，0，1
# 全部數字加起來，不會超過 maxSum，要找到（看不到的）最大值 nums[index] 的最大值
# 可以想像 nums[index] 像傘狀帳拉高，面積不能超過 maxSum 的情況下，最高可拉多高
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def triangle(n: int) -> int:
            return (1+n)*n//2
        def area(h: int) -> int: # 算面積有3種可能
            # 但是還有一㮔狀況沒考慮到，是要在地面鋪一堆1（因不能為0）
            # 所以要將整個值減1再算
            h = h - 1
            # 1(1), 1+2+1(4), 1+2+3+2+1(9), 1+2+3+4+3+2+1(16) 
            ans = h * h # 如果沒超過底面積，可將三角形，組成正方形
            if index < h - 1 : # 左半邊如果拉太高，左半邊會變成梯型，要扣除小三角形
                ans -= triangle(h-index-1)
            if (n-index) < h: # 右半邊如果拉太高，右半邊會變成梯形，要扣除小三角形
                ans -= triangle(h-(n-index))
            return ans + n
        print( area(2) )
        left, right = 0, maxSum+1 # 要加1
        while left<right:
            mid = (left+right)//2
            print(left, right, mid)
            if area(mid) == maxSum:
                return mid # 撞到答案，太好了
            if area(mid) < maxSum:
                left = mid + 1 # 不小心就超過了
            else:
                right = mid
        return left - 1 # 因為會超過，要再-1
# case 44/370: 1 0 24
# case 52/370: 9 0 90924720
# case 106/370: 6 2 931384943
# case 183/370: 4 0 4
