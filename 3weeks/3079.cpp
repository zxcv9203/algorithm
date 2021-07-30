#include <iostream>
// #include <stack>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <stdio.h>
#include <queue>


using namespace std;

vector<long long> air;
long long N, M, answer;

int main(void)
{
    scanf("%lld %lld", &N, &M);
    long long max2 = -1;
    for(int i = 0; i<N;i++)
    {
        int temp;
        scanf("%d", &temp);
        if (max2 < temp)
            max2 = temp;
        // printf("temp = %lld\n", max2);
        air.push_back(temp);
    }
    // printf("temp = %lld", max2);
    long min=0, max = answer = max2 * M;
    while (min < max)
    {
        long long mid = (min + max) /2;
        long long sum = 0;
        for(int i = 0;i < N;i++)
        {
            sum += mid / air[i];
        }
        if (sum < M)
            min = mid + 1;
        else
        {
            if (answer > mid)
                answer = mid;
            max = mid;
        }
    }
    printf("%lld",answer);
}
