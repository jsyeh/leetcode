# LeetCode 131. Palindrome Partitioning
class Solution:
    @cache  # 加速的技巧，當相同參數再次執行時，會把之前算過的舊答案回傳
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0: return [[]]  # 終止條件：0個字母
        if len(s) == 1: return [[s]]  # 終止條件：1個字母，剛好也是迴文
        ans = []
        for i in range(len(s)):  # 考慮前i個字母
            if s[:i+1] == s[i::-1]:  # 前i個字母「正的、反的」完全相同，是迴文
                for p in self.partition(s[i+1:]):  
                    # 上面函式呼叫函式，問（後半）更小的問題
                    # 下面，把小問題的結果的前面，都冠上「前i個字母」的那個迴文
                    ans.append([s[:i+1]] + p)
        return ans

