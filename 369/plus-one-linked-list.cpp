/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* plusOne(ListNode* head) {
//        if(head->val==0){ //先解決 leading zero 的問題, 剛好是0
//            head->val = 1;
//            return head;
//        }

        //我想到一種解法,是把LinkedList倒過來, 加1後, 再倒過來
        //不過Eiditorial 介紹另一種作法: 先建前一項,然後找NonNine,最後存最後tail

        ListNode * ans = new ListNode(0, head);
        ListNode * next = head;
        ListNode * nonNine = ans;
        while(next!=nullptr) {
            if(next->val != 9) nonNine = next; //會找到最後一個不是9的數字,以便+1
            next = next->next;
        }
        
        nonNine->val++; //最後一個不是9的數字,以便+1
        nonNine = nonNine->next; //後面的9,一律都變成0
        while(nonNine!=nullptr){
            nonNine->val = 0;
            nonNine = nonNine->next;
        }
        if(ans->val==0) return ans->next;//沒有進位的話,就不要用這一位假的
        else return ans;

    }
};

/* test cases
[1,2,3]
[0]
[1,9,9,9]
[9,9,9,9,9]
[1,9,9,1,9]
[1,9,9,1]
*/
