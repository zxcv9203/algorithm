#include <bits/stdc++.h>

using namespace std;
long dp[117] = {0, };


long find_answer(int index)
{
    if (index <= 3)
        return 1;
    if (dp[index] != 0)
        return (dp[index]);
    if (index -1 >= 3&& dp[index-1] == 0)
        dp[index-1] = find_answer(index-1);
    if (index -3 >= 3 && dp[index-3] == 0)
        dp[index-3] = find_answer(index-3);
    dp[index] = find_answer(index-1) + find_answer(index-3);
    return dp[index];
}

int main(void)
{
    int index;
    scanf("%d", &index);
    printf("%ld",find_answer(index));
}