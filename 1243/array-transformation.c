// 有個產生(隔一天) array 的規則:
// 1. 如果左右都比你大, 你要++
// 2. 如果左右都比你小, 你要--
// 3. 頭、尾永不變動
int* transformArray(int* arr, int arrSize, int* returnSize){
    int N = arrSize;
    int arr2[N];
    int same = 0;
    while(same != N-2) {
        same = 0;
        for(int i=1; i<N-1; i++) {
            if(arr[i]<arr[i-1] && arr[i]<arr[i+1]) {
                arr2[i] = arr[i] + 1;
            } else if(arr[i]>arr[i-1] && arr[i]>arr[i+1]) {
                arr2[i] = arr[i] - 1;
            } else {
                arr2[i] = arr[i];
                same++;
            }
        }
        for(int i=1; i<N-1; i++) {
            arr[i] = arr2[i]; //再放回 arr[i]
        }
    }
    *returnSize = N;
    return arr;    
}
