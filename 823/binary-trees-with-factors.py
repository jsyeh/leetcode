class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        N = len(arr)
        index = {}
        for i in range(N): # 建出 index[x] 的字典
            index[ arr[i] ] = i # 給個數字x，便能知道有沒有在字典 index 裡，且能知對應的i為index[x]

        table = [1]*N # 排列組合的個數，記得要 % 1 000 000 007
        # table[i] 代表 arr[i] 這個數為 root 時，答案有幾個。預設都先有1
        MOD = 10 ** 9 + 7 # 也就是 1000 000 007
        for i in range(N): # 動態規劃解題，現在處理 arr[i] 這個數
            for k in range(i): # 想找找 arr[i] 能被 arr[k] 整除嗎？
                if arr[i] % arr[k] == 0: # 太好了，有整除，這時候，再查 arr[i]//arr[k] 有這個數嗎
                    another = arr[i]//arr[k] # 另外一個數字，有在 arr裡嗎？
                    if another in arr:
                        k2 = index[another]
                        table[i] += table[k] * table[k2] # arr[i] == arr[k] * arr[k2] 
                        table[i] %= MOD
        return sum(table) % MOD # 表格裡是以arr[i]當root的答案，全部都加起來，就是總合
        
