# LeetCode 735. Asteroid Collision
# 有一行小行星 asteroids，裡面有「大小」及「行進方向」
# 全部等速移動，相撞時，小的會消失；兩個一樣大時，都會消失
# 問最後剩下哪幾個小行星還在。
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for aster in asteroids:
            if aster<0:  # 往左飛
                while len(ans)>0 and ans[-1]>0:  # 會相撞
                    if abs(ans[-1]) == abs(aster): # 都消失
                        ans.pop()
                        break
                    elif abs(ans[-1]) < abs(aster): # 右大
                        ans.pop()
                        if len(ans)==0 or ans[-1]<0:
                            ans.append(aster)
                            break
                        continue
                    else:  # 右小，aster 小行星被消滅
                        break
                else: ans.append(aster)
            else: 
                ans.append(aster)
        return ans
