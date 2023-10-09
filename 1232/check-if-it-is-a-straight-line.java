class Solution {
    public boolean checkStraightLine(int[][] coordinates) {
        int N = coordinates.length;
        int dx = coordinates[1][0] - coordinates[0][0];
        int dy = coordinates[1][1] - coordinates[0][1];
        for(int i=2; i<N; i++){
            int dx2 = coordinates[i][0] - coordinates[0][0];
            int dy2 = coordinates[i][1] - coordinates[0][1];
            if(dx*dy2!=dy*dx2) return false;
        } // 交叉相乘，便能知「比例」是否一樣
        return true;
    }
}
