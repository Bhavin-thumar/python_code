#include<stdio.h>



int main(){
    int a_row, a_column;
    printf("Enter matrix dimension of a :");
    scanf("%d %d", &a_row, &a_column);

    int b_row, b_column;
    printf("Enter matrix dimension of b :");
    scanf("%d %d", &b_row, &b_column);

    int a_matrix[a_row][a_column];
    int b_matrix[b_row][b_column];

    for (int i = 0; i < a_row; i++)
    {
        for (int j= 0; j < a_column; j++)
        {
                printf("Enter value for %d %d index of a :", i, j);
                scanf("%d", &a_matrix[i][j]);
        }
    }


    for (int i = 0; i < b_row; i++)
    {
        for (int j= 0; j < b_column; j++)
        {
                printf("Enter value for %d %d index of b :", i, j);
                scanf("%d", &b_matrix[i][j]);
        }
    }

    int result[a_row][b_column];

    for (int k = 0; k < a_row; k++)
    {
        for (int i = 0; i < b_column; i++)
        {
            int sumproduct = 0;
            int product = 0;
            for (int j = 0; j < a_row; j++)
            {
                product = a_matrix[k][j] * b_matrix[j][i];
                sumproduct += product;

            }
            result[k][i] = sumproduct;
        }

    }

    for (int i = 0; i < a_row; i++)
    {
        for (int j = 0; j < b_column; j++)
        {
            printf("The value of result[%d][%d] matrix : %d\n", i, j, result[i][j]);
        }
    }


    return 0;


}

