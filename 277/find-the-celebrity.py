# LeetCode 277. Find the Celebrity
# 找到「名人」，每個人都認識「名人」，但「名人」不認識任何人
# 只能呼叫 knows(a,b) 查看「誰是否認識誰」
class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(1,n):
            if knows(candidate, i):  # i 更有名，換 candidate
                candidate = i  # 全部巡完後，能撐到最後的那個，是候選人
        following = 0
        for i in range(n):  # 再確認 candidate 能讓所有人認識
            if i == candidate: continue  #避開自己看自己
            if knows(i, candidate): following += 1  # 有幾個人認識
            if knows(candidate, i):
                return -1  # 竟然認識別人，這就不是名人

        if following==n-1:  # n-1 人都認識他
            return candidate
        else: 
            return -1
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
