# 每位小朋友都有 ratings[i]，要給candy：每人給1顆，rating高的要更多顆
# 請問最少需要幾個candy? 感覺 sorting 後，就可從小到大放candy數目
# 但是不對不對！題目是寫「要比鄰居高」只有鄰居相比。所以不能sorting
#「higher rating get more candies than their neighbors.」
# 所以模依 1145520074 的 Solution，左往右巡、（最重要的）再右往左巡
class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        candy = [1]*N # 全部都塞1 當基礎

        for i in range(1,N):
            if ratings[i-1] < ratings[i]: # 有更高（左往右看）
                candy[i] = candy[i-1] + 1 # 就只好多拿糖果
            # 否則的話，就是只有基礎款的1顆糖

        for i in range(N-1,0,-1):
            if ratings[i-1] > ratings[i]: # （右往左看）有更高
                candy[i-1] = max(candy[i]+1, candy[i-1])
                # 如果原來的更高，那就用原來的值就好
        # print(candy)
        return sum(candy)


        ''' 以下是錯誤的，重寫
        ratings.sort() # 先排序
        print(ratings)
        # 這題難在哪裡？可能是「數字太多」逐一算會超時吧
        N = len(ratings)
        candy = [1]*N
        ans = 0
        for i in range(1,N):
            if ratings[i-1]==ratings[i]:
                candy[i] = candy[i-1]
            else:
                candy[i] = candy[i-1] + 1
        print(candy)
        return sum(candy)
        '''

