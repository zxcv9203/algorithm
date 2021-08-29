#include <bits/stdc++.h>

using namespace std;

int n,m;
int arr[8][8];
int temp[8][8];
int dx[] = { 0,0,1,-1 };
int dy[] = { 1,-1,0,0 };

int res;

void dfss(int x, int y) {
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
            if (temp[nx][ny] == 0) {
                temp[nx][ny] = 2;
                dfss(nx, ny);
            }
        }
    }
}

int cnt_safe() {
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (temp[i][j] == 0) {
                cnt += 1;
            }
        }
    }
    return cnt;
}


void dfs(int count) {

    if (count == 3) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                temp[i][j] = arr[i][j];
            }
        }
    
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (temp[i][j] == 2) {
                    dfss(i, j);
                }
            }
        }

        res = max(res, cnt_safe());
        return;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (arr[i][j] == 0) {
                arr[i][j] = 1;
                count += 1;
                dfs(count);
                arr[i][j] = 0;
                count -= 1;
            }
        }
    }
}

int main(void) {
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
        }
    }

    dfs(0);
    cout << res << '\n';
}
