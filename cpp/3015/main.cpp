#include <iostream>
#include <string>
#include <stack>
#include <algorithm>

int main(){
    std::ios_base::sync_with_stdio(false);
	std::cin.tie(0);
    int n;
    std::cin >> n;
    std::stack<std::pair<int,int > > stk;
    long long int res=0;

    for(int i=0; i<n; i++){

        int k;

        std::cin >> k;

        int same=0;


        while(!stk.empty()){
            if(stk.top().first < k){
                res += stk.top().second+1;
                stk.pop();
            }
            else if(stk.top().first == k){
                same = stk.top().second;
                stk.pop();
                same++;
            }
            else{
                res++;
                break;
            }
        }
        res += same;
        stk.push(std::make_pair(k,same));
        
        //std::cout << res << "\n \n";
    }

    std::cout << res;

    return 0;
}