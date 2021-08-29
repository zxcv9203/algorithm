#include <bits/stdc++.h>

using namespace std;

int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };

int num, wet, cnt, ans, mx;
int a[102][102];
int b[102][102];


void dfs(int x, int y) {
	b[x][y] = 0;
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
        int ny = y + dy[i];
		if (b[nx][ny] > wet) 
        dfs(nx, ny);
	}
}

int main() {
	cin >> num;
	for (int i = 1; i <= num; i++){
        for (int j = 1; j <= num; j++){
            cin >> a[i][j];
        }
    }
		

	for (int k = 0; k <= 100; k++) {
		memcpy(b, a, sizeof(a));
		for (int i = 1; i <= num; i++) {
			for (int j = 1; j <= num; j++) {
				if (b[i][j] > k) {
					wet = k;
                    cnt++;
					dfs(i, j);
				}
			}
		}
		ans = max(cnt, ans);
		cnt = 0;
	}

	cout << ans << "\n";

	return 0;
}