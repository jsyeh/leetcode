# LeetCode 1002. Find Common Characters
# 最多有 100 個 word, 每個 word 最多有 100 個字母的話
# 問你全部的 word 裡「共同的字母」有哪些。若有重覆的字母, 也要重覆秀出來。
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = Counter(words[0])  # 使用 Counter()來數一下字母出現次數
        # 前面先把 words[0] 拿來分析, 當第一批
        for word in words:  # 接下來, 針對全部的字
            counter2 = Counter(word)  # 都要數一數它的字母出現次數
            counter &= counter2  # 有交集的字母嗎? 交集幾個?
        # 經過以上的 Counter 的 &= 操作, 全部的交集, 都放在 counter 裡
        ans = []  # 最後要把答案格式放好
        for c in counter:  # 最後交集的結果, 依序加入答案
            for i in range(counter[c]):  # 字母c出現 counter[c]次
                ans.append(c)  # 那就將 c 加入 ans, 且重覆做 counter[c] 次
        return ans
