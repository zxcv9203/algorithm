#include <string>
#include <vector>

using namespace std;

string solution(int n) {
    string answer = "";
    int i = 0;
    string watermelon[2] = {"수", "박"};
    
    while (i < n)
    {
        if (i % 2 == 0)
            answer.append(watermelon[0]);
        else
            answer.append(watermelon[1]);
        i++;
    }
    return answer;
}
