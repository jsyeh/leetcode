class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a,b)->a[0]-b[0]);
        int N = 1;
        for(int i=1; i<intervals.length; i++) {
            if(inRange(intervals[i][0], intervals[N-1])) {
                intervals[N-1][1] = max(intervals[N-1][1],intervals[i][1]);
            } else {
                intervals[N][0] = intervals[i][0];
                intervals[N][1] = intervals[i][1];
                N++;
            }
        }
        int [][] ans = Arrays.copyOf(intervals, N);
        return ans;
    }
    int max(int a, int b) {
        return (a>b)?a:b;
    }
    boolean inRange(int a, int [] range) {
        return range[0]<=a && a<=range[1];
    }
}
