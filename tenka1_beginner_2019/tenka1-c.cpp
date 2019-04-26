/* 入力された文字列sを以下の形式に変更する場合に、変更す必要がある文字数の最小値を求める
 * 形式: 左側を任意の個数の'.'、右側を任意の個数の'#'とする文字列
 * 例: "...##", "#####", "....."
 */ 

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(void){
    int n;
    string s;

    cin >> n >> s;

    // #の数の累積和をwに格納する
    // s[i]までの#の数 == w[i + 1]
    vector<int> w(n + 1);
    for(int i=0; i<n; i++){
        if(s[i] == '#'){
            w[i + 1] = w[i] + 1; 
        }else{
            w[i + 1] = w[i];
        }
    }

    // s[i]からs[n-1]までを#とする場合に変更する必要がある文字数を求める
    int ans = 2e5;
    for(int i=0; i<=n; i++){
        // 変更する必要がある文字数　== 左側にある'#'の数 + 右側にある'.'の数
        // 左側にある'#'の数 == w[i]
        // 右側にある'.'の数 == n-i-(w[n]-w[i])
        ans = min(ans, w[i] + n - i - (w[n] - w[i]));
    }
    cout << ans;

    return 0;
}