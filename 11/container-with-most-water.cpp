class Solution {
public:
    int maxArea(vector<int>& height) {
        int N = height.size();

        int ans = 0;
        int i=0, j=N-1;
        while(i<j){
            int h = height[i];
            if(h>height[j]) h = height[j];
            if( ans< h*(j-i) ) ans = h*(j-i);
            if(height[i]>height[j]) j--;
            else i++;
        }
        /*
        for(int i=0; i<N; i++){
            for(int j=i+1; j<N; j++){
                int now = (height[i]<height[j])? (j-i)*height[i]: (j-i)*height[j];
                if(now>ans) ans = now;
            }
        }*/
        return ans;
    }
};
