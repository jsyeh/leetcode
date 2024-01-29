class MyQueue:

    def __init__(self):
        self.input = [] # 進來的資料，會先放到input
        self.output = [] # 送出去前，「先倒到」output反向

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        if not self.output: # 若是空的，就把 input 全倒過來
            while self.input:
                self.output.append(self.input.pop())
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1] # 將來會被 pop 的那項

    def empty(self) -> bool:
        return not (self.input or self.output)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
