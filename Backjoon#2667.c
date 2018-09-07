#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

#define LOOP for(i=0;i<inputnum;i++) 
#define LOOP2 for(j=0;j<inputnum;j++) 


struct Dot{
	int x;
	int y;
};


int result[1000000];
int map[1000][1000];

int mapSearch(int **map, int inputnum);
int blockSearch(int **map, int inputnum, int i, int j);


int main(int argc, char** argv) {
	int inputnum;	// n lines
	int i, j;		// indexes for loop
//	char **map;		// storing map infomation
	int maxhouse;	// the max number of houses in case of input map
	int *block;		// array that stores number of houses in each block
	int result_len = 0;	// length of result array
	
	/************** input allocation starts here ******************/
	

	
	scanf("%d", &inputnum);

//	map = calloc(inputnum, sizeof(char));
//
//	LOOP{
//		map[i] = calloc(inputnum, sizeof(char));
//	}

	
	
	LOOP{
		LOOP2{
			scanf("%1d", &map[i][j]);
		}
	}

	maxhouse = inputnum * inputnum / 2 + 1;
	block = calloc(maxhouse, sizeof(int));

	/************** input allocation is over ******************/

	
//	LOOP{LOOP2{printf("%d ", map[i][j]);} printf("\n");}

	result_len = mapSearch(NULL, inputnum);
	
	for(i = 0; i < result_len; i++){
		for(j = i; j < result_len; j++){
			if(result[i] > result[j]){
				int t = result[i];
				result[i] = result[j];
				result[j] = t;
			}
		}
	}	
	
	printf("%d\n", result_len);
	for(j = 0; j < result_len; j++){
		printf("%d\n", result[j]);
	}
	return 0;
}



int mapSearch(int **maps, int inputnum){
	int i, j;
	int index = 0;
	LOOP{
		LOOP2{
			if(map[i][j] == 1){
				result[index++] = blockSearch(NULL, inputnum, i, j);
			}
		}	
	}
	
	return index;
}



int blockSearch(int **maps, int inputnum, int i, int j){
	struct Dot stack[1000];
	int index = 0;		// stack pointer
	int count = 1;		// variable for count 
	map[i][j] = 0;		// initialization of posion in the map
	while(1){
		if(map[i+1][j] == 1 && i+1 < inputnum){
			stack[index].x = i+1;
			stack[index++].y = j;
			count++;
			map[i+1][j] = 0;
		}
		if(map[i][j+1] == 1 && j+1 < inputnum){
			stack[index].x = i;
			stack[index++].y = j + 1;
			count++;
			map[i][j+1] = 0;			
		}
		if(map[i][j-1] == 1 && j-1 >= 0){
			stack[index].x = i;
			stack[index++].y = j-1;
			count++;
			map[i][j-1] = 0;
		}
		if(map[i-1][j] == 1 && i-1 >= 0){
			stack[index].x = i-1;
			stack[index++].y = j;
			count++;
			map[i-1][j] = 0;
		}
		
		if(index == 0){
			break;
		} else {
			i = stack[index-1].x;
			j = stack[index-1].y;
			index--;
		}
	}
	
	return count;
}
