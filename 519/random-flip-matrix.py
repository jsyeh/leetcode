# m,n <= 10^4 很大的矩陣，都是0。每次flip()隨便挑個座標回傳&設為1
# 因矩陣很大，不要「真的」建陣列。反正flip()及reset()只呼叫1000次
# (x) 我想直接「照順序」把座標送出來即可。不幸「無法通過」要random
# Solutions oa5cuxe0To3 提到 Fisher–Yates shuffle
# https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#Examples
# 它的概念是：亂數挑 1...total 之間數，把數移到右邊（別再用）
# 但陣列無法開太大 10^8 所以它用 map 把用過的數標示，以便快速對照
# 可用 dict 做這個對照表
class Solution:

    def __init__(self, m: int, n: int):
        self.m, self.n = m, n # 記下 m, n
        self.total = m * n
        self.map = {} # 用過的對照表

    def flip(self) -> List[int]:
        # self.used += 1 # 使用的數字「多1個」 下面找出對應的座標
        # return [(self.used-1)//self.n, (self.used-1)%self.n]
        # 上面是錯的方法，下面是 Fisher-Yates shuffle 法
        choose = randrange(self.total) # 亂數挑的位置

        last = self.total - 1 # 挑（最右邊）最後1筆
        if last in self.map: # 若有被轉換過
            last = self.map[last] # 就照轉換過的來用

        if choose in self.map: # 若挑選的位置曾被用過
            ans = self.map[choose] # 放對應的值
            self.map[choose] = last # 把最右邊移來放此處
            # 交換，並讓 ans 可回傳         
        else: # 若未被用過，就簡單移來放，並把ans原數回傳即可
            ans = choose # 沒有對應，就挑的值本身即可
            self.map[choose] = last # 把最右邊移來放此處
        self.total -= 1 # 用掉1數，上限-1
        print(choose, ans, last, self.map)
        return [ans//self.n, ans%self.n]

    def reset(self) -> None:
        self.total = self.m * self.n
        self.map = {}

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
# case 18/20: 裡面有1000個 reset() flip() 一直呼叫。我都給[0,0]但不行
# case 10/20: ["Solution","flip","flip","flip","flip"] [[2,2],[],[],[],[]]
# 我不小心重覆輸出同一座標！
# case 12/20: ["Solution","flip","flip","flip","reset","flip"] [[3,1],[],[],[],[],[]]
