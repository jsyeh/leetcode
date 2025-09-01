# LeetCode 1792. Maximum Average Pass Ratio
# classes 陣列裡，有許多門課的「及格人數passed、全班人數total」資訊。
# 另有 extraStudents 還沒修課的「額外同學」超強，去修「任何課」保證都能及格。
# 要怎麼安排、把「超強」的「額外同學」加入某些班，能得到「最高」的「平均通過率」
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []  # 使用 heap 來找到「改善程度最大」的班
        for passed, total in classes:  # 逐一加入 heap
            improve = (passed+1)/(total+1) - passed/total  # 加入1人後，「可改善」的程度
            # Python heap 會取最小，事先加「負號」便可取出「可改善」的程度「大的」
            heappush(heap, (-improve, passed, total) )  # 每個班級，都算出它的「可改善」的程度
        for k in range(extraStudents):  # 額外同學「一個個塞入班級中」
            # 哪個班「可改善」的值最大，就優先取它
            improve, passed, total = heappop(heap)  # 從 heap 挑1個班級，好好更新
            passed += 1  # 加1人（必及格）
            total += 1  # 加1人（班級人數）
            improve = (passed+1)/(total+1) - passed/total  # 新的「可改善」的程度
            heappush(heap, (-improve, passed, total))  # 再塞回 heap
        ans = 0  # 認真計算「目前所有班級」的通過率
        for improve, passed, total in heap:
            ans += passed/total
        return ans / len(classes)  # 再除「班級數」便是「平均通過率」
