#include<stdio.h>

int main(){
/*
    int a[3][2][1] = {1, 2, 3, 4, 5, 6};

    int i = 0, j = 0, k = 0;
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 2; j++)
        {
            for (k = 0; k < 1; k++)
            {
                printf("The value of a[%d][%d][%d] is %u\n", i, j, k, a[i][j][k]);
                printf("The address of a[%d][%d][%d] is %u\n", i, j, k, &a[i][j][k]);
            }
        }
    }
    printf("The address of a is %u\n", a);
    printf("The address of a + 1 is %u\n", a + 1);
    printf("The value of ***a + 1 is %d\n", *(*(*(a + 1))));

    int a[1][2][3] = {1, 2, 3, 4, 5, 6};

    int i = 0, j = 0, k = 0;
    for (i = 0; i < 1; i++)
    {
        for (j = 0; j < 2; j++)
        {
            for (k = 0; k < 3; k++)
            {
                printf("The value of a[%d][%d][%d] is %u\n", i, j, k, a[i][j][k]);
                printf("The address of a[%d][%d][%d] is %u\n", i, j, k, &a[i][j][k]);
            }
        }
    }
    printf("The address of a is %u\n", a);
    printf("The address of *a + 1 is %u\n", *a + 1);
    /*
    printf("The value of ***a + 1 is %d\n", *(*(*(a + 1)))); */

    int a[2][1][3] = {1, 2, 3, 4, 5, 6};

    int i = 0, j = 0, k = 0;
    for (i = 0; i < 2; i++)
    {
        for (j = 0; j < 1; j++)
        {
            for (k = 0; k < 3; k++)
            {
                printf("The value of a[%d][%d][%d] is %u\n", i, j, k, a[i][j][k]);
                printf("The address of a[%d][%d][%d] is %u\n", i, j, k, &a[i][j][k]);
            }
        }
    }
    printf("The address of a is %u\n", a);
    printf("The address of a + 1 is %u\n", a[0][0][2]);
    printf("The value of ***a + 1 is %d\n", *(*(*(a + 1))));
}
