#include<stdio.h>

struct car{

    char engine[30];
    char engine_type[10];
    int fuel_cap;
    int seating_cap;
    float mileage;

};

int main(){

    // struct car c[3] = {{"F3 vtvi", "petrol", 100, 1, 5.67},
       //                 {"Ffret3 tv", "diesel", 10, 2, 15.67},
         //               {"F3 vtvi", "hybrid", 50, 5, 25.67}
           //             };

    // printf("%s", c[2].engine_type);
    struct car c = {"F3 vtvi", "petrol", 100, 1, 5.67};

    printf("Address of &c : %u\n", &c);
    printf("size of structure c : %d\n", sizeof(c));
    printf("Address of &c + 1 : %u\n", &c + 1);
    printf("Value of c : %u\n", c);

    struct car *ptr_car = &c;

    printf("value of ptr_car : %s\n", ptr_car);
    printf("Value of ptr_seating_cap : %d\n", ptr_car->fuel_cap);
  //  printf("Value of ptr : %x\n", ptr);
    return 0;
}
