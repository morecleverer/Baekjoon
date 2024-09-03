#include <iostream>

int main(){

    int a[3];

    std::cin >> a[0] >> a[1] >> a[2];

    for(int i=0; i<2; i++){

        if(a[i] > a[i+1]){
            int k= a[i];
            a[i] = a[i+1];
            a[i+1] = k;
        }

    }
    if(a[0] > a[1]){
            int k= a[0];
            a[0] = a[1];
            a[1] = k;
        }
    
    std::cout << a[0] << ' ' << a[1] << ' ' << a[2];
    
}