# 第i個人的名字names[i] 及身高heights[i]
# 請照 heights[i] 由高到底排好
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = [(heights[i],names[i]) for i in range(len(names))]
        people.sort(reverse=True) # 先結合成 pepole 再照heights[i]排序
        # 最後再取出 names[i] 即 people[i][1]
        return [people[i][1] for i in range(len(names))] 
