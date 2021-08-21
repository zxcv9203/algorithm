#include <bits/stdc++.h>

using namespace std;

int main(){

     std::ios_base::sync_with_stdio(false);
    // cin.tie(0);
    //int dp[117] = {1,};
    long long dp[117];
    //fill_n(dp, 117, 1);

    int num;
    cin >> num;
    dp[0] = 0;
    dp[1] = dp[2] = dp[3] = 1;

    for(int i = 4; i <= num; i++){
        dp[i] = dp[i-1] + dp[i-3];
    }

    cout << dp[num];
    return 0;
}

