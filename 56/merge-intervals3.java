class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a,b)->a[0]-b[0]);
        int N = 0;
        for(int i=1; i<intervals.length; i++) {
            if(intervals[N][1]>=intervals[i][0]) { //需要合併
                intervals[N][1] = Math.max(intervals[N][1], intervals[i][1]);
            }else{ //確定可獨立
                N++;
                intervals[N] = intervals[i];
                //intervals[N][0] = intervals[i][0];
                //intervals[N][1] = intervals[i][1];
            }
        }
        N++;

        int [][] ans = new int[N][2];
        for(int i=0; i<N; i++){
            ans[i] = intervals[i];
            //ans[i][0] = intervals[i][0];
            //ans[i][1] = intervals[i][1];
        }
        return ans;
    }
}
