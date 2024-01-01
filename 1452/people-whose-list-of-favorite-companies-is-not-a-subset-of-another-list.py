# 找出 i 使得 favoriteCompanies[i] 不是任何人的 subset
# 100人，喜歡500家公司，每家公司字串長度<=20字母
# 可以用集合 set() 來看是否 setA < setB
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        N = len(favoriteCompanies)
        favoriteSet = [set() for _ in range(N)]
        for i in range(N): # 針對每個人
            for k in favoriteCompanies[i]:
                favoriteSet[i].add(k) # 先建出 set
        ans = []
        for i in range(N): # 針對每個人
            bad = 0
            for j in range(N):
                if i==j: continue # 避開自己對自己
                if favoriteSet[i] <= favoriteSet[j]:
                    bad = 1 # 如果是別人的subset 就失敗
                    break
            if bad==0: ans.append(i) # 沒有失敗，便是答案
        return ans
