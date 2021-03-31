#include <stdio.h>
#include <string.h>
#pragma warning(disable : 4996)

int main()
{
	char word[81];
	int result, num, add;
	int i, j;

	scanf("%d", &num);

	for (i = 0; i < num; i++) {
		result = 0;
		add = 1;
		j = 0;

		scanf("%s", word);

		for (j = 0; j < strlen(word); j++) {
			if (word[j] == 'O') {
				result += add;
				add++;
			}
			else {
				add = 1;
			}
		}
		printf("%d\n", result);
	}
	return 0;
}
