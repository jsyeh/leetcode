class Solution:
    def compress(self, chars: List[str]) -> int:
        N = len(chars)
        ansN = 1
        repeat = 1 # 每個字母，出現時，一定是第1個
        for i in range(1,N): # 避開chars[0] 因它不用變
            if chars[i-1] == chars[i]:
                repeat += 1
            else: # 如果字母不同，那就要更新前一項的數目
                if repeat>1: # 重覆的話
                    for c in str(repeat): # 就補上數字
                        chars[ansN] = c
                        ansN += 1
                repeat = 1 # 重新開始
                chars[ansN] = chars[i] # 再把新的字母覆蓋上去
                ansN += 1
                # print(chars, ansN)
            # print(chars, ansN)
        # 離開迴圈時，再更新一次
        if repeat>1: # 若重覆很多次，要再補上「重覆的數字」
            for c in str(repeat):
                chars[ansN] = c
                ansN += 1
                # print(chars, ansN)
        return ansN

