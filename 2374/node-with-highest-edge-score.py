# edges[i] 表示 node i 指到的數字
# edge score[i] 是 sum of labels of node 指到 node i
# 所以就邊讀edges、邊加i，即可得到答案：找到score最高的i
# 如果 score相同時，index越小越好
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        score = defaultdict(int) # score[i]: node i 的分數
        ansI = 0 # 對應分數最高的 node i
        for i,dst in enumerate(edges): # 每個 edge 都去算
            score[dst] += i # 目標 dst 得到 i 分
            if score[dst]>score[ansI] or (score[dst]==score[ansI] and dst<ansI):
                ansI = dst # 如果是更好的答案，就更新
        return ansI
