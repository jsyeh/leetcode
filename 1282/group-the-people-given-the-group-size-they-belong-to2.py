# 題目input是「每個人」所在的 group size人數
# output 一堆 groups, 符合上面的條件
# 可以這樣想：先把相同group size的人都分類出來。
# 同樣 group size 的，再切成對應人數。過程中需要把index記起來

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {} # key:人數，value: list of index
        N = len(groupSizes)
        ans = [] # 用來放答案
        for i in range(N):
            s = groupSizes[i]
            if s in groups:
                groups[s].append(i)
            else:
                groups[s] = [i]
            if len(groups[s])==s: 
                # s人一群，湊齊了，就送出去
                ans.append(groups[s])
                groups[s] = [] # 再清空
            # print(groups) # 果然正確分群分類好了
        return ans        
