#include <stdio.h>

int main(){

	float inchestometer = 0.0254;
	float yardtofoot = 3;
	float kgtopound = 2.205;
	float litretogallon = 0.264;
	char input, reply;
	float first;

	while (1){

		printf("Enter the conversion you want to know, q to quit.\n		1. Inches to meter.\n		2. Yard to Feet.\n		3. Kg to Pound.\n		4. Litre to Gallon.\n");

		scanf("%c", &input);
		switch (input){

			case 'q':
				printf("Quitting the program\n");
				goto below_return;
				break;

			case '1':
				printf("Enter the first quantity:\n");
				scanf("%f", &first);
				printf("%f inches is equal to %f meter\n", first, first*inchestometer);
				printf("press y to continue else quit :\n");
				scanf("%c", &reply);
				printf("%c", reply);
				// if (*reply != 'y'){
				// 	goto below_return;
				// }
				break;


			case '2':
				printf("Enter the first quantity:\n");
				scanf("%f", &first);
				printf("%f yard is equal to %f feet\n", first, first*yardtofoot);
				printf("press y to continue else quit :");
				scanf("%c", &reply);
				// if (*reply != 'y'){
				// 	goto below_return;
				// }
				break;			

			case '3':
				printf("Enter the first quantity:\n");
				scanf("%f", &first);
				printf("%f kg is equal to %f Pound\n", first, first*kgtopound);
				printf("press y to continue else quit :");
				scanf("%c", &reply);
				// if (*reply != 'y'){
				// 	goto below_return;
				// }
				break;

			case '4':
				printf("Enter the first quantity:\n");
				scanf("%f", &first);
				printf("%f litre is equal to %f Gallon\n", first, first*litretogallon);
				printf("press y to continue else quit :");
				scanf("%c", &reply);
				// if (*reply != 'y'){
				// 	goto below_return;
				// }
				break;

			// default:
			// 	printf("Entered wrong option, please enter correct option:\n");
			// 	break;

		}


	}

	below_return:
	return 0;
} 