#include <bits/stdc++.h>

using namespace std;

int main(){
    std::ios_base::sync_with_stdio(false);
    cin.tie(0);
    int cnt = 0;
    int n, num;

    cin >> n;
    vector<int> arr(n);
    int nmax[1001];

    for(int i = 0; i < n; i++){
        cin >> num;
        arr[i] = num;
    }


    for(int i = 0; i < n; i++){
        nmax[i] = 1; //최초 길이 1로 지정

        for(int j = 0; j < i; j++){ //i 까지 비교 

            if (arr[i] > arr[j]){ //i가 인덱스 1더 앞서게

                nmax[i] = max(nmax[i], nmax[j] + 1); //i가 j보다 크면 1 증가
            }
        }
        cnt = max(cnt, nmax[i]); //저장된 값중 최대값 출력
    }

    cout << cnt << "\n";
    return 0;
}