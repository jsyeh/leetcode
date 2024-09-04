# LeetCode 2069. Walking Robot Simulation II
# 原本的模擬 874. Walking Robot Simulation 進階，提供工具，讓別人呼叫
# 我原本寫的程式，是「一步步模擬」，好像太慢。其實「只會繞四周走」答案是固定的。
class Robot:
    def __init__(self, width: int, height: int):
        self.pos = []
        for x in range(1,width):  # 往東走
            self.pos.append([(x,0), 'East'])
        for y in range(1,height):  # 往北走
            self.pos.append([(width-1,y), 'North'])
        for x in range(width-2,-1,-1):  # 往西走
            self.pos.append([(x,height-1), 'West'])
        for y in range(height-2,-1,-1):  # 往南走
            self.pos.append([(0,y), 'South'])
        self.circle = len(self.pos)
        self.i = - 1  # 左下角的原點

    def step(self, num: int) -> None:
        num = num % self.circle # 為避免「超時」，所以「照著圓周」取「餘數」，直球對決
        self.i = (self.i + num) % self.circle

    def getPos(self) -> List[int]:
        return self.pos[self.i][0]

    def getDir(self) -> str:
        if self.i == -1: return 'East'  # 最一開始，是「向東」
        return self.pos[self.i][1]

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
# 最重要的例子：["Robot","getPos", "getDir", "step","getPos","getDir"]
# [[97,98],[],[],[66392],[],[]]
