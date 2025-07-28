#include <bits/stdc++.h>
#define ll long long
#define ull unsigned long long
#define MOD 1000000007
#define MAXN 10000005
#define ii pair<int, int>
#define fio() ios::sync_with_stdio(0); cin.tie(0);

using namespace std;

vector<ii> adj[1005];
bool visited[1005];
int dis[1005];
int n, m, u;

void dijkstra(){
    for (int i = 1; i <= n; i++) dis[i] = 1e9;
    dis[u] = 0;
    priority_queue<ii, vector<ii>, greater<ii>> q;
    q.push({0, u});
    while (!q.empty()){
        auto top = q.top();
        q.pop();
        int u = top.second, d = top.first;
        /* if (d > dis[u])  */
        for (auto it : adj[u]){
            int v = it.first, w = it.second;
            if (dis[v] > dis[u] + w){
                dis[v] = dis[u] + w;
                q.push({dis[v], v});
            }
        }
    }
    for (int i = 1; i <= n; i++) cout << dis[i] << " ";
    cout << endl;
}

int main(){
    fio();
    /* ducknife */
    int t; cin >> t;
    while (t--){
        for (auto &i : adj) i.clear();
        cin >> n >> m >> u;
        for (int i = 1; i <= m; i++){
            int x, y, w; cin >> x >> y >> w;
            adj[x].push_back({y, w});
            adj[y].push_back({x, w});
        }
        dijkstra();
    }
    return 0;
}