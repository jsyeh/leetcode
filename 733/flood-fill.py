class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image # 如果一開始就一致，不用再著色，直接結束
        
        M, N = len(image), len(image[0])
        oldC = image[sr][sc]
        visited = [[False]*N for _ in range(M)]

        Q = deque()
        Q.append( (sr,sc) )
        image[sr][sc] = color
        visited[sr][sc] = True

        def testAndPush(i, j):
            if i<0 or j<0 or i>=M or j>=N:
                return
            if not visited[i][j] and image[i][j] == oldC:
                Q.append( (i,j) )
                image[i][j] = color
                visited[i][j] = True

        while len(Q)>0:
            i, j = Q.pop()
            testAndPush(i+1, j)
            testAndPush(i-1, j)
            testAndPush(i, j+1)
            testAndPush(i, j-1)
        
        return image
