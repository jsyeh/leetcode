# 每次比較 arr[0] vs. arr[1], 大的放在 arr[0] 並計1次
# 如果 arr[0] win k 次，就是答案
# 因arr[0]答案越來越大，輸的「不需要移到最後，直接丟掉」
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        N = len(arr)
        ans, winN = arr[0], 0 # 第0個數字，已勝0次
        for i in range(1,N): # 依序和 arr[1]...最後的數比
            if ans > arr[i]: # 保持連勝記錄
                winN += 1
            else: # 沒辦法連勝，就換人當 ans
                ans = arr[i]
                winN = 1 # 從1勝開始累積
            if winN >= k: # 如果累積夠多勝
                return ans # 就提早結束
        # 如果全部都比過，那 ans 確定比全部人都大
        return ans # 你要k次，不管k要多少次，都能確定 ans 必勝
