#include <iostream>

int main(){

    unsigned long long a,b;

    std::cin >> a >> b;

    if(a>b){
        unsigned long long  k=a;
        a=b;
        b=k;
    }
    if(a==b){
        std::cout << 0;
        return 0;
    }

    std::cout << b-a-1 << '\n';
    

    for(unsigned long long i = a+1; i<b; i++){
        std::cout << i << ' ';
    }


}