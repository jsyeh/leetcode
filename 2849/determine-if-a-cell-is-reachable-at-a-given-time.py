# 給定2個座標，每次可走8個方向，問能不能在t步後走到目標fx,fy
# 因為可以走「廢步」來湊步數，所以只要確定最短距離是t即可
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if t==1 and sx==fx and sy==fy:
            return False # 特別處理 case 799/806 的 1 2 1 2 1
        dx, dy = abs(sx-fx), abs(sy-fy)
        if max(dx,dy)<=t: # 至少要走 max(dx,dy) 的距離，
            return True
        else:
            return False
# case 694/806: 1 1 1 3 2 (可在2步內走到, 要有等號)
# case 799/806: 1 2 1 2 1 (不幸的是，如果在原地，走出去1步就離開了)
