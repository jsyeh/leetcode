# LeetCode 1408. String Matching in an Array
# words 裡，若某字是另一個字的 substring，就放到答案裡（順序沒關係）
# 把所有的 substring 找出來。用暴力全試即可
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x:len(x)) # 字串短的放前面、長的放後面
        ans = []
        N = len(words)
        for i in range(N):  # 小字串（左邊）
            for j in range(i+1, N):  # 大字串（右邊）
                if words[j].find(words[i]) != -1:  # 有找到（大字串裡，有小字串）
                    ans.append(words[i])  # 放入答案
                    break  # 已是子字串，就不用再試囉！
        return ans
