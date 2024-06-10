#include <stdio.h>
#include <string.h>
typedef struct {
  char name[20];
  int speed;
}  Process;
#define MAX 100001
Process S[MAX];
int s_top=0,s_tail=0;
int num;

void Enqueue(Process );
Process Dequeue(void );
int main()
{
  Process in;
  int i;
  int qua=0;
  int time_spend=0;
  
  scanf("%d %d",&num,&qua);
  //printf("%d %d\n",num,qua);
  for(i=0;i<num;i++)
    {
      scanf("%s %d",in.name,&in.speed);
      //printf("%s %d\n",in.name,in.speed);
      Enqueue(in);
    }

  while(s_top != s_tail)  
  {
      in=Dequeue();
      //printf("%s %d\n",in.name,in.speed);
      if(qua >= in.speed)
    {
      time_spend+=in.speed;
      printf("%s %d\n",in.name,time_spend);
    }
      else
     {
      time_spend+= qua;
      in.speed -= qua;
      Enqueue(in);
      //printf("%s %d\n",in.name,in.speed);
     }
    }
   return 0;
}
void Enqueue(Process in)
{
   S[s_tail] = in;
   //printf("%s %d\n",S[s_tail].name,S[s_tail].speed);
   if(s_tail == MAX-1) s_tail =0;
   else s_tail++;
}

Process Dequeue()
{
   Process out;
   out=S[s_top];
   if(s_top == MAX-1) s_top =0;
   else s_top++;
   return out;
}