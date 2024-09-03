#include <iostream>

int main(){

    int a,min,s=0, isodd = 0;

    for(int i=0; i<7; i++){
        std::cin >> a;

        if(a%2 != 0){
            s += a;


            if(isodd==0){
                min = a;
                isodd = 1;
            }

            else{
                if(min > a){
                    min = a;
                }

            }

        }
        

    }

    if(s == 0){
        std::cout << -1;
    }
    else{
        std::cout << s << '\n' << min;
    }

}