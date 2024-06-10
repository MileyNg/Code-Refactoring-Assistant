#include<stdio.h>

int main(){ int aa, bb, cc;
	scanf ("%d %d %d", &aa, &bb, &cc);
	if (aa <= bb && bb <= cc) printf ("%d %d %d\n", aa, bb, cc);
	if (aa <= cc && cc <= bb) printf ("%d %d %d\n", aa, cc, bb);
	if (bb <= aa && aa <= cc) printf ("%d %d %d\n", bb, aa, cc);
	if (bb <= cc && cc <= aa) printf ("%d %d %d\n", bb, cc, aa);
	if (cc <= aa && aa <= bb) printf ("%d %d %d\n", cc, aa, bb);
	if (cc <= bb && bb <= aa) printf ("%d %d %d\n", cc, bb, aa);
	return 0;
}