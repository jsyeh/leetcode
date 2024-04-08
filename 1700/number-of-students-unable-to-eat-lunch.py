# 有幾位同學沒辦法吃午餐?
# 餐廳有提供 圓形0、方形1 的三明治, 同學也有各個自喜歡的三明治
# 規則: 學生排隊, 如果三明治喜歡就拿走, 不喜歡, 就再重新排隊
# 一直持續, 直到沒辦法再拿為止。
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students) # 先把學生變成排隊的格式, 照著模擬
        food = deque(sandwiches) # 因 sandwiches[0]表示最上面, 與 list 不同, 要改一下
        happy = True # 用來控制迴圈的變數
        while happy: # 只要上一輪裡, 有任一個人開心, 就有進展, 繼續值
            happy = False # 目前還沒有人開心
            for i in range(len(queue)):
                now = queue.popleft()
                if now == food[0]: # 現在的學生,喜歡最上面的食物, 配對成功
                    food.popleft() # 學生拿走這個三明治
                    happy = True # 有人開心了, 很好
                else: # 不喜歡
                    queue.append(now) # 學生重新去排隊
        return len(queue) # 剩下幾位學生 在隊伍裡不開心
