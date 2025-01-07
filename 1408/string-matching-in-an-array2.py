# LeetCode 1408. String Matching in an Array
# words 裡，若某字是另一個字的 substring，就放到答案裡（順序沒關係）
# 把所有的 substring 找出來。用暴力全試即可
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for w1 in words:  # 想試看看 w1 是不是答案
            for w2 in words:  # 看 w2 裡有沒有 w1
                if w1==w2: continue  # 相同就是遇到自己，跳掉
                if w2.find(w1) != -1:  # w2 裡面有找到 w1 的話
                    ans.append(w1)  # 加入答案
                    break  # 並離開小迴圈，換下一個 w1
        return ans
