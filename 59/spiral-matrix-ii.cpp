class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> ans(n); //這個二維陣列有n 個 rows
        for(int i=0; i<n; i++){ //裡面每一個row 是 ans[i]
            ans[i] = vector<int>(n); //對應有 n 個 col 的元素
        }

        int i = 0, j = 0;
        int dir = 0; //右、下、左、上
        int di[4] = {0, 1, 0, -1};//上下移動的量
        int dj[4] = {1, 0, -1, 0};//左右移動的量
        int left = 0, right = n-1, up = 1, down = n-1; //事先準備好的邊界

        for(int k = 1; k<=n*n; k++) { //k 是要填入 ans[i][j] 的值
            ans[i][j] = k;
            if(dir==0 && j==right){ //向右走, 碰到右邊界
                dir = 1; //轉方向, 向下
                right--; //右邊界退縮, 供下次碰撞使
            }else if(dir==1 && i==down) { //向下走, 碰到下邊界
                dir = 2; //轉方向, 向左
                down--;  //下邊界退縮, 供下次碰撞使
            }else if(dir==2 && j==left) { //向左走, 碰到左邊界
                dir = 3; //轉方向, 向上
                left++;  //左邊界也改, 供下次碰撞使
            }else if(dir==3 && i==up) { //向上走, 碰到上邊界
                dir = 0; //轉方向, 回到最早的向右
                up++; //上邊界也改, 供下次碰撞使
            }
            i += di[dir]; //有點像 i++ 或 i--, 要看現在走的方向
            j += dj[dir]; //有點像 j++ 或 j--, 要看現在走的方向
        }

        return ans;
    }
};
