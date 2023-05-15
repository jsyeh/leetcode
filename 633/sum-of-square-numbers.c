bool judgeSquareSum(int c){
    //在 test case 126/127: c:0 時出錯
    for(long long a=0; a*a<=c; a++){
        //a*a+b*b=c
        double b = sqrt(c-a*a);
        printf("b: %lf %d\n", b, (int)b);
        if(b==(int)b){
            printf("a:%lld b:%d\n", a, (int)b);
            return true;
        }
    }
    return false;
}
//case 126/127: 0
