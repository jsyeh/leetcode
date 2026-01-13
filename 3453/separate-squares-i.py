# LeetCode 3453. Separate Squares I
# squares[i] = [x,y,邊長] 標注許多正方形。找一條橫切的線，讓「上方面積==下方面積」
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def helper(yy):  
            part1, part2 = 0, 0  # yy上方、yy下方
            for x,y,L in squares:
                if y>=yy: part2 += L*L
                elif y+L<=yy: part1 += L*L
                else:
                    part1 += L*(yy-y)
                    part2 += L*(y+L-yy)
            return part1 >= part2  # 如果 true 就讓 right = mid
        # 上面 helper 函式，幫助下面 binary search
        left, right = 0, 10**9
        while left < right and right-left > 0.00001:
            mid = (left+right)/2
            if helper(mid): right = mid
            else: left = mid + 0.00001
        return left
