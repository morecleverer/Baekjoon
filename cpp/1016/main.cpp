#include <iostream>
#include <stack>
#include <algorithm>
#include <math.h>

int main(){

    long long min,max;

    std::cin >> min >> max;

    long long sq_max = (long long) (sqrt(double(max))) < 2 ? 2 : (long long) (sqrt(double(max)));




    long long k = max - min + 1;
    long long r = sq_max + 1;

    long long res_list[k];
    long long sq_list[r];
    std::fill_n(res_list,k, 1);
    std::fill_n(sq_list,sq_max+1, 1);

    

    for (long long i = 2; i <= sqrt(sq_max); i++){
		if (sq_list[i] == 1){
			for (long long j = i + i; j <= sq_max; j += i){
				sq_list[j] = 0;
			}
		}
	}

    


    for(long long i=2; i<= sq_max; i++){
        
        if(sq_list[i] == 0)
            continue;

        long long a;

        if(min%(i*i) == 0){
            a = 0;
        }
        else{
            a = (min/(i*i)+1) * (i*i) - min;
        }

        while(a < k){
            if(res_list[a] = 0){
                continue;
            }
            res_list[a] = 0;

            a += i*i;
        }

    }



    long long res=0;
    
    for(long long i : res_list){
        res += i;
    }

    std::cout << res;


}