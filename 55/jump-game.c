bool canJump(int* nums, int numsSize){
    bool visited[numsSize+1];
    for(int i=0; i<=numsSize; i++) visited[i] = false;

    visited[0] = true;
    for(int i=0; i<numsSize; i++){
        if(visited[i]){
            for(int k=i+1; k<=i+nums[i] && k<numsSize; k++){
                visited[k]=true;
            }
        }
    }
    if(visited[numsSize-1]) return true;
    else return false;
}
