#include <bits/stdc++.h>

using namespace std;

int N, K;
vector<pair<int, int> > game;
int visited[151];
int res = 0;

//17204 : 죽음의 게임

int main(void)
{
    scanf("%d %d", &N, &K);
    memset(visited, 0, sizeof(visited));
    game.resize(N+1);
    
    for(int i = 0;i<N;i++)
    {
        game[i].first = i;
        scanf("%d", &game[i].second);
    }

    stack<int> stack;
    stack.push(0);
    while(!stack.empty())
    {
        int top = stack.top();
        if (visited[top] == 1)
        {
            res = 0;
            break;
        }
        if (top == K)
        {
            break;
        }
        res++;
        visited[top] = 1;
        stack.pop();
        stack.push(game[top].second);
    }
    if (res == 0)
        printf("-1");
    else
        printf("%d", res);

}
