#include<stdio.h>
#define N 5

int add(int *ptr, int n){
    int sum = 0;

    for(int i = 0; i < n; i++){
        sum += *ptr;
        ptr++;

    }
    return sum;

}


int main(){

    int a[N] = {10, 20, 30, 40, 50};
    int len = sizeof(a) / sizeof(a[0]);
    int sum = add(a, len);
    printf("%d", sum);
    return 0;
}
