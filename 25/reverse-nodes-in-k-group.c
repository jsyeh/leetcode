/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseKGroup(struct ListNode* head, int k){
    struct ListNode ans;
    ans.next = head;

    struct ListNode * p1 = &ans;
    struct ListNode * p2 = p1;

    while(true){
        for(int i=0; i<k; i++){
            if(p2==NULL) return ans.next;
            p2 = p2->next;
        }
        //數一數,確定有k個, 便能 reverse
        if(p2==NULL) return ans.next;
        
        struct ListNode * p3 = p2->next;//完成反向的部分
        struct ListNode * p4 = p2->next;//最後收尾
        p2 = p1->next;
        for(int i=0; i<k; i++){
            p1->next = p2->next;//未來要處理的那個
            p2->next = p3;
            p3 = p2;
            p2 = p1->next;
        }
        p1->next = p3;//要接上去
        for(int i=0; i<k; i++){
            p1 = p1->next;
        }
        p2 = p1;
    }

    return ans.next;
}
