#include <iostream>
using namespace std;
int ans[7][3], t_ans[7][3], result = 8;
int arr[5][5], corr[5][5];

int cal() {
	int t = 0;
	for (int i = 1; i < 5; i++)
		for (int j = 0; j < 5; j++)
			if (arr[i][j] != corr[i][j])
				t++;
	return t;
}

void mv(int cnt) {
	if (t_ans[cnt][0] == 1) {		//오른쪽으로 이동
		int idx = t_ans[cnt][1];
		for (int t = 0; t < t_ans[cnt][2]; t++) {		//t칸 오른쪽으로 이동
			int temp = arr[idx][4];
			arr[idx][4] = arr[idx][3];
			arr[idx][3] = arr[idx][2];
			arr[idx][2] = arr[idx][1];
			arr[idx][1] = temp;
		}
	}
	else {			//밑으로 이동
		int idx = t_ans[cnt][1];
		for (int t = 0; t < t_ans[cnt][2]; t++) {		//t칸 밑으로 이동
			int temp = arr[4][idx];
			arr[4][idx] = arr[3][idx];
			arr[3][idx] = arr[2][idx];
			arr[2][idx] = arr[1][idx];
			arr[1][idx] = temp;
		}
	}
}

void dfs(int cnt) {
	int dismatch = cal();
	if (dismatch == 0) {		//안바꿔도 이미 정답인 경우
		result = cnt;
		for (int i = 0; i < cnt; i++) {
			ans[i][0] = t_ans[i][0];
			ans[i][1] = t_ans[i][1];
			ans[i][2] = t_ans[i][2];
		}
		return;
	}
	int maybe;
	if (dismatch % 4 == 0) maybe = dismatch / 4;
	else maybe = dismatch / 4 + 1;
	if (cnt + maybe >= result) return;		//적어도 저만큼 돌려야하는데 이미 구한값이 저거보다 적은 경우
	for (int j = 1; j < 3; j++) {		//행or열
		for (int i = 1; i < 5; i++) {		//몇번째(1~4)
			for (int k = 1; k < 4; k++) {		//몇칸 이동
				t_ans[cnt][0] = j;
				t_ans[cnt][1] = i;
				t_ans[cnt][2] = k;
				mv(cnt);
				dfs(cnt + 1);
				t_ans[cnt][2] = 4 - k;
				mv(cnt);
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int num = 1;
	for (int i = 1; i <= 4; i++) {
		for (int j = 1; j <= 4; j++) {
			cin >> arr[i][j];
			corr[i][j] = num++;
		}
	}
	
	dfs(0);
	cout << result << '\n';
	for (int i = 0; i < result; i++) {
		cout << ans[i][0] << " " << ans[i][1] << " " << ans[i][2] << '\n';
	}
	system("pause");
	return 0;
}