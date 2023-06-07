class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        if(image[sr][sc]==color) return image;

        helper(image, sr, sc, image[sr][sc], color);

        return image;
    }
    void helper(vector<vector<int>>&image, int sr, int sc, int old, int color) {
        if(sr<0 || sc<0 || sr>=image.size() || sc>=image[0].size()) return;

        if(image[sr][sc]==old) image[sr][sc]=color;
        else return;

        helper(image, sr+1, sc, old, color);
        helper(image, sr-1, sc, old, color);
        helper(image, sr, sc+1, old, color);
        helper(image, sr, sc-1, old, color);
    }
};
