#pragma warning (disable:4996)
#include <stdio.h>
#include <stdlib.h>

int** inputSize(int *r, int*c){
	unsigned short int i;
	int **matrix;
	scanf("%d %d", r, c);
	
	matrix = (int**)calloc(*r+1, sizeof(int *));
	if (matrix == NULL)exit(1);

	for (i = 0; i < *r+1; i++){
		matrix[i] = (int*)calloc(*c + 1,sizeof(int));
		if (matrix[i] == NULL)exit(1);
	}

	return matrix;
}

void inputMatrix(int *r, int *c, int **matrix){
	unsigned short int i, j;
	for (i = 0; i < *r; i++){
		for (j = 0; j < *c; j++){
			scanf("%d", &matrix[i][j]);
		}
	}
}

void addSpread(int *r, int *c, int **matrix){
	unsigned short int i, j;
	for (i = 0; i < *r; i++){
		for (j = 0; j < *c; j++){
			matrix[i][*c] += matrix[i][j];
			matrix[*r][j] += matrix[i][j];
			matrix[*r][*c] += matrix[i][j];
		}
	}
}
void output(int *r, int *c, int **matrix){
	unsigned short int i, j;
	for (i = 0; i <= *r; i++){
		for (j = 0; j <= *c; j++){
			printf("%d", matrix[i][j]);
			if (j != *c)printf(" ");
		}
	printf("\n");
	}
}
int main(void){
	unsigned short int i;
	int r, c;
	int **matrix;

	matrix = inputSize(&r, &c);
	inputMatrix(&r, &c, matrix);
	addSpread(&r, &c, matrix);
	output(&r, &c, matrix);
	
	for (i = 0; i <= r; i++){
		free(matrix[i]);
	}
	free(matrix);
	return 0;
}