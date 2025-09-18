# LeetCode 3408. Design Task Manager
# 設計資料結構、實作「工作管理員」依照 priority 調整工作
class TaskManager:
    # 一開始 tasks 裡會有一堆 [userId, taskId, priority]
    def __init__(self, tasks: List[List[int]]):
        self.userId = defaultdict(int)  # 設計好「資料結構」的3個表格
        self.priority = defaultdict(int)
        self.heap = []
        for userId, taskId, priority in tasks:  # 有很多工作
            self.add(userId, taskId, priority)  # 「加入」工作

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.userId[taskId] = userId  # 修改「資料結構」的3個表格
        self.priority[taskId] = priority
        heappush(self.heap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.priority[taskId] = newPriority  # 修改「資料結構」的3個表格之2
        heappush(self.heap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        self.priority[taskId] = inf  # heap裡「一定不會這麼大」保證不會執行

    def execTop(self) -> int:
        while len(self.heap):
            priority, taskId = heappop(self.heap)  # 小心，要再「負號」
            if self.priority[-taskId] == -priority:  # 這裡都有加「負號」很好！
                self.rmv(-taskId)  # 記得要先清掉這個task
                return self.userId[-taskId]  # 再回傳答案
        else: return -1  # 都個 heap 裡，都找不到「正確對應」的 task


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
