#include <stdio.h>
#include <string.h>

int main()
{
	char arr[1000000];
	int num = 1, i;
	
	gets(arr);
	
	if(strlen(arr) == 1) {
		if(arr[0] == ' ') {
			printf("0");
			return 0;
		}
	}
	for(i = 1; i < strlen(arr) - 1; i++) {
		if(arr[i] == ' ') {
			num++;
		}
		if(arr[i] == ' ' && arr[i - 1] == ' ') {
			num -= 1;
		}
	}
	
	printf("%d\n", num);
	
	return 0;
}
