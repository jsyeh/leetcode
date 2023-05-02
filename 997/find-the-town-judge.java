class Solution {
    public int findJudge(int n, int[][] trust) {
        int [] trustedN = new int[n+1];//judged要被相信n-1次
        int [] trusting = new int[n+1];//judge不能相信別人
        for(int i=0; i<trust.length; i++){
            int one = trust[i][0];
            int two = trust[i][1];
            trustedN[two]++;
            trusting[one]++;
        }
        int judgeN=0, judge=0;
        for(int i=1; i<=n; i++){
            if(trustedN[i]==n-1 && trusting[i]==0){
                judge=i;
                judgeN++;
            }
        }
        if(judgeN==1) return judge;
        else return -1;
    }
}
//case 90/92: 3
//[[1,2],[2,3]]
