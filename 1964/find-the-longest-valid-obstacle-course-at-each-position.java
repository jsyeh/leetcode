class Solution {
    public int[] longestObstacleCourseAtEachPosition(int[] obstacles) {
        int N = obstacles.length;
        int [] ans = new int[N];
        int [] lis = new int[N];
        int lisN=0;
        for(int i=0; i<N; i++){
            int idx = myBinarySearch(lis, obstacles[i], lisN);
            if(idx==lisN) lisN++;

            ans[i] = idx + 1;
            lis[idx] = obstacles[i];
        }
        return ans;
    }
    int myBinarySearch(int[] lis, int target, int right) {
        if(right==0) return 0;
        int left = 0;
        while(left<right) {
            int mid = (left+right)/2;
            if(lis[mid]<=target){ //這裡為什麼<=，我還沒有搞懂。但我試 < 會錯誤，所以只好改成<=
                left = mid + 1;
            }else{
                right = mid;
            }
        }
        return left;
    }

}
