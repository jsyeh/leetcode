class Solution {
    public int[][] generateMatrix(int n) {
        int [][] ans = new int[n][n];

        int [] dx = {1,0,-1,0};
        int [] dy = {0,1,0,-1};
        int dir = 0;

        int x=0, y=0, right=n-1, left=0, up=1, down=n-1;
        for(int now=1; now<=n*n; now++){
            ans[y][x] = now;
            if(dir==0 && x==right){
                dir=1;
                right--;
            } else if(dir==1 && y==down) {
                dir=2;
                down--;
            } else if(dir==2 && x==left) {
                dir=3;
                left++;
            } else if(dir==3 && y==up) {
                dir=0;
                up++;
            }
            y+=dy[dir];
            x+=dx[dir];
        }
        return ans;
    }
}
