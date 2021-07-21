#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool check[101];
vector<int> graph[101];
int cnt = 0;

void dfs(int x){
    check[x] = true;

    for(int i = 0; i < graph[x].size(); i++){
        int y = graph[x][i];
        if(!check[y]){
            dfs(y);
            cnt++;
        }
    }
}

int main(){

    int n,m;
    int a,b;

    cin >> n;
    cin >> m;

    for(int i = 0; i < m; i++){
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    dfs(1);

    cout << cnt << "\n";

    return 0;
}
