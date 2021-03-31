#include <stdio.h>

int main()
{
	int num, student, i, j, h, aver;
	int total = 0;
	int count = 0;
	int student_grade[100];
	double per;
	
	scanf("%d", &num);
	
	scanf("%d", &student);
	
	for(i = 0; i < num; i++){
		for(j = 0; j < student; j++) {
			scanf("%d", student_grade + i);
			total += student_grade[i];
		}
		aver = total / student;
	
		for(h = 0; h < student; h++) {
			if(student_grade[i] > aver) {
				count++;
			}
		}
	
		per = (double)(count / student * 100);
	
		printf("%.3lf%", per);
	}

	return 0;
}
