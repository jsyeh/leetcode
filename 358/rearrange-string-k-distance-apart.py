# LeetCode 358. Rearrange String k Distance Apart
# 調整字串 s 的順序，使得「相同字母」距離至少有 k 格
# 出現最多次的字母「最麻煩」，想到可用 queue 裡面放 k 個「前k個多的項」用到結束為止
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        counter = Counter(s)  # 統計字母出現次數，希望優先挑「次數多的」
        heap = []  # heap可取出「現在能用、剩下次數最多的字母」
        for c in counter:  # 將字母「依出現次數」加入 heap
            heappush(heap, (-counter[c], c))  # 希望「多到少」挑選，故加負號
        ans = []  # 答案字母將「依序」放入 ans 裡
        queue = deque()  # 「用過的字母」暫放在 queue 裡，若「用過的字母」夠多，可釋放回 heap 池子
        # 解釋：字母會在 heap 和 queue 之間跳動。queue排夠久，就能放回 heap 池子
        while heap:  # 從 heap 挑出「數量最多」的字母
            v, c = heappop(heap)  # 從 heap 池子取出「數量最多」的字母
            ans.append(c)  # 將目前「數量最多」的字母，放入答案
            counter[c] -= 1  # 用掉1個
            queue.append(c)  # 排入 queue 裡，要等待「足夠久」，才能再放回 heap 池子
            if len(queue) >= k:  # 有足夠多「不同」的字母，等待「夠久」才可釋放回 heap 池子
                now = queue.popleft()  # 目前等最久的子母
                if counter[now] > 0:  # 若字母還有剩
                    heappush(heap, (-counter[now], now))  # 就放回池子
        if len(ans) != len(s):  # 若無法湊齊整個字串
            return ""  # 就失敗
        return ''.join(ans)  # 成功的答案
