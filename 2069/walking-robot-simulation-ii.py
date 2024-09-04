# LeetCode 2069. Walking Robot Simulation II
# 原本的模擬 874. Walking Robot Simulation 進階，提供工具，讓別人呼叫
class Robot:
    def __init__(self, width: int, height: int):
        self.W, self.H, self.circle = width, height, (width-1+height-1)*2
        self.x = self.y = 0  # 一開始的位置
        self.d = 1  # 0北 1東 2南 3西，一開始「向東」
        self.dx, self.dy = [0, 1, 0, -1], [1, 0, -1, 0]  # 照著d方向，移動量

    def step(self, num: int) -> None:
        num = num % self.circle # 為避免「超時」，所以「照著圓周」取「餘數」，直球對決
        if num==0: num = self.circle # 前面取餘數，變成0的話，反而「沒有動」，所以「讓它繞一圈」
        for k in range(num):
            self.x += self.dx[self.d]
            self.y += self.dy[self.d]
            while self.x<0 or self.y<0 or self.x>=self.W or self.y>=self.H: # 撞到
                self.x -= self.dx[self.d]
                self.y -= self.dy[self.d]
                self.d = (self.d + 3) % 4
                self.x += self.dx[self.d]
                self.y += self.dy[self.d]

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        direction = ['North', 'East', 'South', 'West']
        return direction[self.d]
# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
# case 91/142: 有大量資料/步數很多，會超時
# case 140/142: 步數很多，且「真的分開很多步」
