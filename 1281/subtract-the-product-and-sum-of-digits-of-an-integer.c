int subtractProductAndSum(int n){
    int product=1, sum=0;
    while(n>0){
        product *= n%10;
        sum += n%10;
        n = n / 10;
    }
    return product - sum;
}
//case 77/123: 114
//1+1+4 = 6
//1*1*4 = 4
