#include<stdio.h>

int main(){
    int n, a, b, c;
    
    scanf("%d %d %d %d", &n, &a, &b, &c);
    printf("%d", (a < n ? a: n) + (b < n ? b: n) + (c < n ? c: n));
    
    return 0;
}