# LeetCode 2710. Remove Trailing Zeros From a String
# 把 num 右邊的0刪光光。
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
            if num[i]!='0': # 只要字母「不是'0'」就要中斷迴圈
                return num[:i+1]  # 並將右邊裁掉，當成答案
        return ''  # 應該不會變成這樣啦（0都被裁光 ，只是寫好玩的
