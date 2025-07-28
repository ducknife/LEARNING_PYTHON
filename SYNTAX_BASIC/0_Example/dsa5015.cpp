/* P(n, k) = P(n-1, k) + k*P(n-1, k-1) */
#include <bits/stdc++.h>
#define ll long long
#define ull unsigned long long
#define MOD 1000000007
#define MAXN 10000005
#define fio() ios::sync_with_stdio(0); cin.tie(0);

using namespace std;

vector<int> adj[1005];
bool visited[1005];
ll perm[1005][1005];

void setup(){
    for (int i = 0; i <= 1000; i++) perm[i][0] = 1;
    for (int i = 1; i <= 1000; i++){
        for (int j = 1; j <= i; j++){
            perm[i][j] = perm[i - 1][j] % MOD + (j * perm[i - 1][j - 1]) % MOD;
            perm[i][j] %= MOD;
        }
    }
}

int main(){
    fio();
    /* ducknife */
    setup();
    int t; cin >> t;
    while (t--){
        int n, k; cin >> n >> k;
        cout << perm[n][k] << endl;
    }
    return 0;
}