

#include <bits/stdc++.h>
using namespace std;

#define pii pair<int, int>
#define f first
#define s second
#define vec vector<int>
#define vecPii vector<pair<int, int>>
#define pb push_back
#define ppb pop_back
#define DOUBLE_INF 1e18
#define INT_INF 1e9
const int N = 1e5 + 100;
vector<int> ans;
vector<pii> allSrc;
pii src, destination;
priority_queue<pii, vecPii, greater<pii>> q;
vecPii adjList[N];
int visited[N];
int parent[N];
long long dist[N];
int n, m;



/*
Find unique elements from integer array. 

Time Complexity: O(n)

Space Complexity: O(n). Elementary array for index hashing. 
*/


void sol()
{

        // int arr[] = {1, 3, 3, 3, 3, 4, 4, 5, 6, 2, 1, 2, 1, 2, 4, 5, 3, 2, 1, 5, 9, 8, 7, 6, 7, 5, 7, 2, 3};   // 29 | unique: 9 
        int arr[] = {1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6};   // 12 | unique 6 

        int n = sizeof(arr) / sizeof(arr[0]);

        cout << "\nArray size: " << n << endl; 

        int mx = INT_MIN;
        for (int i = 0; i < n; i++)
        {
                if (arr[i] > mx)
                        mx = arr[i];
        }

        int check_sum[mx + 1];

        for (int i = 0; i < mx + 1; i++)
        {
                check_sum[i] = 0;
        }

        for (int i = 0; i < n; i++)
        {
                check_sum[arr[i]]++;
        }

        int unique_values = 0;

        for (int i = 0; i < mx + 1; i++)
        {
                if (check_sum[i] > 0)
                        unique_values++;
        }

        cout << "\nUnique Elements: " << unique_values << endl
             << endl;
}

int main()
{

        sol();

        return 0;
}