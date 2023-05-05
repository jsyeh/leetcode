class Solution {
    public int maxPoints(int[][] points) {
        int ans=0;
        for(int i=0; i<points.length; i++) {
            //每次挑一個點當基準
            HashMap<Float,Integer> map = new HashMap<>();
            float x = points[i][0], y = points[i][1], slope;
            for(int k=0; k<points.length; k++) {
                if(k==i) continue;
                if(points[k][0]-x==0) slope = Float.MAX_VALUE;
                else slope = (points[k][1]-y) / (points[k][0]-x);
                if(map.containsKey(slope)) {
                    map.put(slope, map.get(slope)+1);
                } else map.put(slope, 1);
                int count = map.get(slope);
                if(count>ans) ans = count;
            }
        }
        return ans+1;
    }
}//case 29/41: [[1,0],[0,0]]
