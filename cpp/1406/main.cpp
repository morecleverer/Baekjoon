#include <iostream>
#include <string>
#include <list>

int main(){

    std::string str;

    std::cin >> str;

    std::list<char> l_list;

    for(char i : str){
        l_list.push_back(i);
    }

    std::list<char>::iterator t = l_list.end();

    int m;

    std::cin >> m;

    for(int i=0; i<m; i++){
        char ctrl;

        std::cin >> ctrl;

        switch(ctrl){
            case 'L':
                if(t != l_list.begin()){
                    t--;
                }
            break;
            case 'D':
                if(t != l_list.end()){
                    t++;
                }
            break;
            case 'B':
                if(t != l_list.begin()){
                    t--;
                    t = l_list.erase(t);
                }
            break;
            case 'P':
                char x;
                std::cin >> x;

                l_list.insert(t,x);
            break;
        }

    }

    for(char i : l_list){
        std::cout << i;
    }


}