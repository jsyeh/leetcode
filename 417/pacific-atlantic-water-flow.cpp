class Solution {
public:
    int pacific[200][200], atlantic[200][200];
    int M, N;
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        M = heights.size();
        N = heights[0].size();
        for(int i=0; i<M; i++){
            for(int j=0; j<N; j++){
                pacific[i][j] = 0;
                atlantic[i][j] = 0;
            }
        }
        //改成爬山問題

        for(int i=0; i<M; i++){
            helper(heights, i, 0, 0, 1); //pacific
            helper(heights, i, N-1, 0, 2);//atlantic
        }
        for(int j=0; j<N; j++){
            helper(heights, 0, j, 0, 1); //pacific
            helper(heights, M-1, j, 0, 2);//atlantic
        }

        vector<vector<int>> ans;
        for(int i=0; i<M; i++){
            for(int j=0; j<N; j++){
                //printf("%d", pacific[i][j]);
                if(pacific[i][j]==1 && atlantic[i][j]==1){
                    vector<int> temp;
                    temp.push_back(i);
                    temp.push_back(j);
                    ans.push_back(temp);
                }
            }
            //printf("\n");
        }
        return ans;
    }

    void helper(vector<vector<int>>&H, int i, int j, int level, int ocean) {
        //printf("i:%d j:%d\n", i, j);
        if(i<0 || j<0 || i>=M || j>=N) return;
        if(ocean==1 && pacific[i][j]!=0) return;
        if(ocean==2 && atlantic[i][j]!=0) return;

        if(H[i][j]>=level){
            if(ocean==1) pacific[i][j] = 1; //good
            if(ocean==2) atlantic[i][j] = 1; //good
            helper(H, i+1, j, H[i][j], ocean);
            helper(H, i-1, j, H[i][j], ocean);
            helper(H, i, j+1, H[i][j], ocean);
            helper(H, i, j-1, H[i][j], ocean);
        }else{
            //if(ocean==1) pacific[i][j] = 2; //bad
            //if(ocean==2) atlantic[i][j] = 2; //bad
        }
    }
};
