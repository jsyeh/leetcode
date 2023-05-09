// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

int firstBadVersion(int n) {
    long long int left=0, right=n;
    while(left<right){
        long long int mid = (left+right)/2;
        if(isBadVersion(mid)){
            right = mid;
        }else{
            left = mid+1;
        }
    }
    return (int)left;
}//case 11/24: 2126753390 1702766719
