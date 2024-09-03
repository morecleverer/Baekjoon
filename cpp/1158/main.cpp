#include <iostream>

struct Node{
    int value;
    Node* next;

};

class list{
    private:
        Node* head;
        Node* cursor;
        int length;

    public:

        list(): head(new Node{-1,nullptr}), cursor(head), length(0) {}
        ~list(){}

        void addNode(int v){
            if(length == 0){
                head->next = new Node{v, head->next};
                cursor = head->next;
                length++;
            }
            else{
                cursor->next = new Node{v, head->next};
                cursor = cursor->next;
                length++;
            }
        }
        void deleteNode(int a){
            cursor = head;
            std::cout << '<';
            while(length>0){
                for(int i=0; i<a-1;i++){
                    cursor = cursor->next;
                }
                int k = cursor->next->value;
                cursor->next = cursor->next->next;
                std::cout << k;
                length--;
                if(length != 0){
                    std::cout << ", ";
                }
            }
            std::cout << '>';
        }

};

int main(){

    list a;

    int n,k;

    std::cin >> n >> k;


    for(int i=1; i<=n; i++){
        a.addNode(i);
    }

    a.deleteNode(k);

    return 0;
}