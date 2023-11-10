# 搞笑的題目: 忘記陣列裡的值, 只知陣列裡數字不重覆, 只知相鄰的兩兩數字(不知前後順序)
# 要把 array 重建出來。其實只要把頭找出來, 就可以一直串連, 整串一直連起來。
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        N = len(adjacentPairs) + 1 # 總共有幾個數 (pair數+1)
        d = defaultdict(list) # d[k] 將會存 k 的1-2個鄰居
        for a,b in adjacentPairs: # 每次處理 a,b 互為鄰居
            d[a].append(b) # a的鄰居有b
            d[b].append(a) # b的鄰居有a
        # 建好 d 之後, 針對每個 key 逐項檢查
        for k in d:
            if len(d[k])==1: # 找到落單的數了, 它就是頭
                key = k
                break

        ans = [key]
        for i in range(N-1): # 要逐一把鄰居取出來、掛在 ans 後面
            now = ans[-1] # 答案的最後一項 now, 要找出它的鄰居
            next = d[now][-1] # 最後一筆
            ans.append(next)
            # 接下來, 把 now <-> next 這組的資訊清掉, 不要再用它了
            d[now].remove(next) # 用過後, 把它 remove 掉,下次才不會重覆用
            d[next].remove(now) # 用過後, 把它 remove 掉,下次才不會重覆用
        
        # 全部整串連完後,  就可以結束了
        return ans
