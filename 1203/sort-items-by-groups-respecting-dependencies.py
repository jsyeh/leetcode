# 奇怪的排序法：同group的要放在一起。
# 再照著dependency 的相關性（要先把 beforeItems[i]都做完，才能把 i 拿來排
# 可回傳任一種可行的解法。但沒辦法找到排序的解法的話，就 return []
# 這題超過我的能力範圍，所以我參考Solution裡votrubac的解法，使用topological sort

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        def topSort(al, i, ans, state):
            # print("topSort():", i, ans, state)
            # 如果 node i 的 state 不是0，就可能在「測試中」or「測試成功」
            if state[i] != 0: return state[i] == 2 # 「測試成功」的話，good
            # 「測試中」的話，就 no good

            state[i] = 1 # node i 進入「測試中」
            for k in al[i]: # node i 相鄰的全部
                if not topSort(al, k, ans, state):
                    return False # 壞掉，就False
            state[i] = 2 # node i 測試後沒有壞掉，「測試成功」
            ans.append(i) # 開心的把i放到答案裡
            return True

        ans = [] # 放排序後的結果
        ans_temp = [] # 會倒著放，從最後面，依序把符合的node加入。之後要反轉回ans
        state = [0]*(n+2*m) # n個點 + m個group，而每個group需要2個node處理
        al = [set() for _ in range(n+2*m)] # adjacency list
        # 這裡我有出錯，不能寫 al = [set]*(n+2*m) 會用到同一組set()
        # 而要用這個 al = [set() for _ in range(n+2*m)] 才行
        # n個點 + m個group，而每個group需要加2個node處理排序的「頭」「尾」

        for i in range(n): # n個點，照 group 的值，來決定「誰和誰相鄰」
            if group[i] != -1: # 有 group 資訊的話
                al[n+group[i]].add(i) # group i 的頭，在 node i 之前
                al[i].add(n+m+group[i]) # node i 在 group i 的尾把之前

            for j in beforeItems[i]: # node i 之前要做的事 「先j再i」
                if group[i] != -1 and group[i] == group[j]:
                    al[j].add(i) # 有幸 j 與 i 是相同 group 的話，加入 「先j再i」
                    # Connect nodes directly for inter-group dependencies.
                    # 也就是「先j再i」的順序
                else: # 不是同個group 就比較麻煩
                    # 要跨 group 的話，代表 group node 也會有特定的順序
                    if group[i] == -1: ig = i # 自己獨立很自由，考慮自己就好
                    else: ig = n + group[i] # group i 的開始點
                    if group[j] == -1: jg = j # 自己獨立很自由，考慮自己就好
                    else: jg = n + m + group[j] # group j 的結束點
                    al[jg].add(ig) # 「先j再i」 jg的結束點，在ig的開始點之前
        # for s in al: print(s)

        # 「後到前」逐一排序
        # 先看最後面的node (各group結束點), 再處理各group的開始點，最後各個點排序
        for i in range(len(al)-1, -1, -1): 
            if not topSort(al, i, ans_temp, state): 
                # print("無法排序/失敗")
                return [] # 做不到，直接回傳空

        # print(ans_temp)
        for i in range(len(ans_temp)):
            # print("i:", -i-1, "final:", ans_temp[-i])
            if ans_temp[-i-1]<n:
                ans.append(ans_temp[-i-1])
        # 還差一行 copy_if(begin(res_tmp), end(res_tmp), res.begin(), [&](int i) {return i < n; });
        return ans
# case 15/17: 3
# 1
# [-1,0,-1]
# [[],[0],[1]]
