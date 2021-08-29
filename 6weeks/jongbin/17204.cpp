#include <bits/stdc++.h>

using namespace std;

int main(){

    std::ios_base::sync_with_stdio(false);

    cin.tie(0);

    int n, m, num;
    int arr[151];
    int visit[151] = {0,}; 

    cin >> n >> m;


    for(int i = 0; i < n; i++){
        cin >> num;
        arr[i] = num;
    }

    visit[0] = 1;

    int next = arr[0];
    int j = 1;
    while(1) {
        //1 or 0
        if(visit[next]){
            cout << -1 << "\n";
            break;
        }else{
            if(next == m){
                cout << j << "\n";
                break;
            }
            //방문처리하고
            visit[next] = 1;
            //다음 방문 처리
            next = arr[next];
        }
        j++;
    }


    return 0;
}