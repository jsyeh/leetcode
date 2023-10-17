# node i 的 leftChild[i] 與 rightChild[i]
# return true if and only if all the given nodes form exactly one valid binary tree.
# valid binary tree 是什麼東西？ 意思是 它是 binary tree
# 如果有2個parent，就不是binary tree
# 如果有互連，就不是binary tree
# (再看Editorial解說)要全部連在一起、只能有1個root
# 所以應該 topology sort 便可以確認是否是 binary tree
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # 提示1:先找到root node (不是任何人的child)
        visited = [False]*n
        for child in leftChild:
            if child != -1: visited[child]=True
        for child in rightChild:
            if child != -1: visited[child]=True
        rootN = 0
        for i in range(n):
            if visited[i]==False:
                rootN+=1
                root = i
        if rootN!=1: return False

        # 提示2:找到root了，接下來可用DFS找它的小孩
        seen = set() # 希望DFS時，每個點只能走1次
        self.ans = True

        def dfs(root: int):
            if self.ans == False: return # 失敗就都提早結束了
            if root==-1: return
            if root in seen: # 點竟然被走過，便不是tree
                self.ans = False # 失敗
            seen.add(root) # 走過要標示
            dfs(leftChild[root]) # DFS 函式呼叫函式
            dfs(rightChild[root]) # DFS 函式呼叫函式
            
        dfs(root) # 真的去檢測
        if self.ans==False: return False # 有失敗，就False
        if len(seen)==n: return True # 都走過，就True
        else: return False # 沒全部走過，就False
# case 10/44: 5 [] [0,-1,3,1,3] [4,3,0,1,-1]
