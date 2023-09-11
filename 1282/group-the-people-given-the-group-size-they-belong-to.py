# 題目input是「每個人」所在的 group size人數
# output 一堆 groups, 符合上面的條件
# 可以這樣想：先把相同group size的人都分類出來。
# 同樣 group size 的，再切成對應人數。過程中需要把index記起來

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {} # key:人數，value: list of index
        N = len(groupSizes)
        for i in range(N):
            s = groupSizes[i]
            if s in groups:
                groups[s].append(i)
            else:
                groups[s] = [i]
        # print(groups) # 果然正確分群分類好了

        ans = [] # 用來放答案
        for s in groups: # 現在要處理的這群，是每s人一群
            # print(s, groups[s])
            persons = groups[s] 
            # 如果 s 是 3, persons 有6個人，就要再分成2群
            nowgroup = [] # 現要處理的這群
            for i in range(len(persons)):
                nowgroup.append(persons[i]) # 先把 persons[i] 塞進去
                if i%s == s-1: # 如果是這群的最後1人
                    ans.append(nowgroup) # 整群塞入ans
                    nowgroup = [] # 再開新的一群
        return ans
        
