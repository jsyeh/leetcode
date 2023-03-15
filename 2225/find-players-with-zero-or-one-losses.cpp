class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        vector<vector<int>> ans(2);

        int Lost[100001]={}, Play[100001]={};
        int N = matches.size();
        int maxN = 0;
        for(int i=0; i<N; i++){
            int m1 = matches[i][0], m2 = matches[i][1];
            Lost[m2]++;
            Play[m1]++;
            Play[m2]++;
            if(m1>maxN) maxN=m1;
            if(m2>maxN) maxN=m2;
        }
        for(int i=1; i<=maxN; i++){
            if(Play[i]>0 && Lost[i]==0) ans[0].push_back(i);
            if(Play[i]>0 && Lost[i]==1) ans[1].push_back(i);
        }
        return ans;

    }
};
