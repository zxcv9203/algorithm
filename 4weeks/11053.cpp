#include <bits/stdc++.h>

using namespace std;
vector <int> arr;
vector <int> dp;


// 이전에 나온 숫자들 중에서, 현재 값인 '3'보다 작은 값 중에서 
// 가지고 있는 부분 수열의 길이 중 가장 긴 부분 수열의 길이에 +1을 한 값이 
// 현재 값에서 발생 할 수 있는 가장 긴 증가하는 부분 수열의 길이가 된다.


//dp배열 최대값 리턴
int the_longest_one_ever(int index, int now_index_value)
{
    int dp_max = 0;
    for(int i = 0;i<index;i++)
    {   
        if(now_index_value > arr[i] && dp_max < dp[i])
        {
            dp_max = (max(dp_max, dp[i]));
        }
    }
    return (dp_max);
}
int main(void)
{   
    int n;
    scanf("%d", &n);
    dp.resize(n+1);
   
    for(int i=0; i<n;i++)
    {
        int temp;
        scanf("%d", &temp);
        arr.push_back(temp);
    }
   
    for(int i = 0;i<n;i++)
    {
        
        dp[i] = the_longest_one_ever(i, arr[i]) + 1;
        
    }
    int max=0;
    for(int i = 0; i<n;i++)
    {
      
        if (dp[i] > max)
            max = dp[i];
    }
    printf("%d", max);
}
