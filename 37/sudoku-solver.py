# LeetCode 37. Sudoku Solver
# board 是「數獨遊戲」的盤面，把答案填進去。可巧妙使用「函式呼叫函式」嘗試把各種「可能的數字」填進去
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def check(ii,jj):  # 檢查 board[i][j] 這格「可以填哪些數字」
            ans = set( [str(i) for i in range(1,10)] )  # 利用 set 放「可能的答案」'1'~'9'
            for i in range(9):  # 想找 (ii,jj) 對應的直行，逐個值檢查
                now = board[i][jj]  # 這個值 小心是 i 配 jj
                if now != '.' and now in ans: ans.remove(now)  # 這個值用掉了
            if len(ans)==0: return ans  # 這行很重要，提早用盡數字，就提早結束

            for j in range(9):  # 想找 (ii,jj) 對應的橫行，逐個值檢查
                now = board[ii][j]  # 這個值 小心是 ii 配 j
                if now != '.' and now in ans: ans.remove(now)  # 這個值用掉了
            if len(ans)==0: return ans  # 這行很重要，提早用盡數字，就提早結束

            for i in range(ii//3*3, ii//3*3+3):  # 3x3 的正方形 對應的 i
                for j in range(jj//3*3, jj//3*3+3):  # 小正方形 對應的 j
                    now = board[i][j]  # 這個值
                    if now != '.' and now in ans: ans.remove(now)  # 這個值用掉了
            return ans
        def solve():  # 檢查盤面，每次填1個數字，去試試看
            for i in range(9):  # 在盤子裡，還有沒有「沒填數字」的格子
                for j in range(9):
                    if board[i][j]=='.':  # 太好了，找到1格沒填的，專心試它
                        for now in check(i,j):  # 呼叫上面的 check() 找出可能的數
                            board[i][j] = now  # 塞入可能的數
                            if solve()==True: return True  # 函式呼叫函式，若成功，就可結束
                            board[i][j] = '.'  # 若沒成功，就「還原」擦掉數字
                        return False  # 這格「試過所有的值」，都沒成功，那不用玩了，無解，離開
            return True  # 如果都填完了，就順利結束了
        solve()  # 真的去解它囉！解完的答案，都填好、放在 board[i][j] 裡面了
