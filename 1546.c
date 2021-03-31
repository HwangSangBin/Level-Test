#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable : 4996)

int main()
{
	int num, i, temp;
	double no, MAX;

	MAX = 0;
	no = 0;

	scanf("%d", &num);

	double* num_list = (double*)malloc(sizeof(double) * num);

	for (i = 0; i < num; i++)
		scanf("%lf", num_list + i);

	for (i = 0; i < num; i++) {
		if (num_list[i] > MAX) {
			MAX = num_list[i];
		}
	}

	for (i = 0; i < num; i++) {
		num_list[i] = num_list[i] / MAX * 100;
	}

	for (i = 0; i < num; i++) {
		no += num_list[i];
	}

	printf("%.2lf", no / (double)num);

	return 0;
}
