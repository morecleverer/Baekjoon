#include <iostream>
#include <string>
#include <stack>
#include <algorithm>

int main(){

    std::ios_base::sync_with_stdio(false);
	std::cin.tie(0);
    int n;
    std::stack<std::pair<int, int> > stk;
    std::cin >> n;

    
    for(int i=0; i<n; i++){
        int a;

        std::cin >> a;


        while(!stk.empty()){

            if(stk.top().first > a){
                std::cout << stk.top().second+1 << ' ';
                break;
            }
            stk.pop();
            
        }

        if(stk.empty()){
            std::cout << 0 << ' ';
        }
        stk.push(std::make_pair(a,i));

    }

}