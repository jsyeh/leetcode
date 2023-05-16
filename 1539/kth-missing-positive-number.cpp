class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int N = 1;
        for(int i=0; i<arr.size(); i++) {
            if(arr[i]>N) { //代表有missing發生
                if(arr[i]-N>=k) { //missing的數量夠多，則Kth在這裡
                    return N+k-1;
                }else{
                    k -= (arr[i]-N);
                    N = arr[i]+1;
                }
            }else N++;
        }
        return N+k-1;
    }
};
