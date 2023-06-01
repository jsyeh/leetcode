class Step{
public:
    int i, j, step;
    Step(int _i, int _j, int _step){
        i = _i;
        j = _j;
        step = _step;
    }
};

class Solution {
public:
    queue<Step> Q;
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int N = grid.size();
        //Step first(0, 0, 0);
        if(grid[0][0]!=0) return -1;
        else Q.push(Step(0,0,1));//else Q.push(first);
        grid[0][0] = 1;//偷改grid,以免再走進來一次

        while(Q.size()>0) {
            Step now = Q.front();
            if(now.i==N-1 && now.j==N-1) return now.step;
            testAndPush(now.i-1, now.j-1, now.step+1, grid);
            testAndPush(now.i-1, now.j, now.step+1, grid);
            testAndPush(now.i-1, now.j+1, now.step+1, grid);
            testAndPush(now.i, now.j-1, now.step+1, grid);
            testAndPush(now.i, now.j+1, now.step+1, grid);
            testAndPush(now.i+1, now.j-1, now.step+1, grid);
            testAndPush(now.i+1, now.j, now.step+1, grid);
            testAndPush(now.i+1, now.j+1, now.step+1, grid);
            Q.pop();
        }
        return -1; //沒辦法走到右下角
    }
    void testAndPush(int i, int j, int step, vector<vector<int>>&grid) {
        int N = grid.size();
        if(i>=0 && j>=0 && i<N && j<N && grid[i][j]==0) {
            Q.push(Step(i,j,step)); 
            grid[i][j] = 1; //偷改grid,以免再走進來一次
        }
    }
};
//case 62/89: [[0,1,1,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,1,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]]
