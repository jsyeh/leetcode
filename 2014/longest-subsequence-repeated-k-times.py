# LeetCode 2014. Longest Subsequence Repeated k Times
# s 字串裡，找到重覆 k 次的 subsenquence 最長字串
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def isSubsequence(sub, s):  # sub 是 s 的 subsequence 嗎？
            i = 0  # sub[i] 這個字母，有出現在 s 裡嗎？
            for c in s:  # 依序測試
                if sub[i]==c:  # 找到1個字母
                    i += 1  # 就換下一個字母
                    if i>=len(sub): return True  # 湊齊字母，就成功
            return False  # 沒成功，就失敗

        counter = Counter(s)  # 統計字母出現次數，超過 k 倍以上，可當候選人
        candidate = []  # 候選的字母，都足夠8倍
        for c in counter:
            if counter[c] >= k:  # 有重覆 k 次的字母，可放入 queue 裡
                candidate.append(c)
        candidate.sort(reverse=True)  # 讓字母大的放在前面，因題目希望「字典序大」
        queue = deque(candidate)  # 字母「由大到小」依序放入 queue 裡
        ans = ''  # 一開始是空字串
        while queue:  # 還能取出字母（用BFS的方式，依序取出）
            now = queue.popleft()  # 現在處理 now 字串
            if len(now)>len(ans): ans = now  # 更長的話，換新答案
            for part2 in candidate:  # now + part2 能不能組合出更長的答案？
                if isSubsequence( (now+part2)*k, s ):  # 確認k倍後成立
                    queue.append(now+part2)  # 延伸出更長的答案候選人
        return ans   
