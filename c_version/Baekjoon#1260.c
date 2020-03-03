#include <stdio.h>

int map[1000][1000];
int map2[1000][1000];

int main(){
	int n, m, start;
	scanf("%d %d %d", &n, &m, &start);
	
	int i, j;
	int num1, num2;
	int stack[10000], queue[10000], array[10000];
	
	for(i=0;i<1000;i++){
		for(j=0;j<1000;j++){
			map[i][j] = 0;
			map2[i][j] = 0;
		}
	}
	
	for(i=0;i<10000;i++){
		array[i] = 0;
	}
	
	for(i=0;i<m;i++){
		scanf("%d %d", &num1, &num2);
		map[num1-1][num2-1] = 1;
		map[num2-1][num1-1] = 1;
		map2[num1-1][num2-1] = 1;
		map2[num2-1][num1-1] = 1;
	}
	
		
	int count = 0;
	int index = 0;
	int index_i = 0;
	int tmp = 0;
	int flag = 0;
	stack[index++]= start;
	while(1){
		count = 0;
		flag = 0;
		tmp = stack[--index];
		for(i=0;i<index_i;i++){
			if(tmp == array[i]){
				flag = 1;
				break;
			}
		}
		if(flag == 0 && tmp != 0){
			array[index_i++] = tmp;
			printf("%d ", tmp);
		}
		flag = 1;
		for(i = n-1; i >= 0; i--){
			if(map[tmp-1][i] == 1){
				map[tmp-1][i] = 0;
				map[i][tmp-1] = 0;
				stack[index++] = i+1;
			}
		}
		
		if(index == -1){
			break;
		}
	}
	
	
	printf("\n");
	
	/************************* bfs starts here ********************************/
	
	for(i=0;i<10000;i++){
		array[i] = 0;
	}
		
	index = 1;
	int front = 0;
	queue[front] = start;
	index_i = 0;
	while(1){
		
		flag = 0;
		tmp = queue[front++];
		for(i=0;i<index_i;i++){
			if(tmp == array[i]){
				flag = 1;
				break;
			}
		}
		
		if(flag == 0 && tmp != 0){
			array[index_i++] = tmp;
			printf("%d ", tmp);
		}
		
		for(i = 0; i < n; i++){
			if(map2[tmp-1][i] == 1){
				map2[tmp-1][i] = 0;
				map2[i][tmp-1] = 0;
				queue[index++] = i+1;
			}
		}
		
		if(front > index){
			break;
		}
	}
	
	return 0;
}
