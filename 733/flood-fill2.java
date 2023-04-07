class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if(color==image[sr][sc]) return image;

        int old = image[sr][sc];
        flood(image, sr, sc, old, color);

        return image;
    }
    void flood(int[][] image, int i, int j, int old, int color) {
        if(i<0 || j<0 || i>=image.length || j>=image[0].length) return;
        if(image[i][j]==old){
            image[i][j]=color;
            flood(image, i+1, j, old, color);
            flood(image, i-1, j, old, color);
            flood(image, i, j+1, old, color);
            flood(image, i, j-1, old, color);
        }
    }
}
