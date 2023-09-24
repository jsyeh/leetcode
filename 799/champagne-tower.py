# 看起來就好像 binary search 的題目。或著是用公式解的題目。
# 先了解有幾杯是滿的（滿的到第幾個row），接下來多的杯子，分成 n個位置溢出。
# 再看 query_glass 會收到幾個溢出，便能知道 more/n 或 2*more/n 的量
# 但後來越寫越複雜，所以偷看別人的答案，發現「直接模擬」倒酒的過程，更簡單
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        cup = [[0]*101 for _ in range(101)] # cup[i][j]
        cup[0][0] = poured

        for i in range(100):
            for j in range(i+1):
                if cup[i][j]>1:
                    extra = cup[i][j]-1
                    cup[i+1][j] += extra/2
                    cup[i+1][j+1] += extra/2
                    cup[i][j] = 1
        
        return cup[query_row][query_glass]

        '''
        # 下面的程式還是有錯。
        if poured==0: return 0 # 漏寫這行，就會 divided by zero
        # 很像三角形/梯形的面積，就用梯形公式
        def area(level: index) -> int: # 1-index
            return (level+1)*level//2
        
        left, right = 0, poured

        while left<right:
            mid = (left+right)//2
            # print(left, right, mid, poured)
            if area(mid)<poured:
                left = mid+1
            else:
                right = mid
        print(left, right, mid, poured, area(left))
        if area(left)!=poured:
            left -= 1
        filled = area(left) # left is 1-index
        extra = poured - filled
        # print(filled, 'extra:', extra, 'left:', left)
        if query_row<left:
            return 1
        if query_row==left:
            if query_glass==0 or query_glass==left: # 邊緣杯
                return extra/(left*2)
            else:
                return extra*2/(left*2)
        return 0
        '''
# case 140/312: 25 6 1
