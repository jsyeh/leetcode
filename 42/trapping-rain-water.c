//要記 local maximum
int max(int a, int b){
    if(a>b) return a;
    else return b;
}
int min(int a, int b){
    if(a<b) return a;
    else return b;
}
int trap(int* height, int heightSize){
    if(heightSize==0) return 0;
    int N = heightSize;

    int left_max[N], right_max[N];
    left_max[0] = height[0];
    for(int i=1; i<N; i++){
        left_max[i] = max(height[i], left_max[i-1]);
    }

    right_max[N-1] = height[N-1];
    for(int i=N-2; i>=0; i--){
        right_max[i] = max(height[i], right_max[i+1]);
    }

    int ans = 0;
    for(int i=1; i<N-1; i++){
        ans += min(left_max[i], right_max[i]) - height[i]; 
    }
    return ans;
}
