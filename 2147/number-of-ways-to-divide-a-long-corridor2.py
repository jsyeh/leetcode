# LeetCode 2147. Number of Ways to Divide a Long Corridor
# 長廊corridor裡，有許多「座位S、盆栽P」，用「屏風」隔開「剛好2個座位」
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seats = []
        for i in range(len(corridor)): 
            if corridor[i]=='S':
                seats.append(i)  # 記錄「座位S」的座標
        # 兩兩座位，不能接受「奇數座位、沒有座位」
        if len(seats)%2==1 or len(seats)==0: return 0  
        MOD = 10**9+7  # 數字會很大，要取餘數
        ans = 1
        for i in range(1, len(seats)-1, 2):  # 針對每兩個「座位S」
            # 乘上「中間」的「盆栽間隔數目」，便能知道「總共有幾種隔間法」
            ans = ans * (seats[i+1] - seats[i]) % MOD
        return ans
