class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if(intervals.length==0) return 0;

        Arrays.sort(intervals, (a,b) -> a[1]-b[1]);
        //Arrays.sort(intervals, (a,b) -> (a[1]-b[1]==0)?(a[0]-b[0]):(a[1]-b[1]) );
for(int i=0; i<intervals.length; i++){
    System.out.println(intervals[i][0] + " " + intervals[i][1]);
}
        int end=intervals[0][1];
        int ans=1;
        for(int i=1; i<intervals.length; i++){
            if(intervals[i][0]>=end){ //表示有重疊
                end = intervals[i][1];
                ans++;
            }
        }
        return intervals.length-ans;
    }//我有參考 Solutions 裡 crickey180 的思路, 還蠻帥的想法
}//case 4: [[1,100],[11,22],[1,11],[2,12]]
