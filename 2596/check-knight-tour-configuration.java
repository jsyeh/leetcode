class Pos{
  int x;
  int y;
  Pos(int _x, int _y){
    x = _x;
    y = _y;
  }
};

class Solution {
    Pos[] pos;
    public boolean checkValidGrid(int[][] grid) {
      if(grid[0][0]!=0) return false;
        
      int N = grid.length;
      pos = new Pos[N*N];
      for(int i=0; i<grid.length; i++){
        for(int j=0; j<grid[i].length; j++){
          int step = grid[i][j];
          pos[step] = new Pos(i, j);
        }
      }
      
      for(int i=1; i<N*N; i++){
        if(!check(i)) return false;
      }
      return true;
    }
    int abs2(int d){
      if(d<0) return -d;
      return d;
    }
    boolean check(int i){
        int dx = abs2(pos[i-1].x-pos[i].x);
        int dy = abs2(pos[i-1].y-pos[i].y);
        if(dx==1&&dy==2) return true;
        if(dx==2&&dy==1) return true;
        return false;      
    }
}
//Case 3: [[24,11,22,17,4],[21,16,5,12,9],[6,23,10,3,18],[15,20,1,8,13],[0,7,14,19,2]]
//true false false
