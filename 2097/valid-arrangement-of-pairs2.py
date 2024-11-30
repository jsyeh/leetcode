# LeetCode 2097. Valid Arrangement of Pairs
# 「頭尾相接」全部走完
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        path = defaultdict(list)  # 所有可能的走法「a到b」
        head = Counter()  # 數一數，誰要當「開始點」（頭）
        for a,b in pairs:  # a 到 b
            path[a].append(b)  # a 可以到 b
            head[a] += 1  # a當頭的次數+1
            head[b] -= 1  # 尾與頭對消，所以 b 當頭的次數 -1
        # 先找到「開始點」，也就是「只在前面」及「只在後面」的數
        for i in head:
            if head[i]==1:
                a = i  # 確定頭在哪裡
                break  # 並離開迴圈（如果都沒找到，會用第7行殘留的a）
        # DFS
        ans = []
        def helper(a):
            while path[a]: helper(path[a].pop())
            ans.append(a)
        helper(a)
        #print(ans)
        return [ [ans[i+1],ans[i]] for i in range(len(ans)-2,-1,-1)]
