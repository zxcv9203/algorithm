#include <bits/stdc++.h>

using namespace std;

int main(){

    std::ios_base::sync_with_stdio(false);
    cin.tie(0);
    int res = 0;
    int a, num;
    //vector<int> vec[a];
    //vector<int> inner;

    cin >> a;
    //vector<int> vec[a];
    vector<vector<int>> vec(a, vector<int>(a));
    int sum[501][501];

    for(int i = 0; i < a; i++){
       for(int j = 0; j <= i; j++ ){
           cin >> num;
           vec[i][j] = num;
        }
    }


    //누적합 배열 선언 및 초기화
    sum[0][0] = vec[0][0];

    for(int i = 1; i < a; i++){
        for(int j = 0; j <= i; j++){

            if(j == 0){ //맨 왼쪽이거나
                sum[i][j] = sum[i-1][j] + vec[i][j]; //누적합
               

            }else if(j == i){ //맨 오른쪽일 경우
                sum[i][j] = sum[i-1][j-1] + vec[i][j];
                //바로 위에거에 자기자신더함


            }else{ //아니면 둘중 큰것을 정함
                sum[i][j] = max(sum[i-1][j]+ vec[i][j], sum[i-1][j-1]+ vec[i][j]);
         
        }
    }
}

    for (int i = 0; i < a; i++){
        if(sum[a-1][i] > res){
            res = sum[a-1][i];
        }
    }

    cout << res;

    return 0;
}

