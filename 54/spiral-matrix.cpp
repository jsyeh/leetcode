class Solution {
public: //用C++寫 今天挑戰題 LeetCode 54 迴旋
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> ans; //step01
        int M = matrix.size(); //step03
        int N = matrix[0].size(); //step03
        int i=0, j=0; //step04
        int dir=0; //0:右, 1:下, 2:左, 3:右
        //int di=0, dj=1;//要轉向 //step05
        int di[4] = {0, 1, 0, -1};
        int dj[4] = {1, 0, -1, 0};
        int left=0, right=N-1, up=1, down=M-1;//上下左右邊界
        for(int k=0; k<M*N; k++){
            ans.push_back( matrix[i][j] );//step04
            if(dir==0 && j==right){ //往右,遇到右邊界,轉方向(並改變新邊界)
                dir++; //step06
                right--;
            }else if(dir==1 && i==down){ //往下,遇到下邊界(並改變新邊界)
                dir++; //step06
                down--;
            }else if(dir==2 && j==left){ //往左,遇到左邊界(並改變新邊界)
                dir++; //step06
                left++;
            }else if(dir==3 && i==up){ //往上,遇到上邊界(並改變新邊界)
                dir = 0; //step06再回到右方向
                up++;
            }
            i += di[dir];//step05遇到邊界要轉向
            j += dj[dir];
        }
        return ans; //step01
    }
};
        //for(int i=0; i<M; i++){ //step03
        //    for(int j=0; j<N; j++){ //step03
        //        matrix[i][j]; //step02
        //    }
        //}
