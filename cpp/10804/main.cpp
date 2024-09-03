#include <iostream>

int main(){

    int card[20] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20};

    for(int i=0; i<10; i++){
        int a,b;

        std::cin >> a >> b;

        for(int j = 0; j<(b-a+1)/2; j++){

            int k=card[a-1+j];
            card[a-1+j] = card[b-1-j];
            card[b-1-j] = k;
            
        }
    }

    for(int i=0; i<20; i++){
        std::cout << card[i] << " ";
    }


}