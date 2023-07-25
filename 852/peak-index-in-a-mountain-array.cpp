class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        /*
        //第一直覺，是直接使用for迴圈巡一輪，就找到答案
        for(int i=0; i<arr.size()-1; i++){
            if(arr[i]>arr[i+1]){
                return i;
            }
        }
        //最右邊是最大時。不過這並不是 mountain array，只是程式最後總是要return嘛
        return arr.size()-1;;
        //不過題目說：You must solve it in O(log(arr.length)) time complexity.
        //所以全部重寫，改用 binary search 的方法來寫
        */
        int left = 0, right = arr.size(); //右邊不包含
        while(1){
            int mid = (left+right)/2;
            if(arr[mid]>arr[mid-1] && arr[mid]>arr[mid+1]) return mid;
            if(arr[mid]<arr[mid-1]){ //太右邊了
                right = mid;
            }else {
                left = mid;
            }
        }
        return left;
    }
};
