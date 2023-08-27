# 原本題目看不太懂，就用 Example 1 來理解
#  前一次跳距離k, 下一次跳 k-1 or k or k+1
#  第1次跳必須距離1
# 參考 quencyhehe 解法後，視野開闊 -- 原來可反過來想
#  利用 dict 減少考慮範圍、加速，了解「能到的步數」
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        speed = {} # speed[0] 代表在 0 的石頭，下次跳出去的速度有誰, 是個 list
        # 每次挑1個石頭來研究，看之前青蛙有否跳來（並給新速度)
        # speed[stone] 在這個石頭上，能跳出去的(全部可能的)速度/距離
        for stone in stones: # 0 1 3 5 8 12 17
            speed[stone] = [] # 每個石頭的位置，都加到 speed 裡對應的list，但都還是空的
        speed[0].append(1) # 在位置0的石頭，可以有個（跳出去的）速度 1

        for stone in stones: # 每次挑1個石頭來研究，看之前青蛙有否跳來（並給新速度)
            # speed[stone] 在這個石頭上，能跳出去的(全部可能的)速度/距離
            for k in speed[stone]: # 能跳出去的(全部可能的)速度/距離 k
                next = stone + k # 可以跳到的地方
                if next == stones[-1]: # 可跳到最後1顆石頭
                    return True # 直接結束
                if next in speed: # 有在 speed 抽籤袋子裡,就可跳到next
                    if k-1>0: # 小心，不要往回走，不然迴圈會走不完
                        speed[next].append(k-1)
                    # 因重覆數字不用append，可加速
                    if k not in speed[next]:
                        speed[next].append(k)
                    if k+1 not in speed[next]:
                        speed[next].append(k+1)
        return False
