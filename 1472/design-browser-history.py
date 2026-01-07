# LeetCode 1472. Design Browser History
# 實作 visit() back() forward() 模擬 browser 的瀏覽歷史記錄
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]  # 最早的頁面
        self.I = 0  # 陣列從0開始

    def visit(self, url: str) -> None:
        while self.I < len(self.history) - 1:  # 現在不在最後面
            self.history.pop()  # 後面的記錄，要先刪掉
        self.history.append(url)  # 再把現在的網址塞入
        self.I += 1  # 往右多了1格

    def back(self, steps: int) -> str:
        if steps > self.I:  # 要 back 太多步
            self.I = 0  # 就限定只能回到第0步
        else:  # 可以全部 back
            self.I -= steps  # 就直接 back 這麼多步
        return self.history[self.I]

    def forward(self, steps: int) -> str:
        if self.I + steps >= len(self.history):  # 沒辦法太後面
            self.I = len(self.history) - 1
        else:  # 可以順利 forward
            self.I += steps  # 就 forward 這麼多步
        return self.history[self.I]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
