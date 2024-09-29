# LeetCode 432. All O`one Data Structure
# 設計 AllOne 資料結構：題目 All O'one 是指全部的操作，都要在O(1)時間內做到，好像很難，尤其是找最大key、最小key。
# 看了 Editorial 的解法，突然發現「好像沒那麼難」，只要在「雙向linked list」裡，能加減node，配合 HashMap 就做完了。
class Node:  # 用來放 linked list 的1個node
    def __init__(self,freq): # ex. Node(7)表示頻率為7的nodes，裡面可裝許多key
        self.left = None  # 一開始：左邊還沒接好
        self.right = None  # 一開始：右邊也還沒接好
        self.keys = set()  # 可裝許多key
        self.freq = freq

class AllOne:
    def __init__(self):
        self.head = Node(0)  # 頻率0的node，右邊會接「最小值」
        self.tail = Node(0)  # 頻率0的node，左邊會接「最大值」
        self.head.right = self.tail  # 左右接起來
        self.tail.left = self.head  # 左右接起來
        self.nodes = {}  # 完整對照表，使用 HashMap 字典 node[key] 對應到 Node，裡面有freq及keys等資訊

    def inc(self, key: str) -> None:  # key 增加1次
        if key in self.nodes:  # 有出現過，就把它搬家/右移
            node = self.nodes[key]  # key字串，對應的node
            freq = node.freq  # 取出「舊的freq值」
            node.keys.remove(key)  # 要搬家，舊家的戶籍要刪掉
            if node.right.freq==freq+1 and node.right != self.tail: # 右邊「剛好有個freq+1的家」
                node.right.keys.add(key)  # 剛好有、移過去，就好了
                node = node.right  # 現在的主角
            else:  # 剛好沒有，就建「新房子」
                left, node, right = node, Node(freq+1), node.right  # 要插入 freq+1 的「新房子」
                # 一口氣，把「雙向linked list」新增時，4個箭頭「一次更新」
                left.right, node.left, node.right, right.left = node, left, right, node
                node.keys.add(key)
            self.nodes[key] = node  # 最後住址改成「新家」
            if len(node.left.keys)==0 and node.left != self.head:  # 但是如果原來的點(舊家)戶口裡沒人，那怎麼辦？要刪掉它
                left, right = node.left.left, node
                left.right, right.left = right, left
        else:  # 此key沒有出現過，那要從「最左邊」誕生（將對應「出現1次」）
            if self.head.right.freq == 1: # 先看看「最左邊」freq是不是1
                node = self.head.right  # 要更新的 node
                node.keys.add(key)
            else:  # 沒有1能用，就要建新房子
                left, node, right = self.head, Node(1), self.head.right  # 要處理的3個nodes
                left.right, node.left, node.right, right.left = node, left, right, node
                node.keys.add(key)
            self.nodes[key] = node  # 住址在這裡

    def dec(self, key: str) -> None:  # key 減少1次
        node = self.nodes[key]  # 取得對應的 node
        freq = node.freq  # 取得舊的出現次數
        node.keys.remove(key)  # 將 key 從舊家移除（戶藉從舊家移出）
        if node.left.freq == freq-1:  # 如果 freq-1 剛好存在
            node.left.keys.add(key)  # 太好了，直接搬
            node = node.left  # 主角現在的位置
        else: # 不存在舊的 node 能用，只能新創1個
            left, node, right = node.left, Node(freq-1), node  # 左、中、右，準備好
            left.right, node.left, node.right, right.left = node, left, right, node
            node.keys.add(key)
        self.nodes[key] = node
        if len(node.right.keys) == 0 and node.right != self.tail:  # 如果舊家沒有人了
            left, right = node, node.right.right
            left.right, right.left = right, left

    def getMaxKey(self) -> str:
        if self.tail.left==self.head: return '' # 沒有東西
        return next(iter(self.tail.left.keys))  # 最右邊的最大值(的其中1個)
        # 找到「set裡」任1個的方法 next(iter(某個set)) https://stackoverflow.com/questions/59825/how-to-retrieve-an-element-from-a-set-without-removing-it

    def getMinKey(self) -> str:
        if self.head.right == self.tail: return '' # 沒有東西
        return next(iter(self.head.right.keys))  # 最左邊的最小值(的其中1個)


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
