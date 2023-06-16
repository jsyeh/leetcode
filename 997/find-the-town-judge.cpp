class Solution {
public:
    //先找「沒有相信任何人的人」剛好1人，接下來，便是看大家是否都相信它
    int findJudge(int n, vector<vector<int>>& trust) {
        int trusted[1001]={};
        int trusting[1001]={};
        for(int i=0; i<trust.size(); i++){
            int a = trust[i][0], b = trust[i][1];
            trusted[b]++;//b被多1個人相信
            trusting[a]++;//a相信別人
        }

        int judge=-1, judgeN=0;
        for(int i=1; i<=n; i++){
            if(trusted[i]==n-1 && trusting[i]==0){
                judge=i;
                judgeN++;
            }
        }

        if(judgeN==1) return judge;
        else return -1;
    }
};
