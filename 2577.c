#include <stdio.h>
#define NUM 3

int main()
{
	int abc[NUM], num_list[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	int i, n;
	double total;

	for(i = 0; i < NUM; i++)
		scanf("%d", abc + i);
		
	total = (double)(abc[0] * abc[1] * abc[2]);
	
	while(total != 0) {
		n = (int)total % 10;
		total = (int)total / 10;
		num_list[n]++;
	}
	
		for(i = 0; i < 10; i++)
		printf("%d\n", num_list[i]);
		
	return 0;
}
