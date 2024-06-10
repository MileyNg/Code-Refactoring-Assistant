#include <stdio.h>

int main(void)
{
  float a, b, c, d, e, f;

  while (scanf("%f%f%f%f%f%f", &a, &b, &c, &d, &e, &f) != EOF)
    printf("%.3f %.3f\n", (-b*f+c*e)/(a*e-b*d)+0.00001, (-c*d+a*f)/(a*e-b*d)+0.00001);

  return 0;
}