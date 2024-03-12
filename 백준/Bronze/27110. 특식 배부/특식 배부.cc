#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    int A;
    int B;
    int C;
    int ans = 0;

    cin >> N;
    cin >> A >> B >> C;

    if (A < N){
        ans += A;
    }else{
        ans += N;
    }

    if (B < N){
        ans += B;
    }else{
        ans += N;
    }

    if (C < N){
        ans += C;
    }else{
        ans += N;
    }

    cout << ans;

}