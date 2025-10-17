# LeetCode 3003. Maximize the Number of Partitions After Operations
# s 字串「先改某1個字母」，再持續「從頭挑prefix裡最多k個不同字母」斷開刪掉，直到字母全部刪光，最多能做幾次？
# 問題在「可先改1個字母」到底「要改哪一個」？不能暴力試。可用「函式呼叫函式」全試、避開重覆運算
class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        N = len(s)
        charBit = {chr(ord('a')+i) : (1<<i) for i in range(26)}  # 字母bit對照表 bit['a']為1<<0
        @cache  # 用「函式呼叫函式」解DP問題，大問題變小問題
        def helper(i, changed, charSet):  # 處理到 s[i], 是否已用1次機會、charSet 對應 bit mask
            if i==N: return 0  # 順利走到最後，最後這裡是0個 partition, 從右往左「回報」
            nowSet = charSet | charBit[s[i]]  # 使用「現在」的字母、不變動
            if nowSet.bit_count() <= k:  # 沒超過上限，還可以繼續延伸
                ans = helper(i+1, changed, nowSet)  # 繼續往下個字母走
            else:  # 超過上限，必須「從s[i]開始、切出新的一塊」、新的開始
                ans = 1 + helper(i+1, changed, charBit[s[i]] )  # 1 + 新的開始
            if not changed:  # 若之前沒「變動過字母」，接下來思考「能把現在s[i]換成其他字母」嗎？
                for c in charBit:  # 每種字母都試看看
                    nowSet = charSet | charBit[c]  # 使用新的字母
                    if nowSet.bit_count() <= k:  # 沒超過上限，還可以繼續延伸
                        ans = max(ans, helper(i+1, True, nowSet) )
                    else:  # 哇，超過上限，必須「從這個位置、切出新的一塊」、新的開始
                        ans = max(ans, 1 + helper(i+1, True, charBit[c]))
            return ans  # 試過所有可能的「最佳解」
        return 1 + helper(0, False, 0)  # 第1塊，從s[0]開始、還沒變動過字母、目前mask還是0

