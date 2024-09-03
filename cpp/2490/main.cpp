#include <iostream>

int main(){

    for(int i=0; i<3;i++){

        int a,b,c,d;

        std::cin >> a >> b >> c >> d;

        switch(a+b+c+d){
            case 0:
            std::cout << "D\n";
            break;
            case 3:
            std::cout << "A\n";
            break;
            case 2:
            std::cout << "B\n";
            break;
            case 1:
            std::cout << "C\n";
            break;
            case 4:
            std::cout << "E\n";
            break;

        }

    }


    
    return 0;
}