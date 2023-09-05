# 要建出 trie 的資料結構，每個node裡有 child nodes
class Trie:

    def __init__(self):
        self.H = {}
        # print(self.H)

    def insert(self, word: str) -> None:
        H = self.H
        for c in word:
            if c in H: # 這個字母在裡面
                H = H[c]
            else:
                H[c] = {}
                H = H[c]
        H["end"] = True
        # print(self.H)        
        return

    def search(self, word: str) -> bool:
        H = self.H
        for c in word:
            if c not in H: return False
            H = H[c]
        if "end" in H: return True
        return False

    def startsWith(self, prefix: str) -> bool:
        H = self.H
        for c in prefix:
            if c not in H: return False
            H = H[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
