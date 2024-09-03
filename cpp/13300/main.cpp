#include <iostream>

int main(){

    int school[2][6] = {{},{}};

    int n,k,res=0;

    std::cin >> n >> k;

    for(int i=0; i<n; i++){
        int grade, sex;

        std::cin >> sex >> grade;

        school[sex][grade-1] ++;
    }

    for(int i=0; i<2; i++){
        for(int j=0; j<6; j++){
            res += school[i][j]/k;

            if(school[i][j]%k>0)
                res++;
        }
    }

    std::cout << res;

}