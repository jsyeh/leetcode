class MyCalendar {
    ArrayList<int[]> cal = new ArrayList<int[]>();
    public MyCalendar() {
        
    }
    
    public boolean book(int start, int end) {
        for(int i=0; i<cal.size(); i++) {
            int [] t = cal.get(i);
            if( ! (t[1] <= start || end <= t[0]) ){
                return false;
            }
        }

        int [] now = {start, end};
        cal.add(now);
        return true;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */
