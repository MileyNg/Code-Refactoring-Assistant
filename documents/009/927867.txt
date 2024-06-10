#include<stdio.h>
#include<string.h>
#define LEN 100005

typedef struct pp {
	char name[100];
	int t;
} P;

P Q[LEN + 1];
int head, tail, n;

void enqueue(P x) {
	if (tail >= LEN) {
		tail = 0;
	}
	Q[tail++] = x;
}

P dequeue() {
	P u = { "p0", 0 };

	if (head == tail || head > tail) return u;
	else {
		if (head >= LEN) {
			head = 0;
		}
		return Q[head++];
	}
}

int main() {
	int elaps = 0;
	int cnt = 0;
	int i, q;

	scanf("%d %d", &n, &q);

	tail = n;

	for (i = 0; i < n; i++) {
		scanf("%s", Q[i].name);
		scanf("%d", &Q[i].t);
	}

	while (1) {

		if (Q[head].t <= q) {
			if (cnt == n) break;
			elaps += Q[head].t;
			printf("%s %d\n", Q[head].name, elaps);
			dequeue(Q[head]);
			cnt++;
		} else {
			Q[head].t -= q;
			elaps += q;
			enqueue(dequeue(Q[head]));
		}
	}

	return 0;
}