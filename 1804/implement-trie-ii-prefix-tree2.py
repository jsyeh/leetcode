# LeetCode 1804. Implement Trie II (Prefix Tree)
# Trie 是 prefix tree，能知道word的前面字母相同的狀況(數量)
# 每一層可對應26個字母，將一堆words 變成一棵tree
class Node:
    def __init__(self):
        self.child = defaultdict(Node)
        self.prefixCount = 0
        self.endCount = 0

class Trie:

    def __init__(self):
        self.trie = Node() # root node

    def insert(self, word: str) -> None:
        now = self.trie
        for c in word:  # 逐個字母
            now = now.child[c]  # 在 trie 裡遊走
            now.prefixCount += 1  # 並更新 prefixCount
        now.endCount += 1  # 最後更新 endCount

    def countWordsEqualTo(self, word: str) -> int:
        now = self.trie
        for c in word:  # 逐個字母
            now = now.child[c]  # 在 trie 裡遊走
        return now.endCount  # 最後查看 endCount

    def countWordsStartingWith(self, prefix: str) -> int:
        now = self.trie
        for c in prefix:  # 逐個字母
            now = now.child[c]  # 在 trie 裡遊走
        return now.prefixCount  # 最後查看 prefixCount

    def erase(self, word: str) -> None:
        now = self.trie
        for c in word:  # 逐個字母
            now = now.child[c]  # 在 trie 裡遊走
            now.prefixCount -= 1  # 邊走邊更新 prefixCount
        now.endCount -= 1  # 最後更新 endCount

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
