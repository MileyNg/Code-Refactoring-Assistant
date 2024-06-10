#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

struct _node_table {
    int* next_node;
    int* cost;
    int size;
    int capacity;
} node_table[100005];

int dp[100005];

void init_node(int i) {
    node_table[i].capacity = 10;
    node_table[i].next_node = (int*)malloc(node_table[i].capacity*sizeof(int));
    node_table[i].cost = (int*)malloc(node_table[i].capacity*sizeof(int));
    node_table[i].size = 0;
}

void free_node(int i) {
    free(node_table[i].next_node);
    free(node_table[i].cost);
}

void grow_node(int s) {
    if(node_table[s].capacity < node_table[s].size+2) {
        int size, i;
        int* next_node = node_table[s].next_node;
        int* cost = node_table[s].cost;
        node_table[s].capacity *= 1.5;
        node_table[s].next_node = (int*)malloc(node_table[s].capacity*sizeof(int));
        node_table[s].cost = (int*)malloc(node_table[s].capacity*sizeof(int));
        for(i=0,size=node_table[s].size;i<size;i++) {
            node_table[s].next_node[i] = next_node[i];
            node_table[s].cost[i] = cost[i];
        }
        free(next_node);
        free(cost);
    }
}

void add_next_node(int s, int t, int d) {
    int size = node_table[s].size;
    node_table[s].next_node[size] = t;
    node_table[s].cost[size] = d;
    node_table[s].size++;

    grow_node(s);
}

void solve(int r, int V) {
    int i, size, from, to, cost;
    int queue[SHRT_MAX];
    int wp, rp;

	dp[0] = 0;
    for(i=1;i<V;i++) dp[i] = INT_MAX;

    wp = rp = 0;
    queue[wp++%SHRT_MAX] = r;

    while(wp>rp) {
        from = queue[rp++%SHRT_MAX];

        for(i=0,size=node_table[from].size;i<size;i++) {
            to = node_table[from].next_node[i];
            cost = node_table[from].cost[i];

            if(cost+dp[from] < dp[to]) {
                queue[wp++%SHRT_MAX] = to;
                dp[to] = cost+dp[from];
            }
        }
    }
}

int main(void) {
	int i, n;
    for(i=0;i<100005;i++) init_node(i);

	scanf("%d\n", &n);
    for(i=0;i<n;i++) {
        int j, u, k, v, c;
        scanf("%d %d", &u, &k);
        for(j=0;j<k;j++) {
	        scanf("%d %d", &v, &c);
	        add_next_node(u, v, c);
        }
    }

    solve(0, n);

    for(i=0;i<n;i++) {
        free_node(i);
        if(dp[i] == INT_MAX) {
            printf("INF\n");
        } else {
            printf("%d %d\n", i, dp[i]);
        }
    }

    return 0;
}