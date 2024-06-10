#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DBG 0
#define BUFSIZE 1024

#define FULLORD 80

/* order 1 has 0 - 99999999*/
#define ORDNUM 8
#define ORDMAX 100000000
#define ORDARYSZ (FULLORD/ORDNUM)
static int input1_sz;
static unsigned long input1[ORDARYSZ];
static int input2_sz;
static unsigned long input2[ORDARYSZ];
static int output_sz;
static unsigned long output[ORDARYSZ];
static unsigned int input_num;

void get_input_num() {
  char buf[BUFSIZE];
  if (NULL == fgets(buf, BUFSIZE, stdin)) {
    fprintf(stderr, "Unexpected EOF\n");
    exit(1);
  }
  buf[strlen(buf)-1] = 0; // Remove \n
  input_num = atoi(buf);
  if (DBG) {
    fprintf(stderr, "input_num=%d\n", input_num);
  }
  return;
}

void get_input(unsigned long *input, int *input_sz) {
  char buf[BUFSIZE];
  char *bufp;
  char numbuf[ORDNUM+1] = {0};
  int i, len;
  *input_sz = 0;
  bzero(input, ORDARYSZ);
  if (NULL == fgets(buf, BUFSIZE, stdin)) {
    fprintf(stderr, "Unexpected EOF\n");
    exit(2);
  }
  buf[strlen(buf)-1] = 0; // Remove \n
  if (DBG) {
    fprintf(stderr, "buf=%s\n", buf);
  }
  len = strlen(buf);
  if (len > FULLORD) {
    *input_sz = -1;
    if (DBG) {
      fprintf(stderr, "input_sz overflow\n");
    }
    return;
  }
  
  for (bufp=buf+len-ORDNUM; bufp>=buf; bufp=bufp-ORDNUM) { // Fill input from lower to higher order.
    bzero(numbuf, sizeof(numbuf));
    strncpy(numbuf, bufp, ORDNUM);
    input[(*input_sz)++] = atol(numbuf);
    if (DBG) {
      fprintf(stderr, "reading[\n%s\n", buf);
      for (i=0; i<bufp-buf; i++) {
	fprintf(stderr, " ");
      }
      for (i=0; i<ORDNUM; i++) {
	fprintf(stderr, "^");
      }
      fprintf(stderr, "\n]=>%s=>%lu\n", numbuf, input[*input_sz-1]);
    }
  }
  if (bufp != buf-ORDNUM) {
    bzero(numbuf, sizeof(numbuf));
    strncpy(numbuf, buf, strlen(buf)%ORDNUM);
    input[(*input_sz)++] = atol(numbuf);
    if (DBG) {
      fprintf(stderr, "reading[\n%s\n", buf);
      for (i=0; i<strlen(buf)%ORDNUM; i++) {
	fprintf(stderr, "^");
      }
      fprintf(stderr, "\n]=>%s=>%lu\n", numbuf, input[*input_sz-1]);
    }
  }
  if (DBG) {
    fprintf(stderr, "input_sz=%d\n", *input_sz);
    for (i=0; i<ORDARYSZ; i++) {
      fprintf(stderr, "input[%d]=%lu\n", i, input[i]);
    }
  }
  return;
}

void get_output() {
  int i;
  unsigned long next = 0;
  unsigned long sum = 0;
  output_sz = input1_sz > input2_sz ? input1_sz : input2_sz;
  if (DBG) {
    fprintf(stderr, "initial output_sz=%d\n", output_sz);
  }
  if (input1_sz == -1 || input2_sz == -1) {
    output_sz = -1;
    return;
  }
  for (i=0; i<output_sz; i++) {
    sum = input1[i] + input2[i] + next;
    if (sum >= ORDMAX) {
      next = sum/ORDMAX;
    }
    else {
      next = 0;
    }
    output[i] = sum%ORDMAX;
  }
  if (next != 0) {
    if (output_sz < ORDARYSZ-1) {
      output[output_sz++] = next;
    }
    else {
      output_sz = -1;
    }
  }
  if (DBG) {
    fprintf(stderr, "final output_sz=%d\n", output_sz);
    for (i=0; i<ORDARYSZ; i++) {
      fprintf(stderr, "output[%d]=%lu\n", i, output[i]);
    }
  }
  return;
}

void print_output() {
  int i;
  if (input1_sz == -1 || input2_sz == -1 || output_sz == -1) {
    printf("overflow\n");
    return;
  }
  printf("%lu", output[output_sz-1]);
  if (DBG) {
    fprintf(stderr, "result[%d]=%lu\n", output_sz-1, output[output_sz-1]);
  }
  for (i=output_sz-2; i>=0; i--) {
    printf("%08lu", output[i]);
    if (DBG) {
      fprintf(stderr, "result[%d]=%08lu\n", i, output[i]);
    }
  }
  printf("\n");
  if (DBG) {
    fprintf(stderr, "result=%lu,", output[output_sz-1]);
    for (i=output_sz-2; i>=0; i--) {
      fprintf(stderr, "%08lu,", output[i]);
    }
    fprintf(stderr, "\n");
  }
}

int main (void) {
  int i;
  get_input_num();
  for (i=0; i<input_num; i++) {
    get_input(input1, &input1_sz);
    get_input(input2, &input2_sz);
    get_output();
    print_output();
  }
  return 0;
}