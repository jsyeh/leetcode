# 請把依學生的第k項成績排序。第i位同學的分數是 score[i]，所以是照 score[i][k]排序
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(reverse=True, key=lambda x:x[k])
        return score
