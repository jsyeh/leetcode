class Solution {
public:
    //這題我又偷看 Editorial 了。它的方法很棒, 就用陣列來處理, 找到可以長大一點的數, 交換後, 右方最小
    //以做出大一點的數
    int nextGreaterElement(int n) {
        //先用剝皮法,把數字分析出來
        int a[10];
        int len=0;
        while(n>0) { //a[i]裡存的,是倒過來的數。之後要反過來做出數字
            a[len] = n % 10;
            n = n / 10;
            len++;
        }
        //從小到大的位數, 逐項找有機會換的數字
        int max = a[0];
        int thePos = -1; //thePos 表示那個 "稍微變小的那個位數" 以與 minI 交換, 如果找不到 就是 -1

        for(int i=0; i<len; i++) { //因為a[i]的位數是倒過來的, 個位數是 a[0], 所以迴圈從0開始
//printf("i:%d a[i]:%d max:%d\n", i, a[i], max);
            if(a[i]<max) { //比最大值小, 就是找到了, 完成任務
                thePos = i;
                break;
            } else if(a[i]>max) {
                max = a[i]; //繼續增加、繼續做
            }
        }
        if(thePos==-1) return -1; //如果找不到 就是 -1

        //找比thePos大的數字中, 最小的數字, 因為要搬來 thsPos使用
        int next = -1;
        for(int i=0; i<thePos; i++){
            if(a[i]>a[thePos]) {
                if(next==-1) next = i;
                else if(a[i]<a[next]) next = i;
            }
        }

        int temp = a[thePos];
        a[thePos] = a[next];
        a[next] = temp;//交換這兩個位數, ans確定就變大了
for(int i=0; i<len; i++) printf("%d ", a[i]);
printf("\nthePos:%d next:%d\n", thePos, next);
        //為了後面考量, 進行排序
        for(int i=0; i<thePos; i++){
            for(int j=i+1; j<thePos; j++){
                if(a[i]<a[j]){
                    temp = a[i];
                    a[i] = a[j];
                    a[j] = temp;
                }
            }
        }


        //最後用倒裝的方法, 再把數字組回去
        long ans = 0;
        for(int i=len-1; i>=0; i--) {
            if(ans*10+a[i]>INT_MAX) return -1;
            //case: 19/39: 2147483486 在組合 2147483 684 時, 超過int的範圍,要return -1

            ans = ans * 10 + a[i];
        }
        return (int)ans;
    }
};
//case 18/39: 230241
//case 19/39: 2147483486 太大, 糟!
