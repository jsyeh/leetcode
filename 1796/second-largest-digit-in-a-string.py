# LeetCode 1796. Second Largest Digit in a String
# 把字串 s 裡的數字取出來，問「第2大」的數字是誰。
# 用 Counter 來快速統計「有哪些字母」，再從 9,8,7 往下逐一找即可
class Solution:
    def secondHighest(self, s: str) -> int:
        counter = Counter(s)
        largest = 0
        print(counter)
        for i in range(9,-1,-1):  # 倒過來的迴圈
            now = str(i)  # 改成字串來分析
            if counter[now]>0: 
                largest+= 1
            if largest==2:
                return i
        return -1
