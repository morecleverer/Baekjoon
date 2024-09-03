#include <iostream>
#include <string>

int main(){

    int alpha[26] = {};
    int res=0;
    std::string str1, str2;

    std::cin >> str1 >> str2;

    for(int j=0; j<str1.length(); j++){
        alpha[str1[j]-97] += 1;
    }
    
    for(int j=0; j<str2.length(); j++){
        alpha[str2[j]-97] -= 1;
    }

    for(int i=0; i<26; i++){
        if(alpha[i]<0)
            res -= alpha[i];
        else   
            res += alpha[i];
    }

    std::cout << res;

}