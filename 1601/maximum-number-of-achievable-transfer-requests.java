//這題 Editorial 的解法有 backtracking 及 bit masking
//昨天的題目2023-07-01也是 bit masking 相關，可以練練
class Solution {
    public int maximumRequests(int n, int[][] requests) {
        int R = requests.length;
        int maskRange = 1 << R, maskAll = maskRange - 1;
        int ans = 0;
        for(int mask = 0; mask < maskRange; mask++) {
            int [] degree = new int[n]; //in out 次數
            int ok = 0; //requests ok 的數量
            for(int i = 0; i < R; i++) { //針對 requests 逐一分析
                int [] r = requests[i];
                if( (mask & (1<<i)) > 0 ) { //mask對應bit有，要用它
                    degree[r[0]]--; //離開
                    degree[r[1]]++; //移入
                    ok++; //多考慮1個request ok 的數量
                }
            }
            int bad = 0;
            for(int i = 0; i < n; i++){
                if(degree[i] != 0) bad = 1;
//System.out.print(degree[i] + " ");
            }
//System.out.println("bad:" + bad + " ok:" + ok);
            if(bad == 0 && ok > ans) ans = ok; //沒問題，
        }
        return ans;
    }
}
