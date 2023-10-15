# 很多書架，從左到右拿書（嚴格遞增），最多可拿多少書
# Monostack 可以解
# 但我還是不太熟。Solutions yuanzhi247012 的圖解很清楚
# https://leetcode.com/problems/maximum-number-of-books-you-can-take/solutions/2367084/python3-increasing-stack-only-record-sudden-changes/

class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        N = len(books)
        ans = 0
        stack = [] # 裡面會存「index、對應的加總最大值」
        for i in range(N):
            while len(stack)>0 and books[i]<=books[stack[-1][0]]+(i-stack[-1][0]):
                # 如果 monostack 裡存的值，需要被book[i]剪頭髮，那就不行
                stack.pop() # 最右邊的stack[-1]要被剪掉
            # 接下來 stack[-1]便是(現階段)合理的答案
            if len(stack)>0:
                prevI, prevAns = stack[-1]
            else:
                prevI, prevAns = [-1, 0]
            # 要算梯形面積：(上底+下底)*高//2
            h = min(i-prevI, books[i])
            cur = prevAns + (books[i]+books[i]-h+1)*h//2

            # 最後，把現在的index i及對應答案cur，塞回stack裡
            stack.append([i,cur])
            if cur>ans: ans = cur
        return ans

