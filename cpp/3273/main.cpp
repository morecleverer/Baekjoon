#include <iostream>

int main(){

    int num[2000001] = {};

    int n,x,res=0;

    std::cin >> n;
    int k[n];

    for(int i=0; i<n; i++){
        std::cin >> k[i];
    }

    std::cin >> x;

    for(int i=0; i<n; i++){
        if(k[i] >= x)
            continue;
        if(num[x-k[i]] > 0)
            res++;
        num[k[i]] += 1;
    }

    std::cout << res;

}