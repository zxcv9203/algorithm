#include <iostream>
#include <stack>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <stdio.h>


using namespace std;

//  바이러스
int num_of_computers, pairs;

vector< vector<int> > connect;
int result = 0;

int main(void)
{
    scanf("%d", &num_of_computers);
    scanf("%d", &pairs);

    vector<int> visited(num_of_computers + 1, 0);
    connect.resize(num_of_computers + 1);
    for(int i = 0; i < pairs; i++)
    {
        int one, two;
        scanf("%d %d", &one, &two);

        connect[one].push_back(two);
        connect[two].push_back(one);
    }
    stack<int> stack;
    stack.push(1);
    visited[1] = 1;
    int top;
    
    while(!stack.empty())
    {
    
        int top = stack.top(); stack.pop();
        visited[top] = 1;
        
        for(int i = 0; i < connect.at(top).size();i++)
        {
            int next = connect.at(top).at(i);
            if (visited.at(next) == 0)
            {
                stack.push(next);
                result++;
                visited.at(next) = 1;
            }
        }
    }
    printf("%d", result);
}
