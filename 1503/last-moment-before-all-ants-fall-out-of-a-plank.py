class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left.sort() # 往左走,最右邊的left[-1]是關鍵
        right.sort() # 往右走，最左邊的right[0]是關鍵

        N1, N2 = len(left), len(right)

        if N1==0 and N2==0: # 台面上都沒有人在走
            return 0 # 就0秒達清「清台面」
        if N1==0 and N2!=0: # 只有往右走
            return n-right[0] # 關鍵的那個，離右邊界
        if N1!=0 and N2==0: # 只有往左走
            return left[-1] # 關鍵的那個的值，就是距離

        # 兩個方向都有的話，找最大值
        return max(left[-1] ,n-right[0])
        
