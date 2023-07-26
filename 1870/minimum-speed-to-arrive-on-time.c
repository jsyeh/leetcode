bool possible(int* dist, int distSize, double hour, int speed){
    double t = 0;
    for(int i=0; i<distSize-1; i++){
        t += dist[i]/speed;
        if(dist[i]%speed>0) t++;
    }
    t += dist[distSize-1]/(double)speed; //最後一趟可能有小數
printf("t:%lf hour:%lf, possible:%d\n", t, hour, t<=hour);
    if(t>hour) return false;
    else return true;
}
int minSpeedOnTime(int* dist, int distSize, double hour){
//感覺binary search 可以解
//dist有 10^5 項，所以不能經常去巡 dist[i]
//可先快速淘汰不合理的答案
    if(distSize-1>=hour) return -1; //因為每趟要1小時（最後一趟不用滿1小時）

    int left = 1, right = 10000001; //因為 dist[i] <= 10^5 ，另外hour到小數點下2位
    //There will be at most two digits after the decimal point in hour.
    //最極端的狀況是 [1,1,100000] 2.01 所以最快就必須 100 * 100000 也就是 10^7
    while(left<right){
        int mid = (left+(double)right)/2; //左包含、右不包含
        //這裡可能 Overflow，所以要轉換一下
//printf("left:%d right:%d mid:%d\n", left, right, mid);
        if(possible(dist,distSize, hour, mid)){
            right = mid;
        }else left = mid+1; 
    }
    return left;
}
//case 45/65: [6,10,5,1,8,9,2] 34.0
//case 64/65: [1,1] 1.0
