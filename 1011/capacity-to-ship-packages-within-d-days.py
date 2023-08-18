class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        N = len(weights) # 總貨物有N件
        M = max(weights) # 貨物最大有M，所以 shipCapacity不夠就爆了！
        def possible(shipCapacity: int) -> bool:
            # if shipCapacity<M: return False # 無法裝下最大的貨，就註定失敗
            ship = 1 # 用了幾艘船
            take = 0 # 載了多少貨，不能超過 shipCapacity
            for w in weights:
                if take + w <= shipCapacity:
                    take += w
                else: # 沒辦法裝下這一波 w
                    ship += 1 # 要增加1艘船，也就增加了1天
                    take = w # 載這個貨
                if ship>days: return False # 船爆了、天數爆了（超過天數）
            return True # 天數一直沒有爆，成功！

        total = sum(weights)
        left, right = M, total+1 # 最大那艘船的容量可以是 total，所以右界設 total+1
        while left<right:
            mid = (left+right)//2
            # print(left, right, mid, possible(mid))
            if not possible(mid):
                left = mid + 1 # 容量不夠，就加容量
            else:
                right = mid
        return left
