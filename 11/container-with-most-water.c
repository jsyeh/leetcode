int maxArea(int* height, int heightSize){
    int ans=0;
    int left=0, right=heightSize-1;
    while(left<right){
        int min = (height[left]<height[right]) ? height[left] : height[right];
        int temp = (right-left)*min;
        if(temp>ans) ans = temp;
        if(height[left]>height[right]) right--;
        else left++;
    }
    return ans;
}
