class BrowserHistory {
    int historyN=0, nowN=0;
    ArrayList<String> history;
    public BrowserHistory(String homepage) {
        history = new ArrayList<String>();
        history.add(homepage);
        historyN = history.size();
        nowN = 0;
    }
    
    public void visit(String url) {
        nowN++;
        if(nowN>=historyN){
            history.add(url);
            historyN = history.size();
        }else{ //往右，是新的開始
            for(int i=historyN-1; i>=nowN; i--){
                history.remove(i);//要把後面的歷史刪掉
            }
            history.add(url);
            historyN = history.size();
        }
    }
    
    public String back(int steps) {
        if(steps > nowN) steps = nowN;
        nowN -= steps;
        return history.get(nowN);
    }
    
    public String forward(int steps) {
        if(nowN + steps > historyN - 1) steps = historyN  - 1 - nowN;
        nowN += steps;
        return history.get(nowN);
    }
}
//Case 2: ["BrowserHistory","visit","visit","back","visit","forward","visit","visit","forward","visit","back","visit","visit","forward"]
//[["esgriv.com"],["cgrt.com"],["tip.com"],[9],["kttzxgh.com"],[7],["crqje.com"],["iybch.com"],[5],["uun.com"],[10],["hci.com"],["whula.com"],[10]]

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */
