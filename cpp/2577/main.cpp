#include <iostream>
#include "string"

int main(){


    int a,b,c;
    int num[10] = {};

    std::cin >> a >> b >> c;

    std::string res = std::to_string(a*b*c);


    for(int i=0; i<res.length(); i++){
        num[res[i]-48] += 1;
    }

    for(int i=0; i<10; i++){
        std::cout << num[i] << '\n';
    }



}