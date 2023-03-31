class Solution {
    //研究 Rebite Sun 的程式 https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/solutions/666985/Java-2-d-accumulation-sum-(rectangular-sum)/
    int [][][] table;
    int [][] sum;
    public int ways(String[] pizza, int k) {
        //You have to cut the pizza into k pieces using k-1 cuts. 
        //意思是，要分變k個人，所以要切 k-1 刀
        int I = pizza.length, J = pizza[0].length();

        sum = new int[I+1][J+1];//大一點，右邊界、下邊界是0
        //sum[i][j]存的值，是它右下方管的Apple數，含本身
        for(int i=I-1; i>=0; i--){
            int right = 0; //第i列 右邊累積的apple數
            for(int j=J-1; j>=0; j--){
                if(pizza[i].charAt(j)=='A') right++;
                sum[i][j] = sum[i+1][j] + right; //下方管的+右方那條
            }
        }
        int MOD = 1000000007;
        table = new int[k+1][I+1][J+1];
        //table[切幾刀][某個位置][某個位置] 的總共方法

        for(int i=0; i<=I; i++){
            for(int j=0; j<=J; j++){
                if(sum[i][j]==0) table[1][i][j] = 0;//如果右下都沒有，就絕對不能切，cutN為1是不可能的
                else table[1][i][j] = 1; //有的話，就可在這切1，分給1人
                //System.out.print(sum[i][j] + " ");
            }
            //System.out.println();
        }
        for(int cutN=2; cutN<=k; cutN++) {
            for(int i=I-1; i>=0; i--) {
                for(int j=J-1; j>=0; j--) {
                    int t1 = 0; //統計這次有幾種切法
                    for(int cut=j+1; cut<J; cut++) { //橫切
                        if(sum[i][j]>sum[i][cut]) { //左上比右下大，可以在這裡切一刀，加
                            t1 = (t1 + table[cutN-1][i][cut] ) % MOD;
                            //System.out.print(".");
                        }
                    }
                    //System.out.println();
                    for(int cut=i+1; cut<I; cut++) { //直切
                        if(sum[i][j]>sum[cut][j]) {
                            t1 = (t1 + table[cutN-1][cut][j] ) % MOD;
                            //System.out.print(".");
                        }
                    }
                    table[cutN][i][j] = t1;
                }
            }
        }
        return table[k][0][0];
    }
}
