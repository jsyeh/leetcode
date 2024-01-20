# 把全部連續的 subarray ，每個subarray的最小值加起來。
# 本來以為是 DP 的題目, 每次多考慮1個數字，Subarray 需要是「連續」不能跳過某些數哦！
# 但我一直失敗、超時，最後放棄。好難、超難。改參考 manassenhkola 的 mono stack 解法。
# 利用 mono stack 存某人當主角（最小值）並會對應它的左邊界i1 右邊界i2，能算出當時的總和
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # 最後發現這題超難。改用 mono stack 解決變超簡單
        ans = 0 # 放加總的結果
        arr.append(0) # 最後面加上0，讓迴圈最後收尾，可簡化程式
        stack = [-1] # stack最前面（也是最後一項)，塞入 -1 對應arr最後一項0，可簡化程式
        for i2,now in enumerate(arr): # now = arr[i2] 把 i2 當右邊界
            while stack and now < arr[stack[-1]]: # 比mono stack 最上方小，就一直吐出stack
            # stack 不是空的時，最後一項的index可查「對應」的 arr[index] 主角當下的最小值
                index = stack.pop() # 吐出最後的 index
                # 最一開始會吐出arr.append(0) 的那個0, 即第0項的index
                # i1 ... index ... i2
                #    left      right
                i1 = stack[-1] # 左邊界i1，右邊界i2
                left = index-i1 # 左邊有哪些可能
                right = i2-index # 右邊有哪些可能
                ans += left*right*arr[index] 
                # 排列組合，左邊選擇數 * 右邊選擇數，都是對應最小值 arr[index]，算其總合
            stack.append(i2) # 把迴圈 i2 stack 對應最佳值（每個人都有機會當1次主角）
        return ans%(10**9+7) # 加總的結束，要記得 MOD 10**9+7

        '''# 這個版本會超過時間
        MOD = 10**9 + 7
        N = len(arr)
        # 邊更新 dict 邊計算答案
        table1 = defaultdict(int)
        table1[arr[0]] = 1 # 最簡單的基礎型
        ans = arr[0]  # 最簡單的基礎型
        for i in range(1,N): # 從1開始
            table2 = defaultdict(int)
            table2[arr[i]] = 1 # 最簡單的基礎型
            ans += arr[i]
            for m in table1: # 往前看前1題的答案
                if arr[i]<m: # 如果數字更小，就要把 table1 的值都 變小
                    table2[arr[i]] += table1[m] # 都更新
                    ans += table1[m] * arr[i]
                else:
                    table2[m] += table1[m]
                    ans += table1[m] * m
            table1 = table2
            ans = ans % MOD
        return ans
        '''

        ''' # 因為數字太多時，陣列會開太大，所以「開兩個字典」交換即可
        N = len(arr)
        table = [defaultdict(int) for _ in range(N)]
        # table[i] 表示結尾在 arr[i] 的全部 subarray 的最小值m & 出現次數
        # 對應「最小值是m有幾個 subarray」
        # 在更新時，依 arr[i] vs. 字典的key 最小值m，來更新「新字典」
        # 因為 subarray 是連續的，所以 table[i] 會與 table[i-1] 有關
        for i in range(N):
            table[i][arr[i]] += 1 # 只有最後一項，最小值就是 arr[i]
            # 下面則是有「摻」前面的項
            if i>0:
                for m in table[i-1]: # 字典 table[k] 對應的最小值
                    if arr[i] < m:
                        table[i][arr[i]] += table[i-1][m] # 最小值是它，有幾次，就全上
                    else:
                        table[i][m] += table[i-1][m] # 最小值是原本的m保持，有幾次，就全上
            #print(table[i])
        ans = 0 # 最後算答案，統計加起來到底有多少，記得要 % MOD
        MOD = 10**9+7
        for i in range(N): # 把「結尾在不同位置」的 subarray 全部考慮
            for m in table[i]:
                ans += table[i][m] * m # 有幾個m, 乘起來就是 sum of m
                ans %= MOD
        return ans
        '''
# case 73/87: 數字太大時，return the answer modulo 10**9 + 7.
# case 82/87: 有大量數字時，Memory爆了！defaultdict()會用太多。要省著用
# 但改用2個hash table輪流用，Time也爆了，因為兩層for迴圈會爆！
