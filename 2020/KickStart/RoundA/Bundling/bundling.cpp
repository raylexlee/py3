#include <iostream>
#include <algorithm>
#include <map>
using namespace std;
struct WordGreaterComparator {
    bool operator()(const std::string & left, const std::string & right) const {
        if (left.length() > right.length()) return true;
        if (left.length() < right.length()) return false;
        return (left > right);
    }
};
string prefixOf(string a, string b) {
    int l = min(a.length(), b.length());
    for (int x=0; x < l; ++x) {
        if (a[x] != b[x]) {
            if (x == 0) return "";
            return a.substr(0, x);
        }
    }
    return a.substr(0, l);
}
int main() {
    int T;
    cin >> T;
    for (int i=1; i <= T; ++i) {
        int N, K;
        cin >> N >> K;
        string w[N];
        for (int j=0; j < N; ++j) cin >> w[j];
        if (K == 1) {
            int m = 0;
            for (int j=0; j < N; ++j) m += w[j].length();
            cout << "Case #" << i << ": " << m << endl;    
            continue;
        } 
        sort(w, w + N);
        string p[N];
        p[0] = prefixOf(w[0], w[1]);
        p[N-1] = prefixOf(w[N-2], w[N-1]);
        for (int j=1; j < N-1; ++j) {
            string u = prefixOf(w[j-1], w[j]);
            string l = prefixOf(w[j+1], w[j]);
            int ul = u.length(),
                ll = l.length();
            if (ul>0 && ll>0) {
                p[j] = (ul > ll) ? u : l;
                continue;
            }
            p[j] = (ul > 0) ? u : ((ll>0) ? l : "");    
        }
        map<string, int, WordGreaterComparator> c;
        for (int j=0; j < N; ++j) {
            if (p[j].length() == 0) continue;
            if (c.count(p[j]) == 1) {
                c[p[j]]++;
            } else {
                c[p[j]] = 1;
            } 
        }
        long m = 0;
        int v, mlk, r, d, j;
        string k;
        while (!c.empty()) {
            k = c.begin()->first;
            v = c.begin()->second;
            mlk = k.length();
            r = v % K;
            d = v / K;
            if (d) m += mlk * d;
            c.erase(k);
            if (r == 0) continue;
            j = mlk - 1;
            if (c.count(k.substr(0,j))) {
                c[k.substr(0, j)] += r;
            } else {
                c[k.substr(0, j)] = r;
            }    
        }
        cout << "Case #" << i << ": " << m << endl;    
    }
}
