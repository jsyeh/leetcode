# LeetCode 2751. Robot Collisions 很多機器人互撞。一開始給你 positions[i] healths[i] directions[i] 是 Robot i 的資料
# 往右、往左的兩個機器人，會相撞，撞到時，healths值相同時，會「兩敗俱傷」, 如果 healths 值不同，那小的會消失，大的會「減1點」
# 這幾天的題目很像，都可用 Stack 實作。可想像成 左括號、右括號, 遇到對應括號，就要「對戰」不會太難。只是 Index 資訊要存起來
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = [[positions[i], healths[i], directions[i], i] for i in range(len(positions))] # 有 N 個機器人
        robots.sort() # 先把「分散」在各陣列的資料，合成一組一組的大資料，再以position[i] 來排序，以便「從左到右」依序處理
        stack = [] # 利用 list 來模擬 stack 資料結構
        for p, h, d, i in robots: # 以位置為準，從左到右，依序取出 p位置 h生命值 d方向 i機器人編號
            while len(stack)>0 and stack[-1][2]=='R' and d=='L' and h>0: # 只要還可對戰，就一直對戰
                if stack[-1][1]>h: # 左大
                    stack[-1][1] -= 1 # 左邊損1點
                    h = 0 # 右邊消滅
                elif stack[-1][1]<h: # 右大
                    stack.pop() # 左邊消滅
                    h -= 1 # 折損1點
                elif stack[-1][1]==h: # 一樣大
                    stack.pop() # 左邊消滅
                    h = 0 # 右邊也消滅
            if h>0: stack.append([p,h,d,i]) # 若右邊沒被消滅，就推入stack  
        stack.sort(key=lambda x:x[3]) # 以 robot 的 index 排序
        return [stack[i][1] for i in range(len(stack))] # 只回傳 health 值

