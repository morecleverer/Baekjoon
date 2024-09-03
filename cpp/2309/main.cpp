#include <iostream>

int main(){

    int a[9];
    int sum=0;
    int isOk=0;

    for(int i=0; i< 9; i++){
        std::cin >> a[i];
        sum += a[i];
    }

    for(int i=0; i< 8; i++){
        for(int j=i+1; j<9; j++){
            if(sum - a[i] - a[j] == 100){
                a[i] = a[j] = 0;
                isOk = 1;
                break;
            }
        }
        if(isOk)
        break;
    }

    for(int i=0; i<9; i++){
        for(int j=0; j<8-i; j++){
            if(a[j] > a[j+1]){
                int k = a[j];
                a[j] = a[j+1];
                a[j+1] = k;
            }
        }
    }

    for(int i=2; i<9; i++){
        std::cout << a[i] << '\n';
    }



}