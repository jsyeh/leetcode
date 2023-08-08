# (1) 這是模擬題，看機器人會走到哪裡、向哪個方向
# (2) 是否會在有限的空間 vs. 是否會發散、到無限大的地方
# 其實看它的方向，如果方向有回來，就True。如果方向轉90度，也會是True
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dx = [1,0,-1,0] # 4個方向的移動
        dy = [0,1,0,-1] # 4個方向的移動
        x,y,dir = 0,0,0 # 初始位置、初始方向
        for c in instructions:
            if c == "L": dir = (dir+1)%4
            if c == "R": dir = (dir+3)%4
            if c == "G": 
                x += dx[dir]
                y += dy[dir]
        
        print(dir)
        if x==0 and y==0: return True # 留在原地的話，一定可以
        elif dir == 0: return False # 沒留在原地，而且向同一方向，將會持續移動
        else: return True # 只要轉動方向，就會循環
# case 105/117: "GLRLLGLL" 雖然方向沒改變，但是距離改變了哦！

