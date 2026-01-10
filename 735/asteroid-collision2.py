# LeetCode 735. Asteroid Collision
# 有一行小行星 asteroids，裡面有「大小」及「行進方向」
# 全部等速移動，相撞時，小的會消失；兩個一樣大時，都會消失
# 問最後剩下哪幾個小行星還在。
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            # 下面不用 if 而用 while 因為要一直相撞測試
            while stack and stack[-1]>0 and a < 0: # 會相撞
                if stack[-1] == -a: 
                    stack.pop()  # 相同，都消失
                    break  # 右邊消失，會break
                elif stack[-1] < -a:  # 右邊的大，取代左邊
                    stack.pop()  # 左邊消失，右邊沒消失、沒break、繼續撞
                else:  # 左邊的大，右邊a消失，可離開 while 迴圈
                    break  # 右邊消失，會break
            else: stack.append(a)  # 沒有 break 表示「右邊沒消失」要append()
        return stack
