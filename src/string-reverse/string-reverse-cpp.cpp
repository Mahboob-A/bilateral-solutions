

#include <bits/stdc++.h>
using namespace std;

/*
C++ Version of Reverse a string making vowel as uppercase and consonants as lowercase. 
*/

bool isVowel(char c)
{
        c = tolower(c);

        return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

string rev_str_2(string inp_str)
{
        /*
        Two Pointers Algorithm.

        Taking the starting position and ending position characters.
                - Checking the characters whether they are vowel. if vowel, change to uppercase, else change to lowercase.
                - Once the modification is completed, swap the positions of the both the characters to reverse the string.

        Time Complexity: O(n)

        Space Complexity: O(1)

        */

        int start = 0;
        int end = inp_str.length() - 1;

        while (start < end)
        {
                char leftChar = inp_str[start];
                char rightChar = inp_str[end];

                if (isVowel(leftChar))
                {
                        leftChar = toupper(leftChar);
                }
                else
                {
                        leftChar = tolower(leftChar);
                }

                if (isVowel(rightChar))
                {
                        rightChar = toupper(rightChar);
                }
                else
                {
                        rightChar = tolower(rightChar);
                }

                inp_str[start] = rightChar;
                inp_str[end] = leftChar;

                start++;
                end--;
        }

        return inp_str;
}

int main()
{
        // string new_str = "Hello world";

        string new_str;

        cout << "\nInput the string to reverrse...\n";

        getline(cin, new_str); 

        string ans = rev_str_2(new_str);

        cout << "Ans: " << ans << endl;
}