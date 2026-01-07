# LeetCode 707. Design Linked List
# 實作 Linked List 的 get() addAtHead() addAtTail() addAtIndex()
# 因為可能 addAtIndex() 所以想到用 part1 和 part2 方便「插在中間」
class MyLinkedList:

    def __init__(self):
        self.part1 = deque()
        self.part2 = deque()

    def get(self, index: int) -> int:
        if index >= len(self.part1) + len(self.part2):
            return -1  # 超過範圍
        if index < len(self.part1):
            return self.part1[index]
        else:
            return self.part2[index-len(self.part1)]

    def addAtHead(self, val: int) -> None:
        self.part1.appendleft(val)

    def addAtTail(self, val: int) -> None:
        self.part2.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > len(self.part1) + len(self.part2):
            return  # 提早結束
        while index < len(self.part1):
            self.part2.appendleft(self.part1.pop())
        while index > len(self.part1):
            self.part1.append(self.part2.popleft())
        self.part1.append(val)

    def deleteAtIndex(self, index: int) -> None:
        if index >= len(self.part1) + len(self.part2):
            return  # 提早結束
        while index + 1 < len(self.part1):
            self.part2.appendleft(self.part1.pop())
        while index + 1 > len(self.part1):
            self.part1.append(self.part2.popleft())
        self.part1.pop()


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
