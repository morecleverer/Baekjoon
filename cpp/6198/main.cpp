#include <iostream>
#include <string>
#include <stack>
#include <algorithm>
#include <string>

int main(){

    std::ios_base::sync_with_stdio(false);
	std::cin.tie(0);
    int n;
    long long int res=0;
    std::cin >> n;
    std::stack<std::pair<int,long long int> > stk;
    std::stack<int> input;

    for(int i=0; i<n; i++){
        int a;
        std::cin >> a;
        input.push(a);
    }


    
    for(int i=0; i<n; i++){

        int a;
        a = input.top();
        input.pop();

        long long int k=0;

        while(!stk.empty()){

            if(stk.top().first >= a){
                break;
            }
            k += stk.top().second+1;
            stk.pop();
            
        }
        stk.push(std::make_pair(a,k));
        res += k;

    }

    std::cout << res;
}