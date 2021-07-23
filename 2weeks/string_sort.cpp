#include <string>
#include <vector>
#include <algorithm>
using namespace std;
 
int i;
 
bool comp(string a, string b) {
    if (a.at(i) != b.at(i)){
        return a.at(i) < b.at(i);
    } 
    else return a < b;
}
 
vector<string> solution(vector<string> strings, int n) {
    vector<string> answer;
 
    i = n;

    sort(strings.begin(), strings.end(), comp);
    answer = strings;
 
    return answer;
}

#include <iostream>
int main() {
    vector<string> strings = {"abce", "abcd", "cdx"};
    int n = 1;

    vector <string>test = solution(strings, n);
    for (int i = 0; i < test.size(); i++){
        cout << test[i] << " ";
    }
    return 0;
}