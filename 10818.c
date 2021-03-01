#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main()
{
	int num, i, j;
	int max = INT_MIN;
	int min = INT_MAX;
	
	scanf("%d", &num);
	
	int* num_list = (int*)malloc(num * sizeof(int));
	
	for(i = 0; i < num; i++)
		scanf("%d", num_list + i);
		
	for(i = 0; i< num; i++) {
		if(num_list[i] > max)
			max = num_list[i];
		
		if(num_list[i] < min)
			min = num_list[i];
	}
	
	printf("%d %d", min, max);
	
	return 0;
}
