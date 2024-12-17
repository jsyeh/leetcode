# LeetCode 2182. Construct String With Repeat Limit
# 用字串 s 的字母（不需全用），做出「新字串」，裡面字母不能重覆太多 （字母序要最大）
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = Counter(s)  # 先統計「能用的字母」
        heap = [(-ord(c),c) for c in counter]
        heapify(heap)  # 希望「字母序大」先取出，但 heap 先取「小」所以加負號 -ord(c) 
        # 策略：優先放「字母序大」字母（並交錯放1個「次大」字母）。用盡換下一個
        ans = []  # 因字串很長、字串加法慢，改用 list 希望快一點，之後再 ''.join(ans) 即可
        while heap:  # 每次取出「最大的」字母
            o, maxC = heappop(heap)  # 先取出字母序「最大的」字母
            repeat = min(counter[maxC], repeatLimit)  # 能重覆的數量（在範圍內，能放多少，儘量放）
            ans += [maxC]*repeat  # 把「這麼多」「重覆」的字母，放入答案
            counter[maxC] -= repeat  # 字母用掉「這麼多」！
            if counter[maxC]==0:  # 如果「最大的」字母用完了
                continue  # 就提早結束這輪（後面不用塞「第二大」字母），換下一種「大字母」
            if heap:  # 再取出「第二大」字母，要塞1個在後面（交錯）
                nextC = heap[0][1]
                ans += [nextC]  # 拿1個「第二大」字母，塞入ans
                counter[nextC] -= 1  # 用掉1個
                if counter[nextC]==0: heappop(heap)  # 如果「第二大」字母用盡，就清掉它
            else: 
                break  # 但已沒有「第二大」字母，就無法「交錯」，只能提早離開了
            heappush(heap, (-ord(maxC), maxC))  # 再塞回「最大的」字母，方便下一輪處理

        return ''.join(ans)  # 再把 list 變回字串
