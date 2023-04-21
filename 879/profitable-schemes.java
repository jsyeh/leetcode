class Solution {
    int max(int a, int b) {
        if(a>b) return a;
        else return b;
    }
    public int profitableSchemes(int n, int minProfit, int[] group, int[] profit) {
        int crimeN = group.length;//有多少種犯罪
        long [][][] table = new long[crimeN+1][minProfit+1][n+1];

        table[0][0][0] = 1; //不賺錢的方法有1種，就是都沒有
        for(int crime=1; crime<=crimeN;crime++) {
            for(int members = 0; members<=n; members++) {
                for(int earn = 0; earn<=minProfit; earn++) {
                    table[crime][earn][members] = table[crime-1][earn][members];
                    if(members>=group[crime-1]){//現在人數夠進行第crime-1犯罪
                        int p = profit[crime-1], m = group[crime-1];//需要m個人，可賺p元
                        int prevEarn = max(earn-p, 0);
                        table[crime][earn][members] += table[crime-1][prevEarn][members-m];//也能這樣賺錢，加起來
                        table[crime][earn][members] = table[crime][earn][members] %1000000007;
                    }
                }
            }
        }

        long ans=0;
        for(int member=0; member<=n; member++){
            ans = (ans +table[crimeN][minProfit][member])%1000000007;
        }
        return (int) ans;

        /*
        int CrimeN = group.length;
        int [][] table = new int[n+1][CrimeN+1];
        //table[人數][目前考慮的犯罪種類] 可賺多少錢
        for(int i=0; i<=n; i++){
            table[i][0]=0;
        }
        for(int crimeType=1; crimeType<=CrimeN; crimeType++) {
            for(int i=0; i<=n; i++) {
                int diff = group[crimeType-1];//要增加這種犯罪，要多少人
                if(i>=diff){
                    table[i][crimeType] = table[i-diff][crimeType-1]+profit[crimeType-1];
                }
            }
            
        }*/
    }
}//case 40/45: 100 100 [2,5,36,2,5,5,14,1,12,1,14,15,1,1,27,13,6,59,6,1,7,1,2,7,6,1,6,1,3,1,2,11,3,39,21,20,1,27,26,22,11,17,3,2,4,5,6,18,4,14,1,1,1,3,12,9,7,3,16,5,1,19,4,8,6,3,2,7,3,5,12,6,15,2,11,12,12,21,5,1,13,2,29,38,10,17,1,14,1,62,7,1,14,6,4,16,6,4,32,48]
//[21,4,9,12,5,8,8,5,14,18,43,24,3,0,20,9,0,24,4,0,0,7,3,13,6,5,19,6,3,14,9,5,5,6,4,7,20,2,13,0,1,19,4,0,11,9,6,15,15,7,1,25,17,4,4,3,43,46,82,15,12,4,1,8,24,3,15,3,6,3,0,8,10,8,10,1,21,13,10,28,11,27,17,1,13,10,11,4,36,26,4,2,2,2,10,0,11,5,22,6]
