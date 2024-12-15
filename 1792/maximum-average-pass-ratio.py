# LeetCode 1792. Maximum Average Pass Ratio
# classes 有 passi 和 totali 是「及格人數」及「全班人數」，把「必過的人」加入某班，讓平均及格數最漂亮
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []  # 使用 heap 來找到「改善程度最大」的班
        for passi, totali in classes:  # 逐一加入 heap
            improve = (passi+1)/(totali+1) - passi/totali  # 「可改善」的程度
            # Python heap 會取最小，事先加「負號」便可取出「可改善」的程度「大的」
            heappush(heap, (-improve, passi, totali) )  
        for k in range(extraStudents):
            # 哪個班「可改善」的值最大，就優先取它
            ratio, passi, totali = heappop(heap)
            passi += 1  # 加1人（必及格）
            totali += 1  # 加1人（班級人數）
            improve = (passi+1)/(totali+1) - passi/totali  # 新的「可改善」的程度
            heappush(heap, (-improve, passi, totali))  # 再塞回 heap
        ans = 0
        for ratio, passi, totali in heap:
            ans += passi/totali
        return ans / len(heap)        
