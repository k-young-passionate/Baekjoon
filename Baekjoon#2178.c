#include <stdio.h>

struct Dot {
	int x;
	int y;
};

int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

int main(){
	int m, n, i, j, x, y;
	int map[100][100];
	int index = 0;
	int front= 0;
	int count = 0;
	int var1,var2;
	var1 = 0;
	var2 = 0;
	struct Dot queue[10000];
	
	scanf("%d %d", &m, &n);
	
	for(i=0;i<m;i++){
		for(j=0;j<n;j++){
			scanf("%1d", &map[i][j]);
		}
	}
	
	queue[index].x = 0;
	queue[index++].y = 0;
	map[0][0] = 0;
	count = 2;

	var1 = 1;
	while(1){
		x = queue[front].x;
		y = queue[front++].y;
		
		for(i=0;i<4;i++){
			int newx = x+dx[i];
			int newy = y+dy[i];
			if(map[newx][newy] == 1 && newx < m && newx >= 0 && newy < n && newy >= 0){
				queue[index].x = newx;
				queue[index++].y = newy;
				map[newx][newy] = 0;
				var2++;
			}
		}
	
		var1--;
		
		if(map[m-1][n-1] == 0){
			break;
		}
		
		if(var1 == 0){
			var1 = var2;
			var2 = 0;
			count++;
		}
		
	}
	
	printf("%d",count);
	return 0;
}
