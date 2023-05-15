char * interpret(char * command){
    int N = 0;
    for(int i=0; command[i]!=0; i++){
        if(command[i]=='G'){ //很好,什麼事都不做
            command[N++] = 'G'; //把字母直接搬過來
        }else if(command[i]=='('){ //有兩種狀況
            if(command[i+1]==')'){ //簡單的 () 代表 o
                command[N++] = 'o';
                i++; //跳掉後面的 () 不過留一個給第3行的i++用
            }else{ //複雜的 (al)
                command[N++] = 'a';
                command[N++] = 'l';
                i+=3; //跳掉後面的 (al) 不過留一個給第3行的i++用
            }
        }
    }
    command[N] = 0; //字串結尾
    return command;
}
