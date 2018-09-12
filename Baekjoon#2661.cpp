/*
	Baekjoon#2661
	code by Keonyoung Shim
	SKKU University
	2018. 09. 07.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int string[80];

int right(int index, int num){
	int i, j;
	for(i=1;i<=index/2;i++){
		for(j=0;j<index-i*2+1;j++){
			int *str1;
			str1 = (int *) malloc(sizeof(int) * i);
			memcpy(str1, string+j, sizeof(int) * i);			
			if(memcmp(str1, string+j+i, sizeof(int)*i) == 0){
				return -1;
			}
			free(str1);
		}
	}
	if(index == num){
		for(i=0;i<num;i++){
			printf("%d", string[i]);
		}
		exit(0);
	}
	return 0;
}

int check(int index, int num){
	int i;
	int ret = 0;
	if(right(index,num) == -1){
		return -1;
	}
	switch(string[index-1]){
		case 1:
			string[index++] = 2;
			check(index,num);
			string[index - 1] = 3;
			check(index,num);
			break;
		case 2:
			string[index++] = 1;
			check(index,num);
			string[index - 1] = 3;
			check(index,num);
			break;	
		case 3:
			string[index++] = 1;
			check(index,num);
			string[index - 1] = 2;
			check(index,num);
			break;
	}
}

int main(){
	int num, i;
	scanf("%d", &num);
	
	for(i=0;i<80;i++){
		string[i] = 0;
	}
	string[0] = 1;
	check(1, num);

	return 0;
}
