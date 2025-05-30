# LeetCode 2359. Find Closest Node to Given Two Nodes
# edges 記錄「node 向外走到哪裡」ex. edges[node1] 是 node1 下一步會到的 node
# 能從 node1 和 node2 出發，找出「最快相遇」的點(index要最小的)
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        p1, p2 = node1, node2  # 從 node1 和 node2 出發
        set1, set2 = set(), set()  # 記錄「分別走過」的 nodes

        while True:
            set1.add(p1)  # 走過
            set2.add(p2)  # 走過
            if p1 in set2 and p2 in set1:  # 同時走到「對方」的領地，就算「相遇」
                return min(p1, p2)  # (index要最小的)，當答案
            if p1 in set2: return p1  # p1 走入對方領地，這個地方是答案
            if p2 in set1: return p2  # p2 走入對方領地，這個地方是答案

            go = False  # 接下來「還能再走」嗎？
            if edges[p1] != -1 and edges[p1] not in set1:  # 「下一步」沒走過
                p1 = edges[p1]  # 可走到的下一步位置
                go = True  # 有「再走一步」
            if edges[p2] != -1 and edges[p2] not in set2:  # 「下一步」沒走過
                p2 = edges[p2]  # 可走到的下一步位置
                go = True  # 有「再走一步」
            if not go: return -1  # 如果無法「再走一步」，迴圈再也走不下去了，失敗

