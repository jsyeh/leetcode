class MyQueue:

    def __init__(self):
        self.stack1 = [] # 用來放加入的東西
        self.stack2 = [] # 要取出時，從這裡取出

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        # 要取出時比較麻煩，要先倒入 stack2、取出最後1個、再倒回stack1
        while len(self.stack1)>0:
            self.stack2.append(self.stack1.pop())
        ans = self.stack2.pop()
        while len(self.stack2)>0:
            self.stack1.append(self.stack2.pop())
        return ans

    def peek(self) -> int: 
        # 因為 All the calls to pop and peek are valid.
        # 所以不用擔心當機
        return self.stack1[0]

    def empty(self) -> bool:
        return len(self.stack1)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
