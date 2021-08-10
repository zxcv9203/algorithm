#include <bits/stdc++.h>

using namespace std;

int line;
long long arr[501][501] = {0, };
long long dp[501][501] = {0, };

int main(void)
{
    scanf("%d", &line);
    for(int i = 0; i<line;i++)
    {
        for(int j = 0;j<i+1;j++)
        {
            scanf("%lld", &arr[i][j]);
        }
    }
    dp[0][0] = arr[0][0];

    for(int i = 1; i< line;i++)
    {
        for(int j = 0; j < i+1;j++)
        {
            if (j == 0)
            {
                dp[i][j] = arr[i][j] + dp[i-1][j];
            }
            else if (j == i-1)  //여기를 j == i-1로 해둬서 계속 틀림
            {
                dp[i][j] = arr[i][j] + dp[i-1][j-1];
            }
            else
            {
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + arr[i][j];
            }
        }
    }
    long long max = -1;
    for(int i = 0;i<line;i++)
    {
        if (max < dp[line-1][i])
            max = dp[line-1][i];
    }
    printf("%lld", max);
}
