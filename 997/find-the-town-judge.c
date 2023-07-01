int findJudge(int n, int** trust, int trustSize, int* trustColSize){
    int trusted[1001]={};
    int trusting[1001]={};
    for(int i=0; i<trustSize; i++){
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
