/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

int guessNumber(int n){
	long long int left = 0, right = n+(long long int)1;
    while(left<right){
        long long int mid = (int)((left+(long long int)right)/2);
        int temp = guess(mid);
        if(temp==0) return (int)mid;
        else if(temp==1){
            left = mid+1;
        }else{
            right = mid;
        }
    }
    return 0;
}//case 14/25: 2126753390 1702766719 數字太大時，右邊界會overflow
//case 24/25: 2147483647 2147483647 右邊界+1就爆了！
