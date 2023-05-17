/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
//    void print(Node* head) {
//        while(head!=nullptr) {
//            printf("%d ", head->val);
//            head = head->next;
//        }
//        printf("\n");
//    }
    Node* copyRandomList(Node* head) {
        unordered_map<Node*,Node*> map;
        Node* temp = head;
        Node ans(0);
        Node* temp2 = &ans;
        while(temp!=nullptr) {
            temp2->next = new Node(temp->val);
            temp2 = temp2->next;
            if(temp!=nullptr) {
                pair<Node*,Node*> p(temp,temp2);
                map.insert(p);
            }
            temp = temp->next;
        }
        temp = head;
        temp2 = ans.next;
        while(temp!=nullptr){
            printf("%d %d\n", temp->val, temp2->val);
            if(temp->random!=nullptr){
               temp2->random = map.find(temp->random)->second;
            }
            temp = temp->next;
            temp2 = temp2->next;
        }

        return ans.next;
    }
};
