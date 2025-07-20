# LeetCode 1948. Delete Duplicate Folders in System
# 把檔案系統裡「重覆的folder(名字不同，但內容相同)」刪掉。如何判斷 subtree 一模一樣？可用 serialization 也就是把 tree 變字串
class Node:  # 用來建出 tree 的資料結構
    def __init__(self):
        self.child = defaultdict(Node)  # 每個 node 都有它的child對照表
        self.duplicate = False  # 這個 node 有重覆嗎？（一開始都沒重覆，之後會檢查是否重覆）
class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Node()  # 步驟1: 一開始，要將 paths 變成 tree 的資料結構
        for path in sorted(paths):  # 排序後的 for 迴圈
            node = root  # 從 root 出發
            for now in path:  # 往下「一層層」走完path
                node = node.child[now]  # 同時 path 走過、建出對應的 tree 結構（的那一條）
        pattern = defaultdict(list)
        def helperBuildKey(node):  # 步驟2: 將 node 的 subtree 函式呼叫函式，全部的都編碼、變成 key 字串
            key = '('  # 開頭是圓括號
            for c in node.child:
                key += c + helperBuildKey(node.child[c])  # 把 tree 變成字串，每個 child 再生出字串
            key += ')'  # 結束是圓括號。建出的 key 字串像是 (a(b())c(b())d(a())) 代表「a下面有b」「c下面有b」「d下面有a」
            if key != '()': pattern[key].append(node)  # 若不是 leaf node，就是 subtree 要記錄 pattern key
            return key  # 函式呼叫函式 的回傳值，用來慢慢組合、建出 key 字串
        helperBuildKey(root)  # 步驟2: 「函式呼叫函式」將 tree 的每個 subtree 對應的 key 加入 pattern
        # 步驟3: 找出所有 duplicate 的 nodes
        for nodes in pattern.values():  # 檢查 pattern 裡面的 key 是否有重覆的 nodes
            if len(nodes) > 1:  # 哦！有重覆！也就是「不只一個對應的 node」
                for node in nodes: node.duplicate = True  # 標示好，把「重覆的 nodes」都標成「重覆」，步驟4會刪掉它
        ans = []  # 步驟4: 用「函式呼叫函式」把「不重覆」的 nodes 放入答案（也就是「重覆的 nodes」都刪掉）
        def helperKillDuplicate(node, path):
            for now in node.child:
                if not node.child[now].duplicate:  # 沒有重覆，就繼續「函式呼叫函式」
                    helperKillDuplicate(node.child[now], path + [now])
            if path: ans.append(path)
        helperKillDuplicate(root, [])  # 步驟4: 用「函式呼叫函式」完成任務
        return ans
