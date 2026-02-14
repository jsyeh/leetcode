# LeetCode 799. Champagne Tower
# 把酒杯堆成「2D香檳塔」疊成1杯、2杯、3杯等，杯子滿了會往「下層左右兩杯」流。
# 香檳倒的總量是 poured，問 query_row 的 query_glass 分到的香檳量
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        cup = [ [0]*i for i in range(1,102) ]  # 三角形的杯子塔，再大一點，才能「往下」平分
        cup[0][0] = poured  # 雖然可能很大，就照著放入，之後會「流到下面」
        # 最多 100 層杯子，杯子總數不多，可直接模擬
        for i in range(query_row+1):  # 第i層
            for j in range(i+1):  # 第j個杯子
                if cup[i][j]>1:  # 目前酒量超過1個杯子的容量
                    cup[i+1][j] += (cup[i][j]-1)/2  # 超過的部分「往下」平分
                    cup[i+1][j+1] += (cup[i][j]-1)/2  # 超過的部分「往下」平分
                    cup[i][j] = 1  # 杯子裡剩 1.0
                if (i,j)==(query_row, query_glass):  # 遇到「要問」的那個杯子
                    return cup[i][j]
