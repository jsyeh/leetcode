# LeetCode 1268. Search Suggestions System
# searchWord 每次輸入1個字母，找到對應的 products 前3名
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()  # 照字母順序排序，可在之後照字母序插入
        tree = defaultdict(list)  # 建 trie 不過我比較熟 tree 的拼法
        for product in products:  # 照字母序插入
            now = tree
            for c in product:
                if c not in now:
                    now[c] = defaultdict(list)
                now = now[c]
            now[''] = product  # 最後放字
        def helper(now, k):  # 找到 tree 裡符合prefix的前k個
            if k==0: return []  # 終止條件
            ans = []
            for c in now:  # 現在的 node 往下試
                if c=='': ans += [now['']]  # 找到1組
                elif k>0: ans += helper(now[c], k-len(ans))  # 持續湊
                else: break  # 湊完 k 組，可以離開
            return ans  # 湊出來的答案在這裡
        ans = []
        now = tree  # 從頭開始
        for i,c in enumerate(searchWord):  # 逐字母處理
            if c in now:  # 檢查「能不能走下去」
                now = now[c]  # 現在的 tree 走到 now node
                ans.append( helper(now, 3) )  # 找到前3組，塞入答案
            else:  # 走不下去，要提早結束
                print(len(searchWord)- len(ans))
                return ans + [[] for i in range(len(searchWord)- len(ans))]
        return ans
