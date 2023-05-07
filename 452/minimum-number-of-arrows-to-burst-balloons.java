class Solution {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, (a,b)->Integer.compare(a[1],b[1]));
        int N = points.length;
for(int i=0; i<N; i++) System.out.printf("[%d,%d],", points[i][0], points[i][1]);

        int ans=1;
        int right = points[0][1];
        for(int i=0; i<N; i++) {
            if(points[i][0]<=right) { //很好，繼續加

            } else { //糟，超過了
                ans++;
                right = points[i][1];
            }
        }
        return ans;
    }
}//[[-2147483646,-2147483645],[2147483646,2147483647]]
