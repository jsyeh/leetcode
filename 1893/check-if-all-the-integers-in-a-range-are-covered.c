// LeetCode 1893. Check if All the Integers in a Range Are Covered
// 測試 left...right 裡的整數，是否都有在 ranges 裡
bool isCovered(int** ranges, int rangesSize, int* rangesColSize, int left, int right) {
    int s[60] = {};
    for(int i=0; i<rangesSize; i++){
        for(int k=ranges[i][0]; k<=ranges[i][1]; k++){
            s[k] = 1;
        }
    }
    for(int now=left; now<=right; now++){
        if(s[now]==0) return false;
    }
    return true;
}
