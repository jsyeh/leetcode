class Solution {
    public int[][] kClosest(int[][] points, int k) {
        int [][] ans = new int[k][2];

        PriorityQueue<int[]> heap = new PriorityQueue<int[]>((a,b)->(a[0]*a[0]+a[1]*a[1]-b[0]*b[0]-b[1]*b[1]));
        for(int i=0; i<points.length; i++){
            heap.offer(points[i]);
        }
        for(int i=0; i<k; i++){
            ans[i] = heap.poll();
        }
        return ans;
    }
}
