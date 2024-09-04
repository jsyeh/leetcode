# LeetCode 874. Walking Robot Simulation
# 機器人一開始在(0,0)位置，command[i] -2:左轉 -1右轉 1..9前進
# 問「機器人最遠走多遠」，距離要記得「平方」 a*a+b*b=c*c 當結果
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        d = 0  # 0向北+Y，1向東+X，2向南-Y，3向西-X
        x, y = 0, 0  # 一開始的位置
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        obstacles = set([tuple(obstacle) for obstacle in obstacles])
        ans = 0
        for command in commands:
            if command==-2: d = (d+3)%4  # 左轉
            elif command==-1: d = (d+1)%4  # 右轉
            else:  # 前進
                for i in range(command):
                    x, y = x + dx[d], y + dy[d]
                    if (x,y) in obstacles:
                        x -= dx[d]
                        y -= dy[d]
                    ans = max(ans, x*x+y*y)
        return ans
