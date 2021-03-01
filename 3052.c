#include <stdio.h>
#pragma warning(disable : 4996)
#define NUM 10

int main()
{
	int i, j, result;
	int num_list[NUM];

	result = 1;

	for (i = 0; i < NUM; i++) {
		scanf("%d", num_list + i);
		*(num_list + i) = *(num_list + i) % 42;
	}

	for (i = 0; i < NUM; i++) {
		for (j = i + 1; j < NUM; j++) {
			if (*(num_list + i) == *(num_list + j)) {
				break;
			}
			else if (j == 9) {
				if (*(num_list + i) != *(num_list + j)) {
					result++;
				}
			}
		}
	}

	printf("%d\n", result);

	return 0;
}
