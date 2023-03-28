class Solution {
    public int meetRequirement(int n, int[][] lights, int[] requirement) {
        int [] diff = new int[n+1]; //額外加一格，因為程式習慣右邊界不包含
        for(int i=0; i<lights.length; i++){
            int a = lights[i][0]-lights[i][1];
            int b = lights[i][0]+lights[i][1]+1;//額外加一格，程式習慣右邊界不包含
            if(a<0) a=0;
            if(b>n-1) b = n;//額外加一格，程式習慣右邊界不包含
            diff[a]++;
            diff[b]--;
        }//不能用兩層迴圈，因為 10^10 會超時
        //可改成設定改變量 diff[i]
        int now = 0, ans = 0;
        for(int i=0; i<n; i++){
            System.out.print(diff[i]+" ");
            now += diff[i];
            if(now>=requirement[i]) ans++;
        }
        return ans;
    }
}//Case3: n=1, lights=[[0,0]], requirement=[1]
