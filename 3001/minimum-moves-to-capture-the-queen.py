# 白色城堡rook 及 白色主教bishop 要圍攻 黑色皇后queen
# 白色要連走幾步，才能吃掉「黑皇后」（它不會動）
# 觀察後，發現最多2步，一定可以吃掉，因為城堡一定可以移過去（就算擋住，也能繞道避開）
# 但主教若「卡在中間」，那要先把主教「移開」，就多1步了
# 主教「如果棋盤的格子同色」，也能2步內吃掉queen。但城保「卡在中間」也要再移開。
# 但，等等！會不會上面兩個「可以互相取代？」也就是城保卡住時，主教可代勞。城堡卡住時，主教可代勞？ 可
# 有了「繞道」，保證「一步」or「兩步」就可完成任務

class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # 先看是否有「一步擊殺」的狀況
        # (1) 城堡在同一條線，且中間沒有主教擋住
        if e==a or f==b: # 在同一條線
            if  e==a and e==c and (b<d<f or f<d<b): # 主教卡在中間
                return 2 
            elif f==b and f==d and (a<c<e or e<c<a): # 主教卡在中間
                return 2
            else: return 1 # 恭喜 「一步擊殺」
        # (2) 主教在同一斜線，且中間沒有城堡擋住
        print(c+e==d-f)
        if c-d==e-f or c+d==e+f: # 在同一斜線
            #print('bishop') # debug 用
            if c-d==e-f and a-b==e-f and (d<b<f or f<b<d): # 城堡卡在中間
                #print('case 1') # debug 用
                return 2
            elif c+d==e+f and a+b==e+f and (d<b<f or f<b<d): # 城堡卡在中間
                #print('case 2') # debug 用
                return 2
            else: return 1 # 恭喜 「一步擊殺」
        # 沒有「一步擊殺」那就是「兩步擊殺」
        #print('case 3') # debug 用
        return 2
# case 685/743: 4 3 3 4 2 5
#   0 1 2 3 4 5 6 7
# 0
# 1
# 2           Q
# 3         B
# 4       R
# 5
# 6
# 7
