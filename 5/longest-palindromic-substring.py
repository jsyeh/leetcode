# Substring 必須是連續的哦
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        table = [[False]*N for _ in range(N)]
        # table[left][right] 可知道 left...right 是不是迴文
        for i in range(N):
            table[i][i] = True # 長度是1的單一字母，一定是迴文（右包含）
        
        ansLeft, ansRight, ansLen = 0, 0, 1 # 右包含
        # s[左:右+1] 便能取出substring

        # 迴圈要讓字串逐漸長大，才能善用 DP 的特性
        for right in range(N): # 決定右邊界 Q:為何要反過來？A:迴圈較簡單
            for nowLen in range(2,right+2): # 決定長度，由短到長
            # 長度1事先填好True,這裡從2開始。最長是right+1，所以right+2當不包含的右邊界
                left = right - nowLen + 1 # 算出右邊界
                #print(left, right, nowLen)
                if s[left] == s[right]: # 頭尾相同，太好了
                    if nowLen==2 or table[left+1][right-1]==True: # 若裡面也迴文 or 長度為2像"aa"沒裡面時
                        table[left][right] = True # 太棒了，它是迴文
                        if nowLen> ansLen: # 更長的迴文，整組更新
                            ansLen = nowLen
                            ansLeft = left
                            ansRight = right
        #print(ansLen)
        return s[ansLeft:ansRight+1]
# case 81/141: "bb"
