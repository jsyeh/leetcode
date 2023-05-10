class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int N = intervals.length;
        int [][] all = new int[N+1][];
        for(int i=0; i<N; i++) {
            all[i] = intervals[i];
        }
        all[N] = newInterval;
        Arrays.sort(all, (a,b)->a[0]-b[0]);

        int k=0;
        for(int i=1; i<=N; i++){
            if(all[k][1] >= all[i][0]) {
                all[k][1] = Math.max(all[k][1], all[i][1]);
            }else{
                k++;
                all[k] = all[i];
            }
        }
        k++;

        int [][] ans = new int[k][];
        for(int i=0; i<k; i++){
            ans[i] = all[i];
        }

        return ans;
    }
}
/*class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        //Arrays.sort(intervals, (a,b)->a[0]-b[0]);
        int N=intervals.length;
        if(N==0) { //test case 75/156 前面是空的，直接填答案
            int [][] ans = new int[1][2];
            ans[0] = newInterval;
            return ans;
        }
        for(int i=0; i<intervals.length; i++){
            if(intervals[i][0]<=newInterval[0] && intervals[i][1]>=newInterval[0]){
                //找到適當的插入點，插入
                intervals[i][1] = Math.max(newInterval[1], intervals[i][1]);
                //case 76/156: [[1,5]] [2,3]

                //之後，把intervals 後續逐項檢查
                N = i;
                break;
            }
        }
        for(int k=N+1; k<intervals.length; k++) {
            if(intervals[N][1]>=intervals[k][0]) {
                intervals[N][1] = Math.max(intervals[k][1], intervals[N][1]);
            } else {
                N++;
                intervals[N] = intervals[k];
            }
        }
        N++;
        int [][] ans = new int[N][2];
        for(int i=0; i<N && i<intervals.length; i++){
            ans[i] = intervals[i];
        }
        if(intervals.length<N){
            ans[N-1] = newInterval;
        }
        return ans;
    }
}*/
//case 75/156: [] [5,7] 
//case 76/156: [[1,5]] [2,3] 收尾要使用 max
//case: [[1,5]] [6,8] 沒想到變長了。
//case 129/156: [[1,5]] [0,3] 實在是問題太多了。還是重寫吧!
