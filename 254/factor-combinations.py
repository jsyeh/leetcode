# 本來我想要用因數分解，然後算出全部的因數乘起來的組合
# 先做質因數分解，接下來印出排列組合。但寫完程式後，發現排列組合寫不出來。改參考下面網址
# https://leetcode.com/problems/factor-combinations/solutions/943983/python-recursive-dfs-beats-95-explanation-easy/?envType=study-plan&envId=dynamic-programming-ii&plan=dynamic-programming

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        ans = [] # 裡面會放很多 list
        
        def solver(remain, now): # now 是部分結果，會持續長大
            if now: # 如果不是空的 list，也就是有部分答案時
                ans.append(now+[remain]) # 把子問題的n加到後面「剩下的直接全上」
                # 部分結果裡，在最後面補上 [remain] 當成是補完的結果
            
            # 接下來要再拆解 remains 成為更細的結果
            for i in range(2, int(math.sqrt(remain))+1): # sqrt() 讓範圍小，可加速
                if remain%i==0: # 逐一去測試
                    if now and i < now[-1]: 
                        # 若不是第一次進來/有部分結果，且now的最後一筆比較大
                        continue # 那就是 i 之前用過了，不要再加進去，以保持遞增
                    solver(int(remain/i),now+[i])
                    # 不然的話，恭喜，把 [i] 加到 list now 部分結果的後面
        
        solver(n,[])
        return ans
