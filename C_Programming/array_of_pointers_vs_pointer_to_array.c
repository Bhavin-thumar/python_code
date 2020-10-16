#include<stdio.h>

int main(){

 /*   int (*p)[3];    // pointer to array of 3 integers.


    int a[4][3] = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9},
            {10, 11, 12}
        };


    int b[4][3] = {
            {10, 20, 30},
            {40, 50, 60},
            {70, 80, 90},
            {100, 110, 120}
        };

    p = a;
    int *ptr[3] = {b, b+3, b+2};    // array of 3 integer pointers.

    printf("The address of a is %u\n", a);
    printf("The address of a[1] is %u\n", a[1]);
    printf("The address of p is %u\n", p);
    printf("The address of p+1 is %u\n", p[1]);
    printf("The address of b[3] is %u\n", b[3]);
    printf("The address of ptr+1 is %u\n", ptr[1]); */

   /* int a[3][2][2][2][3];

    int i = 0, j = 0, k = 0, l = 0, m = 0, count = 1;

    for (i=0;i<3;i++)
    {
        for (j=0;j<2;j++)
            {
            for (k=0;k<2;k++)
                {
                for (l=0;l<2;l++)
                    {
                    for (m=0;m<3;m++)
                        {
                        a[i][j][k][l][m] = count;
                        count++;
                        }
                    }
                }
             }
    }

    for (i=0;i<3;i++)
        for (j=0;j<2;j++)
            for (k=0;k<2;k++)
                for (l=0;l<2;l++)
                    for (m=0;m<3;m++)
                    {
                        printf("the value of a[%d][%d][%d][%d][%d] = %d\n", i, j, k, l, m, a[i][j][k][l][m]);
                        if (a[i][j][k][l][m] == 46)
                        {
                            printf("the address is %u\n", &a[i][j][k][l][m]);
                        }
              }

    printf("the value at address a[1][1][1][1] %u", a[1][1][1][1]); */

    char (*fruits)[4] = {"2 apples", "2 bananas", "3 oranges", "1 strawberry"};

    printf("%s\n", fruits[2]);

    return 0;
}
