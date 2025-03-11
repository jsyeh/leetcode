# LeetCode 1358. Number of Substrings Containing All Three Characters
# s 字串裡，有幾個 substring 裡，有湊齊 a,b,c 三種字母。可用「毛毛蟲」sliding window解
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = Counter()
        N = len(s)
        ans = tail = head = 0  # 左邊尾巴、右邊頭「一開始都是0」
        while tail < N and head <= N:  # 「毛毛蟲」的頭、尾，都沒超過界線
            if len(counter)==3:  # tail ... head 已湊齊 3 種字母
                ans += N - head + 1  # 這時候 head 往右到底，也都符合3種字母，全加
                c = s[tail]  # 接下來，把「左邊尾巴」吐掉1個字母
                counter[c] -= 1  # 吐掉的字母 -1
                if counter[c]==0: del counter[c]  # 字母用盡，就不列入記錄
                tail += 1  # 尾把右移1格
            else:  # 沒湊齊，需要「右邊頭」再多吃字母
                if head==N: break  # 若 head 已走到底的話，就應離開
                c = s[head]  # 現在要吃的字母是 c
                counter[c] += 1  # 數目加1
                head += 1  # 頭右移1格
        return ans
