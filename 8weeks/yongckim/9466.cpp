#include <cstdio>
#include <iostream>
#include <string.h>

using namespace std;

const int M = 1e5 + 1;
int t;
int n;
int student[M];
bool visit[M];
bool circle[M];
int cnt;
int idx;

void init()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
}

void dfs(int idx)
{
	int next = student[idx];
	visit[idx] = true;
	if (!visit[next])
	{
		dfs(next);
	}
	else {
		if (!circle[next])
		{
			for (int i = next; i != idx; i = student[i])
				cnt++;
			cnt++;
		}
	}
	circle[idx] = true;

}

int main(void)
{
	init();
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cin >> n;
		memset(circle, false, sizeof(circle));
		memset(visit, false, sizeof(visit));
		memset(student, 0, sizeof(student));
		cnt = 0;
		for (int j = 1; j <= n; j++)
			cin >> student[j];
		for (int j = 1; j <= n; j++)
		{
			if (!visit[j])
				dfs(j);
		}
		cout << n - cnt << '\n';
	}
}