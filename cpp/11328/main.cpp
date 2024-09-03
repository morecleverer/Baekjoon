#include <iostream>
#include <string>

int main(){

    int n;

    std::cin >> n;

    for(int i=0; i<n; i++){


        std::string str1, str2;

        int num[26] = {};
        bool isOk = true;

        std::cin >> str1 >> str2;

        for(int j=0; j<str1.length(); j++){
            num[str1[j]-97] += 1;
        }

        for(int j=0; j<str2.length(); j++){
            num[str2[j]-97] -= 1;
        }

        for(int j=0; j<26; j++){
            if(num[j]>0 || num[j] <0){
                isOk = false;
                break;
            }
        }





        if(isOk)
        std::cout << "Possible" << '\n';
        else
        std::cout << "Impossible" << '\n';




    }

}