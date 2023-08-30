# 模擬貪食蛇，如果吃了 food[i] 後，身體會變長，並跳出 food[i+1]
# food[i] 是 r,c （小心 width, height），四個方向 R,D,U,L
# The game is over if the snake goes out of bounds (hits a wall)
# or if its head occupies a space that its body occupies 
# 身體長長的，可使用 deque() 來放身體座標
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.food = food
        self.M, self.N = height, width
        self.i, self.j = 0, 0
        self.score = 0
        self.body = deque()

    def move(self, direction: str) -> int:
        if direction == "R":
            self.j += 1
        if direction == "D":
            self.i += 1
        if direction == "L":
            self.j -= 1
        if direction == "U":
            self.i -= 1
        if self.i < 0 or self.j < 0 or self.i >= self.M or self.j >= self.N:
            # 先測有沒有超過範圍。超過範圍，就完了
            return -1
        
        if self.score < len(self.food) and self.i == self.food[self.score][0] and self.j == self.food[self.score][1]:
            # 再測有沒有吃到food，吃到就不 popleft()
            self.score += 1

        #  If the game is over(碰到身體), return -1.
        for (i,j) in self.body:
            if i==self.i and j==self.j:
                return -1 # 碰到殘存的身體了 

        # 檢查沒問題時， append(現在座標)
        self.body.append((self.i, self.j))
        if len(self.body) > self.score:
            self.body.popleft()

        return self.score

# case 74/447: ["SnakeGame","move","move","move","move","move","move","move","move","move","move","move","move","move","move","move"]
# [[3,3,[[2,0],[0,0],[0,2],[0,1],[2,2],[0,1]]],["D"],["D"],["R"],["U"],["U"],["L"],["D"],["R"],["R"],["U"],["L"],["L"],["D"],["R"],["U"]]
# case 79/447: ["SnakeGame","move","move","move","move","move","move","move","move","move","move","move","move"]
# [[10000,10000,[[0,1],[0,2],[0,3],[0,4],[1,4],[2,4],[2,3],[2,2],[2,1],[2,0],[1,0]]],["R"],["R"],["R"],["R"],["D"],["D"],["L"],["L"],["L"],["L"],["U"],["U"]]

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
