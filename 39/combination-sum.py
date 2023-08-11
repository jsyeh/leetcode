# 題目分類時，是在 Coin Change/Combination Sum 題型，應該解法類似
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        table = [[] for _ in range(target+1)]
        # print(table) table[taget] 將是答案，裡面有一堆list
        # print(table)

        table[0] = [[]] # 二維陣列，目前是空，加起來剛好是0
        for c in candidates:
            # print(c)
            for i in range(c, target+1):
                # print("i:", i)
                for now in table[i-c]: # 可到達 i-c 格的全部組合
                    # print("now:", now)
                    if now == None:
                        table[i].append([c])
                        # print("table[i]:", table[i])
                    else:                
                        temp = now.copy() 
                        # 這裡卡很久，因now是table[i-c] 不能直接append(c)
                        # 要先copy()後，再append(c) 才不會影響舊資料
                        temp.append(c)    
                        table[i].append(temp)
                        # print("table[i]:", table[i])
                    # print(table[i])
            #print(table)
        return table[target]
