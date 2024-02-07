# 是否2字串「只差1個字母」 但10^5 很大，沒辦法暴力算。
# 需使用 HashMap 來加速。但又不能「整個字串」拿來用，因字串太長、太耗記憶體
# votrubac 將字串變成26進位的整數%MOD，並在找到時，再逐字母比對、確認相符。
# 我使用 Python，可使用 dict 對照到 dict[i] 來做，但原參數 dict 要改名
class Solution:
    #def differByOne(self, dict: List[str]) -> bool:
    def differByOne(self, words: List[str]) -> bool:
        table = {} # table[整數]對應 words[i] 的 [i]
        # 要把 words[i] 轉換成整數
        # 如果 hash collision 時，就 append到list後面
        M, N = len(words), len(words[0])
        hashAll = [0]*M # 存「完整」的「字母hash值」
        MOD = 10**9+7
        for i in range(M):
            for j in range(N): # 轉成 26進位 的數字
                hashAll[i] = (hashAll[i]*26 + (ord(words[i][j])-ord('a')))%MOD
        
        # 模仿 votrubac 用的 Robin-Karp 法
        mult26 = 1 # 用來做26進位的「倍數」
        for j in range(N-1,-1,-1): # 逐位去扣除，從最右邊低位開始
            for i in range(M): # 逐字去處理、對應hashAll[i]扣除
                now = ord(words[i][j])-ord('a')
                h = (hashAll[i]-mult26*now+MOD) % MOD
                if h in table: # hash 發找到了，要再確認是否正確
                    for ii in table[h]:
                        if ii == i: continue # 本身不計。 下面則是再檢查是否「只差1個字母」
                        if words[i][:j]==words[ii][:j] and words[i][j+1:]==words[ii][j+1:]:
                            return True # 太好了，找到了
                    # 但若整組找過，都沒有相同的話，那就是 hash collision 誤判
                    table[h].append(i) # 就再加現在這組i
                else: table[h] = [i] # hash h 之前沒出現過，就新增1組list [i]
            mult26 = (mult26*26) % MOD # 隨著 j 將 mult26 倍數增加
        return False # 都沒有成功找到，就false
        '''
        M, N = len(dict), len(dict[0])
        s = set()
        for word in dict:
            for i in range(N): # 逐字母取代
                now = word[:i]+'.'+word[i+1:]
                if now in s: return True # 找到有重覆
                s.add(now) # 字串當 hash key 太長了，要簡化
        return False # 都沒有成功
        '''
# case 74/81: 超長的字串2個，造成 Memory Limit Exceeded
# 所以取 hash 時，不能整個字串都丟入。要簡化成整數 % MOD 才行
# 而且它經過巧妙設計，剛好會發生錯誤的 hash collision 要再檢查才行
