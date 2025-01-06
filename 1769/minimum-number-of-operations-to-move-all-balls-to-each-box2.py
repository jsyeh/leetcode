# LeetCode 1769. Minimum Number of Operations to Move All Balls to Each Box
# 字串 boxes 對應 n 個盒子（0空的、1有球）。若想分別「將球集中」在某個盒子，要分別移動幾步呢？
# 因盒子較少1000個，真的用暴力法，也能及時算完。但想更「優美、有效率」解決，可使用 prefix 技巧
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)
        prefix = [0]*(N+1)  # 從左到右累加
        postfix = [0]*(N+1)  # 從右到左累加
        left, right = 0, 0  # 左邊累積幾個1 vs. 右邊累積幾個1
        for i in range(N):
            prefix[i+1] = prefix[i] + left  # 左到右，累積幾個1，下一格就要加「這麼多個1」
            if boxes[i]=='1':
                left += 1
                prefix[i+1] += 1
                
            postfix[N-i-1] = postfix[N-i] + right  # 右到左
            if boxes[N-i-1]=='1':
                right += 1
                postfix[N-i-1] += 1
        ans = [0]*N
        for i in range(N):  # 從左到右累加 + 從右到左累加
            ans[i] = prefix[i] + postfix[i+1]
        return ans
