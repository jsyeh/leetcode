class Solution {
public:
    queue<int> Qi;
    queue<int> Qj;
    queue<int> D;
    int M, N;
    int ans = -1;
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        M = maze.size();
        N = maze[0].size();
//printf("M:%d N:%d\n", M, N);
        
        Qi.push(entrance[0]);
        Qj.push(entrance[1]);
        D.push(0);
        maze[entrance[0]][entrance[1]]='e'; //entrance

        while(Qi.size()>0) {
            int i = Qi.front(); Qi.pop();
            int j = Qj.front(); Qj.pop();
            int dist = D.front(); D.pop();

            testAndPush(maze, i+1, j, dist+1);
            testAndPush(maze, i-1, j, dist+1);
            testAndPush(maze, i, j+1, dist+1);
            testAndPush(maze, i, j-1, dist+1);
        }
        return ans;
    }
    void testAndPush(vector<vector<char>>& maze, int i, int j, int dist) {
        if(i<0 || j<0 || i>=M || j>=N) return;

//printf("i:%d j:%d, maze[i][j]:%c\n", i, j, maze[i][j] );
        if(ans==-1 && maze[i][j]=='.' && (i==0||j==0||i==M-1||j==N-1)){
            ans = dist;
        }
        if(maze[i][j]=='.'){
            maze[i][j]='v';//visited
            Qi.push(i);
            Qj.push(j);
            D.push(dist);
        }
    }
};
