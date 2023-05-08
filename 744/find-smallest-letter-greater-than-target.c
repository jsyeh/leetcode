char nextGreatestLetter(char* letters, int lettersSize, char target){
    int left=0, right = lettersSize;

    while(left<right){
//printf("%d %d\n", left, right);
        int mid = (left+right)/2;
        if(letters[mid]<=target){
            left = mid+1;
        }else{
            right = mid;
        }
    }
//printf("final: %d %d\n", left, right);
    //if(letters[left]>=target) return letters[0];
    if(left>=lettersSize) return letters[0];
    else return letters[left];
}
