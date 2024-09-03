#include <iostream>
#include "string"

int main(){

    int alpha[26] = {0,};

    std::string str;

    std::cin >> str;

    for(int i=0; i<str.length(); i++){
        alpha[tolower(str[i]) - 97] += 1;
    }

    for(int i=0; i<26; i++){
        std::cout << alpha[i] << ' ';
    }



}