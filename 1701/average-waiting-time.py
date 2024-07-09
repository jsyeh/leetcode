# LeetCode 1701. Average Waiting Time
# 只有1位廚師，客人照著時間進來，有各自需備餐的時間。
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        N = len(customers)
        chiefFreeTime = 0  # 廚師下次有空的時間
        waitingTime = 0  # 用來加總「等待的時間」
        for a, t in customers:
            if a >= chiefFreeTime: # 在有空之後才進來，很好
                waitingTime += t  # 就只要等「備餐時間t」
                chiefFreeTime = a + t  # 更新下次有空時間
            else: # 不幸客人進來時「廚師在忙」，餐點完成時間會更晚
                waitingTime += (chiefFreeTime + t) - a # 要等這麼久
                chiefFreeTime += t  # 更新下次有空時間
        return waitingTime / N  # 平均等待時間

