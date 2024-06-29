# LeetCode 2192. All Ancestors of a Node in a Directed Acyclic Graph
# 題目給一堆 edges 裡面是連線的方向。要找到每個點的「所有可能上游/祖先」
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        A = defaultdict(list)  # A[b] 裡面會有 b 的可能祖先
        for a, b in edges:  # edges 裡有一堆 a 往 b 的連線
            A[b].append(a)  # a 可走到 b （b的祖先是a）
        
        ans = [ [] for i in range(n) ] # 用來放答案的「一堆list」
        for i in range(n):  # 逐一探討 node i 的祖先可能有誰
            stack = []  # 使用 stack 資料結構，用 DFS 找 nodei 可能的答案
            visited = set() # 走過的node不能再走
            stack.append(i) # 現在要解的目標是 node i
            while len(stack)>0:  # 只要stack裡，還有剩下東西
                now = stack.pop()  # 就再提出1個now來處理
                for another in A[now]:  # 再把提出來的那個now的上游/祖先another
                    if another not in visited:  # 只要沒有走過，就去走
                        visited.add(another)  # 標記走過
                        stack.append(another)  # 加入 stack
                        ans[i].append(another)  # 更新答案
            ans[i].sort() # node i 的答案，再照順序排序
        return ans
