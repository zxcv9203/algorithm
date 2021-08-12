#include <bits/stdc++.h>

using namespace std;

int ar1[51][51][51];

int recur(int a,int b, int c){

    if(a <= 0 || b <= 0 || c <= 0){
        return 1;
    }
    if (a > 20 || b > 20 || c > 20){
        return recur(20,20,20);
    } 
    //메모이제이션
    int &res = ar1[a][b][c]; //이미 있다면 반환(주소값을 지정해주어야 됨 안그러면 의미없음)
    if (res){
        return res;
    }

    if(a<b && b< c){
        res = recur(a,b,c-1) + recur(a,b-1,c-1) - recur(a,b-1,c);
    }else{
        res = recur(a-1,b,c) + recur(a-1,b-1,c) + recur(a-1,b,c-1) - recur(a-1,b-1,c-1);
    }
    return res;

}


int main(){

    std::ios_base::sync_with_stdio(false);
    cin.tie(0);
   int a,b,c;
    while(1){
        cin >> a >> b >> c;
        if(a == -1 && b == -1 && c == -1){
            break;
        }
        cout << "w("<< a << ", " << b << ", " << c << ") = " <<  recur(a,b,c) << "\n";
    }

    return 0;
}

