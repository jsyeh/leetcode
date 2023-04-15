class Solution {
    public int maxValueOfCoins(List<List<Integer>> piles, int k) {
        Integer table[][] = new Integer[2001][2001]; //table[i][k] 表示使用i組pile,要取k個的最大值
        //邊界是問題，因每個pile[i].length都不同
        for(int i=0; i<piles.size(); i++) table[i][0] = 0;
        for(int j=1; j<=k; j++){
            if(j-1<piles.get(0).size()) table[0][j] = table[0][j-1] + piles.get(0).get(j-1);
            else table[0][j] = 0;//table[0][j-1];
//System.out.print(table[0][j]+" ");
        }
//System.out.println("zzz");

        for(int i=1; i<piles.size(); i++){//1000次
            for(int j=1; j<=k; j++){//1000次
                //要再加一層kk 看第i個pile要取幾個的值
                int max = table[i-1][j];//kk取0個，就是前一項
                int tempSum=0;
                for(int kk=1; kk<=k && j-kk>=0 && kk<=piles.get(i).size(); kk++){//1000次，超時,改過
                    if(kk<=piles.get(i).size() && j-kk>=0){
                        tempSum += piles.get(i).get(kk-1);
                        if(max<tempSum+table[i-1][j-kk]) max = tempSum+table[i-1][j-kk];
                    }
                }
                table[i][j] = max;
//System.out.print(table[i][j]+" ");
            }
//System.out.println();
        }
        return table[piles.size()-1][k];
    }
    int max(int a, int b) {
        if(a>b) return a;
        else return b;
    }
}//case 3 超過時間,加了1003項 (119/122 test cases passed)
//case 4 超過時間, (120 test cases passed)
