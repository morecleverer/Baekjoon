#include <iostream>

int main(){

    int n, y=0, m=0;

    std::cin >> n;

    for(int i=0; i<n; i++){

        int t;

        std::cin >> t;

        y += 10 + (t/30)*10;
        m += 15 + (t/60)*15;


    }

    if(y>m){
        std::cout << "M " << m;
    }
    else if(y == m){
        std::cout << "Y M " << m;
    }
    else{
        std::cout << "Y " << y;
    }


}