// LeetCode 445. Add Two Numbers II
class Solution {
public:
    // 今天的 week14-2.cpp 就是以下的幾行
    ListNode* myReverse(ListNode* head) {
        // 忘了寫「函式呼叫函式」的終止條件
        if (head==nullptr || head->next==nullptr) return head;
        
        ListNode* ans = myReverse(head->next);
        head->next->next = head;
        head->next = nullptr;
        return ans; 
    }
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* list1 = myReverse(l1); // 反過來
        ListNode* list2 = myReverse(l2); // 反過來

        return myReverse( myAddTwoNumbers(list1, list2) );
    }
    ListNode* myAddTwoNumbers(ListNode* list1, ListNode* list2) {
        ListNode* ans = new ListNode(999);
        ListNode* ans2 = ans; // 幫忙把 ans 的尾巴「收尾」收好
        int carry = 0; // 進位
        while (list1 != nullptr || list2 != nullptr) {
            int now = carry;
            if (list1 != nullptr) {
                now += list1->val; // 加上 list1 的值
                list1 = list1->next; // 換下一筆待命
            }
            if (list2 != nullptr) {
                now += list2->val;
                list2 = list2->next;
            }
            ans2->next = new ListNode( now%10 ); // 個位數的部分, 塞進去
            ans2 = ans2->next;  // 換下一筆待命
            carry = now / 10; // 進位的部分
        }
        if (carry>0) ans2->next = new ListNode(carry); // 最高位的進位

        return ans->next;
    }
};
