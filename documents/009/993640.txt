#include <stdio.h>

typedef struct element_{
	int h, p, q;
} element;

void elem_copy(element* src, element* dst) {
	src->h = dst->h;
	src->p = dst->p;
	src->q = dst->q;
}

int main(void) {
	int n, m, a, i, j;
	int line[105];
	element elem[1001];
	element e;
	int t;
	
	while(scanf("%d %d %d\n", &n, &m, &a)==3) {
		if(n==0 && m==0 && a==0) break;
		
		for(i=0;i<=100;i++) line[i] = i;
		
		for(i=0;i<m;i++) {
			scanf("%d %d %d\n", &(elem[i].h), &(elem[i].p), &(elem[i].q));
		}
	
		for(i=0;i<m-1;i++) {
			for(j=i+1;j<m;j++) {
				if(elem[i].h < elem[j].h) {
					elem_copy(&e, &elem[i]);
					elem_copy(&elem[i], &elem[j]);
					elem_copy(&elem[j], &e);
				}
			}
		}
		
		for(i=0;i<m;i++) {
			t = line[elem[i].p];
			line[elem[i].p] = line[elem[i].q];
			line[elem[i].q] = t;
		}
		
		for(i=0;i<=n;i++) {
			if(line[i] == a) {
				printf("%d\n", i);
				break;
			}
		}
	}
	return 0;
}