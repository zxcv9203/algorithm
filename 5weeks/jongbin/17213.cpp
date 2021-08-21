#include <bits/stdc++.h>

using namespace std;


int main(){

    std::ios_base::sync_with_stdio(false);
    cin.tie(0);

    int num1, num2;
    int div = 1;

    cin >> num1;
    cin >> num2;

    if(num1 > num2){
        cout << 1 << "\n";
        return 0;
    }

    int res =(num2 - num1) + num1 - 1;
    int roop = num1 - 1;

    long long sum = 1;
    long long divide = 1;
    while( 0 < roop--){  
        sum *= res;
              // cout <<"res:" << res << "\n";  
        res = res-1;
        divide *= div;
                // cout << div << "\n";
        div = div+1;
    }
       
               

    cout << sum/divide << "\n";
    
    return 0;
}


