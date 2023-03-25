class Pos {
    int i, j;
    Pos(int _i, int _j){
        i = _i;
        j = _j;
    }
}
class Solution {
    int I, J;
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        I = image.length;
        J = image[0].length;
        //int[][] ans = new int[I][J];
        boolean [][] visited = new boolean[I][J];

        LinkedList<Pos> queue = new LinkedList<Pos>();
        queue.push(new Pos(sr, sc));
        visited[sr][sc]=true;
        int color0 = image[sr][sc];
        image[sr][sc]=color;

        while(queue.size()>0) {
            Pos now = queue.pop();

            testAndAdd(image, now.i-1, now.j, queue, visited, color0, color);
            testAndAdd(image, now.i+1, now.j, queue, visited, color0, color);
            testAndAdd(image, now.i, now.j-1, queue, visited, color0, color);
            testAndAdd(image, now.i, now.j+1, queue, visited, color0, color);
            ////not 8-directionally
            //for(int i=now.i-1; i<=now.i+1; i++){
            //    for(int j=now.j-1; j<=now.j+1; j++){
            //        if(i==now.i && j==now.j) continue;
            //        if(validPos(i,j) && !visited[i][j] && image[i][j]==color0){
            //            queue.push(new Pos(i,j));
            //            visited[i][j]=true;
            //            image[i][j]=color;
            //        }
            //    }
            //}
        }
        //return ans;
        return image;
    }
    void testAndAdd(int[][] image, int i, int j, LinkedList<Pos>queue, boolean[][] visited, int color0, int color) {
        if(validPos(i,j) && !visited[i][j] && image[i][j]==color0){
            queue.push(new Pos(i,j));
            visited[i][j]=true;
            image[i][j]=color;
        }
    }
    boolean validPos(int i, int j) {
        if(i<0) return false;
        if(j<0) return false;
        if(i>=I) return false;
        if(j>=J) return false;
        return true;
    }
}
