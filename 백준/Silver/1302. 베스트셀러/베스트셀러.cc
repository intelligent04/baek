#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;
bool cmp(vector<string> &v1, vector<string> &v2)
{
    if (v1[0] == v2[0])
        return v1[1] < v2[1];
    else
        return v1[0] > v2[0];
}
int main()
{
    map<string, int> sell;
    int t;
    int index = 0;
    cin >> t;
    vector<vector<string>> v;
    vector<string> v2;
    while (t--)
    {
        string inp;
        cin >> inp;
        if (sell.count(inp) == 0)
        {
            sell[inp] = index;
            index++;
            v2.push_back("1");
            v2.push_back(inp);
            v.push_back(v2);
            v2.clear();
        }
        else
        {
            for (int i = 0; i < v.size(); i++)
            {
                if (v[i][1] == inp)
                {
                    v[i][0] = to_string(stoi(v[i][0]) + 1);
                }
            }
        }
    }
    sort(v.begin(), v.end(), cmp);
    cout << v[0][1];
}