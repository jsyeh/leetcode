# LeetCode 2418. Sort the People
# 第i個人的名字names[i] 及身高heights[i]
# 請照 heights[i] 由高到底排好
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans = sorted(zip(heights, names), reverse=True)
        return [name for height,name in ans]
