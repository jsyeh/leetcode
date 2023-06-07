int minFlips(int a, int b, int c){
    int ans = 0;
    for(int i=0; i<31; i++){
        int a2 = a%2, b2 = b%2, c2 = c%2;
        //printf("%d %d %d\n", a2, b2, c2);
        if((a2|b2)==c2){

        }else if((a2|b2)==1 && c2==0){
            if(a2==1) ans++;
            if(b2==1) ans++;
        }else if((a2|b2)==0 && c2==1){
            ans++;
        }

        a /= 2;
        b /= 2;
        c /= 2;
    }
    return ans;
}
