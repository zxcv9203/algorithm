#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <math.h>

using namespace std;

const int M = 21;

int n;
int ans;

void init()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
}

int move_down(int copy[M][M])
{
	int ret;

	ret = 0;
	for (int j = 0; j < n; j++)
	{
		int idx;
		int value;

		idx = n;
		value = -1;
		for (int i = n - 1; i >= 0; i--)
		{
			if (copy[i][j] == 0)
				continue ;
			if (copy[i][j] == value)
			{
				copy[idx][j] = copy[idx][j] * 2;
				value = -1;
			}
			else
			{
				value = copy[i][j];
				idx--;
				copy[idx][j] = copy[i][j];
			}
			ret = max(ret, copy[idx][j]);
		}
		for (int i = idx - 1; i >= 0; i--)
			copy[i][j] = 0;
	}
	return ret;
}

int move_up(int copy[M][M])
{
	int ret;

	ret = 0;
	for (int j = 0; j < n; j++)
	{
		int idx;
		int value;

		idx = -1;
		value = -1;
		for (int i = 0; i < n; i++)
		{
			if (copy[i][j] == 0)
				continue ;
			if (copy[i][j] == value)
			{
				copy[idx][j] = copy[idx][j] * 2;
				value = -1;
			}
			else
			{
				value = copy[i][j];
				idx++;
				copy[idx][j] = copy[i][j];
			}
			ret = max(ret, copy[idx][j]);
		}
		for (int i = idx + 1; i < n; i++)
			copy[i][j] = 0;
	}
	return ret;
}

int move_right(int copy[M][M])
{
	int ret;
	
	ret = 0;
	for (int i = 0; i < n; i++)
	{
		int idx;
		int value;

		idx = n;
		value = -1;
		for (int j = n - 1; j >= 0; j--)
		{
			if (copy[i][j] == 0)
				continue;
			if (copy[i][j] == value)
			{
				copy[i][idx] = copy[i][idx] * 2;
				value = -1;
			}
			else
			{
				value = copy[i][j];
				idx--;
				copy[i][idx] = copy[i][j];
			}
			ret = max(ret, copy[i][idx]);
		}
		for (int j = idx - 1; j >= 0; j--)
			copy[i][j] = 0;
	}
	return ret;
}

int move_left(int copy[M][M])
{
	int ret;

	ret = 0;
	for (int i = 0; i < n; i++)
	{
		int idx;
		int value;

		idx = -1;
		value = -1;
		for (int j = 0; j < n; j++)
		{
			if (copy[i][j] == 0)
				continue;
			if (copy[i][j] == value)
			{
				copy[i][idx] = copy[i][idx] * 2;
				value = -1;
			}
			else
			{
				value = copy[i][j];
				idx++;
				copy[i][idx] = copy[i][j];
			}
			ret = max(ret, copy[i][idx]);
		}
		for (int j = idx + 1; j < n; j++)
			copy[i][j] = 0;
	}
	return ret;
}

void board_copy(int copy[M][M], int board[M][M])
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			copy[i][j] = board[i][j];
		}
	}
}

void dfs(int move, int board[M][M], int value)
{
	if (!move)
	{
		ans = max(ans, value);
		return;
	}
	for (int i = 0; i < 4; i++)
	{
		int copy[M][M];
		int ret;

		board_copy(copy, board);
		if (i == 0)
			ret = move_up(copy);
		else if (i == 1) 
			ret = move_down(copy);
		else if (i == 2)
			ret = move_left(copy);
		else if (i == 3)
			ret = move_right(copy);
		dfs(move - 1, copy, ret);
	}
}

int main(void)
{
	init();
	int board[M][M];
	
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
			cin >> board[i][j];
	}
	dfs(5, board, ans);
	cout << ans << '\n';
}