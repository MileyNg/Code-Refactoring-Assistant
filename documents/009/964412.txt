#include <stdio.h>

static const int monthDays[13]={
	0,31,59,90,120,151,181,212,243,273,304,334,365
};

static long long getDays(int year) {
	long long result;
	if(year<0)return -getDays(-year)-366+365;
	else if(year==0)return 0;
	result=(long long)year*365;
	result+=year/4;
	result-=year/100;
	result+=year/400;
	return result;
}

static long long getDays2(int fromYear,int toYear) {
	return getDays(toYear)-getDays(fromYear);
}

static int getLeapYearNum(int year) {
	int result;
	if(year<0)return -getLeapYearNum(-year)-1;
	else if(year==0)return 0;
	result=year/4;
	result-=year/100;
	result+=year/400;
	return result;
}

static int getLeapYearNum2(int fromYear,int toYear) {
	return getLeapYearNum(toYear)-getLeapYearNum(fromYear);
}

static int isLeapYear(int year) {
	return (year%400==0 || (year%4==0 && year%100!=0));
}

long long date2dayCount(int year,int month,int date) {
	long long result;
	if(month<1 || month>12)return 0;
	result=getDays2(1969,year-1);
	result+=monthDays[month-1];
	if(isLeapYear(year)) {
		if(month>=3)result++;
	}
	result+=date-1;
	return result;
}

void dayCount2date(int* year,int* month,int* date,long long days) {
	int i;
	int yearNum;
	int amariDays;
	int daySeconds;
	int hoseiYear;
	int is2_29;
	if(days>=0) {
		yearNum=1970+(int)(days/365);
		amariDays=(int)(days%365);
	} else {
		days=-days;
		yearNum=1970-(int)(days/365)-1;
		amariDays=365-(int)(days%365);
	}
	amariDays-=getLeapYearNum2(1969,yearNum-1);
	while(1) {
		if((amariDays>=0 && amariDays<365) ||
			(amariDays==365 && isLeapYear(yearNum)))break;
		if(amariDays<0) {
			hoseiYear=(-amariDays)/365+1;
			amariDays+=hoseiYear*365;
			amariDays+=getLeapYearNum(yearNum-1)-
				getLeapYearNum(yearNum-hoseiYear-1);
			yearNum-=hoseiYear;
		} else if(amariDays>=365) {
			hoseiYear=amariDays/365;
			amariDays=amariDays%365;
			amariDays-=getLeapYearNum(yearNum+hoseiYear-1)-
				getLeapYearNum(yearNum-1);
			yearNum+=hoseiYear;
		} else break;
	}
	is2_29=0;
	if(isLeapYear(yearNum) && amariDays>=59) {
		if(amariDays==59)is2_29=1;
		amariDays--;
	}
	for(i=1;i<=12;i++) {
		if(amariDays>=monthDays[i-1] && amariDays<monthDays[i])break;
	}
	amariDays-=monthDays[i-1];
	if(is2_29)amariDays++;
	*year=yearNum;
	*month=i;
	*date=amariDays+1;
}

int main(void) {
	char input[1024];
	long long days_origin=date2dayCount(2012,12,21);
	while(fgets(input,sizeof(input),stdin)) {
		long long days;
		int b,ka,t,w,ki;
		int y,m,d;
		int sscret;
		sscret=sscanf(input,"%d.%d.%d.%d.%d",&b,&ka,&t,&w,&ki);
		if(sscret==5) {
			/* maya -> seireki */
			days=b;
			days=days*20+ka;
			days=days*20+t;
			days=days*18+w;
			days=days*20+ki;
			dayCount2date(&y,&m,&d,days+days_origin);
			printf("%d.%d.%d\n",y,m,d);
		} else if(sscret==3) {
			/* seireki -> maya */
			y=b;m=ka;d=t;
			days=date2dayCount(y,m,d)-days_origin;
			ki=days%20;days/=20;
			w=days%18;days/=18;
			t=days%20;days/=20;
			ka=days%20;days/=20;
			b=days%13;
			printf("%d.%d.%d.%d.%d\n",b,ka,t,w,ki);
		} else break;
	}
	return 0;
}