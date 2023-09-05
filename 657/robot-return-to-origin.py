class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y, dir = 0, 0, 0
        dx = {"R":1, "L":-1, "U":0, "D":0}
        dy = {"R":0, "L":0, "U":-1, "D":1}
        for m in moves:
            x += dx[m]
            y += dy[m]
        if x==0 and y==0: return True
        else: return False
