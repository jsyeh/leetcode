/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    ListNode head;
    ArrayList<Integer> array = new ArrayList<Integer>();
    public Solution(ListNode _head) {
        head = _head;
        ListNode now = head;
        while(now!=null){
            array.add(now.val);
            now = now.next;
        }
    }
    
    public int getRandom() {
        int I = (int) (Math.random()*array.size());
        return array.get(I);
        /*
        //這個水庫法，有人在解答中寫它。但是會超時。
        //所以還是用轉成Array試試吧
        ListNode temp = head;
        int N = 1;
        int ans = temp.val;
        while(temp!=null){
            int R = (int)(Math.random()*N);
            if(R==0) ans = temp.val;
            temp = temp.next;
            N++;
        }
        return ans;*/
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */
