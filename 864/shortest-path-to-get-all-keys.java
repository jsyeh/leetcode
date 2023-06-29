class Solution {
  //參考 wangzi6157 在 Solutions 的答案，得到解題的靈感
  //有個 class 用來存 keyMask 及位置，方便BFS的Queue使用
  class State {
    int keyMask, i, j;
    State(int _keyMask, int _i, int _j) {
      keyMask = _keyMask;
      i = _i;
      j = _j;
    }
  }
  
  int genKeyBit(char c) {
    int n = c - 'a';
    if(c>='A' && c<='F') n = c - 'A';
    return 1<<n;
  }
  void printKey(int mask) {
    System.out.print(mask&0x01);
    System.out.print(mask&0x02);
    System.out.print(mask&0x04);
    System.out.print(mask&0x08);
    System.out.print(mask&0x10);
    System.out.println(mask&0x20);
  }

  public int shortestPathAllKeys(String[] grid) {
    Queue<State> queue = new LinkedList<>();
    HashSet<String> visited = new HashSet<>(); //走過的地方，還要與key有關
    //所以使用String字串來存 State 的3個參數：keyMask, i, j 位置

    int M = grid.length, N = grid[0].length(), keyN = 0;;
    State start;
    //前面的迴圈，先找到 '@' 開始的坐標，同時確認 key 到底有幾把，決定keyMask運作方法
    for(int i=0; i<M; i++) {
      for(int j=0; j<N; j++) {
        char c = grid[i].charAt(j);
        if(c == '@') { //開始的座標
          start = new State(0, i, j);
          queue.offer(start);
          visited.add(0 + " " + i + " " + j);
          //使用String字串來存 State 的3個參數：keyMask, i, j 位置
        } else if(c >= 'a' && c <= 'f') { //最多key只有6把，可能更少
          if(c-'a'>=keyN) keyN = c-'a'+1; //由最大的key知道有幾個key
        }
      }
    }
    int allKeyMask = (1<<keyN)-1; //補數的概念
    //ex. keyN為2時，allKeyMask是 3 (2進位的11)
    //ex. keyN為3時，allKeyMask是 7 (2進位的111)
    System.out.println(keyN);
    System.out.println(allKeyMask);

    //後面的迴圈，開始進行BFS。因visited被改過，（只要keyMask不同）有些坐標會重覆走到
    int [] di = {0, 1, 0, -1};
    int [] dj = {1, 0, -1, 0};
    int ans = 0; //shortest steps
    while(queue.size()>0) {
      int size = queue.size(); //這一輪的queue有多少個
      while(size-- > 0) { //這一輪要把 (同steps) 的 queue 全部用完
        State now = queue.poll(); //取出存好的state
        if(now.keyMask == allKeyMask) { //如果收集到全部的key
          return ans; 
        }

        for(int dir=0; dir<4; dir++){
          int i = now.i + di[dir];
          int j = now.j + dj[dir];
          int keyMask = now.keyMask; //很多新鮮的 keyMask 後面遇到key時會改
          if(i>=0 && i<M && j>=0 && j<N) { //合理的下一步
            char c = grid[i].charAt(j);
            if(c == '#') {
              continue; //遇到牆，不做事, 直接避開這一格
            } else if(c >= 'a' && c<='f') { //小寫是key
              keyMask |= genKeyBit(c);//1<<(c-'a'); //找到某個key就記起來
//printKey(keyMask);
            } else if(c>='A' && c<='F') { //大寫是鎖
//System.out.println("遇到"+c+" 對應的key bit:" + genKeyBit(c));
//printKey(keyMask);
//System.out.println("keyMask & genKeyBit(c) 會得到" + (keyMask & genKeyBit(c)));
              if((keyMask & genKeyBit(c))==0) { //binary bit AND
//System.out.println("被鎖卡住了");
                continue; //keyMask不存在需要的key
              } 
              //如果這個鎖無法解開，就像牆一樣，直接避開這一格
            }
            if(!visited.contains(keyMask + " " + i + " " + j)) {
              visited.add(keyMask + " " + i + " " + j);
              queue.offer(new State(keyMask, i, j));
            }
          }
        }
      }
      ans++; //這輪走完，就要再多走一步囉
    }
    return -1; //沒有收集齊全部的key,就-1
  }
}
