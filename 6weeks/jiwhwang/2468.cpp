#include <bits/stdc++.h>

using namespace std;
int N;
int region[101][101];
bool safe_zone[101][101];
bool visit[101][101];
int max_lump = 0;
vector<int> v;

//왼, 오, 위, 아래
int xx[4] = {-1, 1, 0, 0};
int yy[4] = {0, 0, 1, -1};


//2468 안전영역
queue<pair<int, int> > q;
void BFS(int x, int y)
{
    visit[x][y] = true;
    q.push(make_pair(x,y));

    while(!q.empty())
    {
        x = q.front().first;
        y = q.front().second;
        q.pop();

        for(int i = 0; i<4;i++)
        {
            int nx = x + xx[i];
            int ny = y + yy[i];

            if (nx < 0 || nx >= N || ny < 0 || ny >= N)
                continue;
            if (safe_zone[nx][ny] && !visit[nx][ny])
            {
                visit[nx][ny] = true;
                q.push(make_pair(nx, ny));
            }

        }
    }
}

// void show_safe()
// {
//     for(int i=0; i<N;i++)
//     {
//         for(int j=0;j<N;j++)
//         {
//             if (!safe_zone[i][j])
//                 printf("%c ", 'X');
//             else
//                 printf("%c ", 'O');
//         }
//         printf("\n");
//     }
// }


void reset()
{
    for(int i = 0;i<101;i++)
    {
        for(int j = 0; j<101;j++)
        {
            safe_zone[i][j] = false;
            visit[i][j] = false;
        }
    }
    max_lump = 0;
}

int main(void)
{
    memset(region, 0, sizeof(region));
    reset();

    scanf("%d", &N);
    int max_height = -1;
    for(int i = 0; i<N;i++)
    {
        for(int j = 0; j<N;j++)
        {
            scanf("%d", &region[i][j]);
            if (max_height < region[i][j])
                max_height = region[i][j];
        }
    }
    // printf("max_height = %d\n", max_height);
    for(int h = 1;h<=max_height;h++)
    {
        // h이하 물에 잠김 
        for(int a = 0; a<N; a++)
        {
            for(int b=0; b<N; b++)
            {
                if (region[a][b] >= h)
                    safe_zone[a][b] = true;
                else
                    safe_zone[a][b] = false;
            }
        }
        // show_safe();
        // BFS 영역 개수 구하기
        for(int i=0; i<N;i++)
        {
            for (int j=0; j<N;j++)
            {
                if (safe_zone[i][j] && visit[i][j] == 0)
                {
                    BFS(i, j);
                    max_lump++;
                }
            }
        }
        // printf("i = %d, res = %d\n\n\n", h, max_lump);
        v.push_back(max_lump);
        reset();
    }
    sort(v.begin(), v.end());
    printf("%d", v[v.size()-1]);
}
