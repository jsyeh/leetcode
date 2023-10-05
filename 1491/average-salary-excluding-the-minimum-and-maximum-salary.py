# 把最大值、最小值去除掉的平均
# 其實重點就是找到最大值、最小值，刪掉它，就好了
class Solution:
    def average(self, salary: List[int]) -> float:
        N = len(salary)
        return (sum(salary)-max(salary)-min(salary))/(N-2)
