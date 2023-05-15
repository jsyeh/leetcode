class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int M = matrix.size(), N = matrix[0].size();
        int left=0, right = M*N;
        while(left<right){
            int mid = (left+right)/2;
            printf("left:%d mid:%d right:%d\n", left, mid, right);
            int i = mid/N, j = mid%N;
            if(matrix[i][j]==target) return true; //小心
            if(matrix[i][j]<target) left = mid+1;
            else right = mid;
        }
        return false;
/*        printf("left:%d\n", left);
        if(left<M*N && matrix[left/N][left%N]==target) return true;
        else return false;*/
    }
};
//case 3/133: [[1]] 1
//case 4/133: 
