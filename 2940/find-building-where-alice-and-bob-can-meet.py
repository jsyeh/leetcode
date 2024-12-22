# LeetCode 2940. Find Building Where Alice and Bob Can Meet
# 大樓高度 heights[i] 在這可往右走到「更高」的大樓
# queries 裡，有各種 a,b 的位置，他們「右邊」更高的大樓，就是他們見面的位置，都找出來。
# 若用「暴力兩層for迴圈」，程式很好寫，但會超時。
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1]*len(queries)  # 準備好放答案（問題Q有幾筆、答案A就有幾筆）無法處理的放-1
        waiting = [ [] for i in range(len(heights))]  # 有些格子，還無待處理
        for qi,(a,b) in enumerate(queries):  # 問 a,b 兩人的答案 ans[qi]
            if a>b: a, b = b, a # 交換，讓a在左、b在右
            if a==b: ans[qi] = b  # 在同一個大樓，直接「原地集合」就好了
            elif heights[a]<heights[b]: ans[qi]=b  # 剛好右邊b大樓「更高」，就在右邊b大樓集合即可
            else:  # 還無法判斷的，放 waiting 裡，等「左到右，依大樓的高度處理」時，再取出來
                higher = max(heights[a], heights[b]) # 比較高的大樓高度
                waiting[b].append( (higher, qi) ) # 右邊大樓b出發、高度要比 higher大，答案會補填ans[qi]
        # 接下來，針對 waiting 裡未解的部分，左到右處理
        heap = []  # 會取出「待處理」中，小的部分
        for i, h in enumerate(heights): # 左到右，依建築高度處理。本大樓 heights[i]
            while heap and heap[0][0] < h: # 現在這個高度 h 夠高，能當成 heap 「待處理」案件的答案
                higher, qi = heappop(heap)  # 「待處理」案件，heap[0][0] 是higher高度，對應答案 qi
                ans[qi] = i  # 本大樓，可以是之前「待處理」案件的答案，因為比較高
            # 處理完「待處理」且比較矮的大樓後，把「本大樓」旗下「待處理」案件，也加入 heap
            for (higher, qi) in waiting[i]: # 本大樓 i 「待處理」的案件
                heappush(heap, (higher,qi) )
        return ans
