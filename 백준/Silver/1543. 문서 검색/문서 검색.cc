#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    string inp;
    string word;
    getline(cin, inp);
    getline(cin, word);
    int wordLen = word.length();
    int stack = 0;
    int cnt = 0;
    while (wordLen <= inp.length())
    {
        for (int i = 0; i < wordLen; i++)
        {
            if (inp[i] == word[i])
                stack += 1;
            if (stack == wordLen)
            {
                cnt += 1;
                inp.erase(0, stack);
                stack = 0;
            }
            else if (inp[i] != word[i])
            {
                inp.erase(0, 1);
                stack = 0;
            }
        }
    }
    cout << cnt;
}