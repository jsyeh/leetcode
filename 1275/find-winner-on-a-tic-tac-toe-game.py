class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        table = [[0]*3 for _ in range(3)]
        AB = -1 # [-1, +1] # A:-1, B:+1

        def testWin() -> bool:
            for i in range(3):
                A, B = 0, 0
                for j in range(3):
                    if table[i][j] == -1: A += 1
                    if table[i][j] == +1: B += 1
                if A==3 or B==3: return True

            for j in range(3):
                A, B = 0, 0
                for i in range(3):
                    if table[i][j] == -1: A += 1
                    if table[i][j] == +1: B += 1
                if A==3 or B==3: return True

            A, B = 0, 0
            for i in range(3):
                if table[i][i] == -1: A += 1
                if table[i][i] == +1: B += 1
            if A==3 or B==3: return True

            A, B = 0, 0
            for i in range(3):
                if table[i][2-i] == -1: A += 1
                if table[i][2-i] == +1: B += 1
            if A==3 or B==3: return True

            return False

        for m in moves:
            table[m[0]][m[1]] = AB
            if testWin():
                if AB == -1: return "A"
                else: return "B"
            AB *= -1
        if len(moves)==9:
            return "Draw"
        else:
            return "Pending"
# case 38/100: [[0,0],[1,1]]
