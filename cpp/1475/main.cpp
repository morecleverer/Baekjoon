#include <iostream>
#include "string"

int main(){

    int num[9] = {};

    std::string n;

    std::cin >> n;

    for(int i=0; i< n.length(); i++){
        if(n[i] == '9')
            num[6] ++;
        else
            num[n[i]-48] ++;

        

    }

    num[6] = (num[6]/2) + (num[6]%2);

    int max = 0;

    for(int i=0; i<9; i++){

        if(num[i] > max){
            max = num[i];
        }

    }

    std::cout << max;
}


