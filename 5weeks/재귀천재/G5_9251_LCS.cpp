#include <bits/stdc++.h>

using namespace std;

char arr1[1001] = {0,};
char arr2[1001] = {0,};
long lcs[1001][1001] = {0,};

void longest(int end1, int end2)
{
    for(int i=1; i<=end1; i++)
    {
        for(int j=1; j<=end2; j++)
        {
            if (arr1[i-1] == arr2[j-1])
            {
                lcs[i][j] = lcs[i-1][j-1]+1;
            }
            else
            {
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1]);
            }
        }
    }
}

int main(void)
{
    scanf("%s\n%s", arr1, arr2);
    
    int end1, end2;
    for(int i = 0; i<1001;i++)
    {
        if (arr1[i] == 0)
        {
            end1 = i;
            break;
        }
    }
    for(int i = 0; i<1001;i++)
    {
        if (arr2[i] == 0)
        {
            end2 = i;
            break;
        }
    }

    longest(end1, end2);
    printf("%ld", lcs[end1][end2]);
}

// http://melonicedlatte.com/algorithm/2018/03/15/181550.html