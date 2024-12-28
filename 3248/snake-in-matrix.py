# LeetCode 3248. Snake in Matrix
# n x n 的正方形（矩陣）一開始在左上角，commands 移動方向，問最後位置
class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i, j = 0, 0  # 一開始的座標
        for command in commands:
            if command=='UP': i -= 1
            elif command=='RIGHT': j += 1
            elif command=='DOWN': i += 1
            elif command=='LEFT': j -= 1
        return i * n + j  # 換算這個座標「對應」的數字

