class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        dir = 0 # 0:right, 1:down, 2:left, 3:up
        di = [0,1,0,-1]
        dj = [1,0,-1,0]
        M, N = len(matrix), len(matrix[0])
        left, right = 0, N-1
        up, down = 1, M-1
        nowI, nowJ = 0, 0
        while len(ans)<M*N: # 還沒湊齊, 就繼續
            ans.append(matrix[nowI][nowJ])
            if dir==0 and nowJ==right: 
                dir = (dir+1)%4
                right -= 1
            elif dir==1 and nowI==down: 
                dir = (dir+1)%4
                down -= 1
            elif dir==2 and nowJ==left: 
                dir = (dir+1)%4
                left += 1
            elif dir==3 and nowI==up: 
                dir = (dir+1)%4
                up += 1
            nowI += di[dir]
            nowJ += dj[dir]
        return ans
