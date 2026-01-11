# LeetCode 208. Implement Trie (Prefix Tree)
# 要建出 trie 的資料結構，每個node裡有 child nodes
class Trie:

    def __init__(self):
        self.root = defaultdict(list)

    def insert(self, word: str) -> None:
        now = self.root
        for c in word:
            if c not in now:
                now[c] = defaultdict(list)
            now = now[c]
        now[''] = word  # 最後的字

    def search(self, word: str) -> bool:
        now = self.root
        for c in word:
            if c not in now: return False
            now = now[c]
        return now[''] == word

    def startsWith(self, prefix: str) -> bool:
        now = self.root
        for c in prefix:
            if c not in now: return False
            now = now[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
