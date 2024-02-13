# 有100人，[birth, death] 對應「出生年、死亡年」（死亡那年，就不算）
# 問「哪一年」人最多。若有很多答案，回傳「最早的那年」
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        detail = [(log[0], 1) for log in logs] # 出生年，人數+1
        detail += [(log[1], -1) for log in logs] # 死亡年，人數-1
        detail.sort() # 照年分排序
        ansYear = 0 # 哪一年人最多
        maxPeople = 0 # 人最多，是多少人？
        people = 0 # 計算中，現在是多少人
        for year,diff in detail:
            people += diff # 每年的增減
            if people>maxPeople: # 如果人數更多
                maxPeople = people # 就更新
                ansYear = year # 並記錄年份

        return ansYear
