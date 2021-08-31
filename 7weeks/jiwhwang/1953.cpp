#include <bits/stdc++.h>

using namespace std;

int N;
bool connect[101][101];
bool visit[101];
int color_map[101]; // blue = 1, white = 0, else = -1;

vector<int > blue;
vector<int> white;

void BFS(int x)
{
    queue <int> q;
    q.push(x);
    while(!q.empty())
    {
        int first = q.front();
        visit[first] = true;
        q.pop();
        bool is_connect = false;    // 아무것도 연결이 안된경우

        for(int i=1; i<=N; i++)
        {
            if (connect[first][i] && !visit[i])
            {
                q.push(i);
                visit[i] = true;
                if (color_map[first] == -1)
                {
                    color_map[first] = 1;
                    blue.push_back(first);
                    is_connect = true;
                }
                if (color_map[first] == 1)
                {
                    white.push_back(i);
                    color_map[i] = 0;
                    is_connect = true;
                }
                else if (color_map[first] == 0)
                {    
                    color_map[i] = 1;
                    blue.push_back(i);
                    is_connect = true;
                } 
            }
           
        }
        if (color_map[first] == -1)
        {
            color_map[first] = 1;
            blue.push_back(first);
        }
    }
}

void isConcentrated()
{
    if (blue.size() == N)
    {
        int temp = blue[blue.size()-1];
        blue.pop_back();
        white.push_back(temp);
    }
    else if (white.size() == N)
    {
        int temp = white[white.size()-1];
        white.pop_back();
        blue.push_back(temp);
    }
}

int main()
{
    //  N은 학생수 
    scanf("%d", &N);

    memset(visit, false, sizeof(visit));
    memset(connect, false, sizeof(connect));
    memset(color_map, -1, sizeof(color_map));

    //  input
    for(int i=1; i<=N; i++)
    {
        int a;
        scanf("%d", &a);
        for(int j=0; j<a; j++)
        {
            int b;
            scanf("%d", &b);
            connect[i][b] = true;
            connect[b][i] = true;
        }
    }

    for(int i=1; i<=N; i++)
    {
        if(color_map[i] == -1)
        {
            BFS(i);
        }
    }

    isConcentrated();
    sort(blue.begin(), blue.end());
    sort(white.begin(), white.end());
    printf("%lu\n", blue.size());
    for(int i = 0; i<blue.size();i++)
    {
        printf("%d ", blue[i]);
    }
    printf("\n%lu\n", white.size());
    for(int i = 0; i<white.size();i++)
    {
        printf("%d ", white[i]);
    }


}   // 두 집합에 하나는 무조건 있어야함
