// LeetCode 941. Valid Mountain Array
// 確認 arr 是先增加、再減少，像山一樣
bool validMountainArray(int* arr, int arrSize){
    if(arrSize<3) return false; // 長度不夠
    if(arr[0]>=arr[1]) return false; // 先確認：開始是否變高。不是變高，就失敗
    int state = 0; // 先往上
    for(int i=1; i<arrSize-1; i++){
        if(arr[i]==arr[i+1]) return false; // 相等，就失敗
        if(state==0){
            if(arr[i]>arr[i+1]) state = 1; // 變成向下
        }else{ // 目前向下
            if(arr[i]<arr[i+1]) return false;
        }
    }
    if(state==1) return true;
    else return false;
}
