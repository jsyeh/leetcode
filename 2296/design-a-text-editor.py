# LeetCode 2296. Design a Text Editor
# 可以插入、可以刪除字母，游標可以左移、右移。我之前用 Java 模擬，在 case 41/45 超過時間
# Vlad 建議「用兩字串 s1 和 s2」對應游標「前、後」 
class TextEditor:

    def __init__(self):
        self.s1, self.s2 = [], []

    def addText(self, text: str) -> None:
        for c in text:
            self.s1.append(c)

    def deleteText(self, k: int) -> int:
        L = min(len(self.s1), k)
        for i in range(L): self.s1.pop()
        return L

    def cursorLeft(self, k: int) -> str:
        L = min(len(self.s1), k)
        # https://stackoverflow.com/questions/12088089/python-list-concatenation-efficiency
        self.s2[0:0] = self.s1[-L:]
        self.s1[-L:] = []  #del self.s1[-L:]
        L = min(len(self.s1), 10)
        return ''.join(self.s1[-L:])

    def cursorRight(self, k: int) -> str:
        L = min(len(self.s2), k)
        for i in range(L):  # 這裡不能寫 self.s1[-1:-1] = self.s2[:L]
           self.s1.append(self.s2[i])
        self.s2[:L] = []
        L = min(len(self.s1), 10)
        return ''.join(self.s1[-L:])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
