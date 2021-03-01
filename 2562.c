#include <stdio.h>
#define NUM 9

int main()
{
	int i, j, count;
	int num_list[NUM];
	
	for(i = 0; i < NUM; i++) 
		scanf("%d", num_list + i);
	
	for(i = 0; i < NUM; i++) {
		count = 0;
		
		for(j = 0; j < NUM; j ++) {
			if (num_list[i] > num_list[j]) {
				count++;
			}
		}
		
		if (count == 8) {
			printf("%d\n", num_list[i]);
			printf("%d\n", i + 1);	
		}
	}
	
	return 0;
}
