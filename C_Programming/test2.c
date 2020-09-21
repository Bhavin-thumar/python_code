#include<stdio.h>

int a = 10;

int main(){

    int a = 0;
    a += 20;
    printf("The value of a is %x", &a);
    return 0;
}
