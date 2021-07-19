#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

long long already_have, need, res;
long long p[1000001];
int k = 0;


long long binary()
{
    long long low = 1, hi = p[already_have-1];
    while(low <= hi)
    {
        long long mid = (low + hi)/2;
        int temp = 0;
        for(int i = 0; i<already_have;i++)
        {
            temp += (p[i]/mid);
        }
        if (temp < need)
            hi = mid - 1;
        else
            low = mid + 1;
    }
    return hi;
}

int main(void)
{
    scanf("%lld %lld", &already_have, &need);

    for(int i = 0; i < already_have;i++)
    {
        long long a = 10;
        scanf("%lld", &a);
        p[i] = a;
    }
    sort(p, p + already_have);
    printf("%lld\n",binary());
}
