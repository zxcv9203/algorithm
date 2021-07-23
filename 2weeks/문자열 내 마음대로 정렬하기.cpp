#include <string>
#include <algorithm>
#include <vector>
#include <iostream>


using namespace std;

vector<string> solution(vector<string> strings, int n) {
    vector<string> answer;
    
    vector<pair <char, string> > hash;
    int i = 0;
    for (size_t i = 0; i < strings.size(); ++i) 
    {
        hash.push_back(make_pair(strings[i][n], strings[i]));
    }
    
    sort(hash.begin(), hash.end());
    
    i = 0;
    for(int i = 0; i< strings.size();i++)
    {
        answer.push_back(hash[i].second);
    }
    return answer;
}
