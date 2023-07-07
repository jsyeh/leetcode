//這個題目與昨天2023-07-06 的題目很像，可以用相同的解法
//有個會移動的框框（右邊界右移），如果找到最大值combo時，框框會變大（像貪食蛇，left會留原地）
//吃到錯的答案時，會把功德值k變小
//如果功德值變負的時，無法combo，左邊界會右移，並看吐出來的值，能不能讓k恢復為0或正的
//不過這題有個不同的地方：連續T 或連續F 都可以。這題就做2次就好了
int maxConsecutiveAnswers(char * answerKey, int k){
    int N = strlen(answerKey);
    int left = 0, right = 0, kd = k; //kd:功德值
    for(int i=0; i<N; i++){
        if(answerKey[i]=='T' && kd>=0){ //很好，連續T
            right++;
        }else{ //不好，沒有連續T,要耗掉1點功德值
            if(answerKey[i]!='T') kd--; //耗掉1點功德值
            if(kd<0){ //不幸的，累積的功德值不足，只好移動右邊界(整個平移)，吐出舊的值
                if(answerKey[left]!='T') kd++;//很好，吐掉壞東西，功德值回升
                left++;
            }
            right++;
        }
    }
    int ans = right-left;
//printf("ans1:%d\n", ans);
    //上面測「連續T」，下面測「連續F」。
    //之後可改成「用函式來實作」 maxContinueAnswer(char* answerKey, int k , char key)
    //然後呼叫 maxContinueAnswer(answerKey, k, 'T') 及 maxContinueAnswer(answerKey, k, 'F') 便可得到最好的答案
    left = 0;
    right = 0;
    kd = k;
    for(int i=0; i<N; i++){
        if(answerKey[i]=='F' && kd>=0){ //現在改測「連續F」
            right++; //有人會想要把 right++ 移到外面，不過我刻意放裡面，方便理解在做的事
        }else{ //不好，沒有連續'F'
            if(answerKey[i]!='F') kd--; //耗掉1點功德值
            if(kd<0){ //不幸的，累積的功德值不足
                if(answerKey[left]!='F') kd++; //功德值回升
                left++; //吐掉後，左界右移
            }
            right++;
        }
    }
//printf("ans2:%d\n", right-left);
    if(right-left>ans) ans = right-left;
    return ans;
}
//case 45/93: "FTFFTFTFTTFTTFTTFFTTFFTTTTTFTTTFTFFTTFFFFFTTTTFTTTTTTTTTFTTFFTTFTFFTTTFFFFFTTTFFTTTTFTFTFFTTFTTTTTTF"
//32
