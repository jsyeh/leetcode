# LeetCode 1381. Design a Stack With Increment Operation
# 設計資料結構：stack 的 push() pop() 外，再加 inc(k,val) 將最下面k個數，+val
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []  # 用 list 模擬「正常的 stack」
        self.diff = []  # 另外「供修改微調」的加總結果，放在 diff 裡，
        self.maxSize = maxSize  # stack 的大小範圍

    def push(self, x: int) -> None:
        if len(self.stack)>=self.maxSize: return  # 超過範圍
        self.stack.append(x)  # 加入新的項
        self.diff.append(0)  # 目前這項，沒有「供修改微調」的加總結果

    def pop(self) -> int:
        if len(self.stack)==0: return -1  # 超過範圍
        now = self.diff.pop()  # 吐出「供修改微調」的加總結果
        if len(self.diff)>0: self.diff[-1] += now  # 把「供修改微調」的加總結果，持續影響
        return self.stack.pop()+now  # 「供修改微調」的加總結果，套用到答案

    def increment(self, k: int, val: int) -> None:
        if len(self.diff)==0: return  # 空的，不要做任何事
        if k >= len(self.diff): self.diff[-1] += val  # 超過範圍
        else: self.diff[k-1] += val  # 修改「供修改微調」的加總結果


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
