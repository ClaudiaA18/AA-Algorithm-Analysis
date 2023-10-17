#include <stdio.h>
#include <stdlib.h>

//definim structura muchiei
typedef struct muchie{
	int u, v;
};

//G=(V,E), n=card(V), m=card(E) 
//graf[100][100] -> matrice de adiacenta
//O(n)*O(n^2) + O(n^2)*O(n^2) = O(n^4)
int functie_verificare(int graf[100][100], muchie E[100], int n, int m, int numar[100]){
	for (int i = 1; i < n; i++) //O(n)
		for (int j = i+1; j <= n; j++) //O(n^2)
			if (numar[i] == numar[v])
				return 0;
			else	
				return 1;
			
	for (int i = 1; i < m; i++){ // O(n^2) 
		int dif1 = numar[E[i].u] - numar[E[i].v];
		if (dif1 < 1 || dif1 > m)
			for (int j = i+1; j <= m; j++){ //O(n^2)
				dif2 = numar[E[j].u] - numar[E[j].v];
				if (dif1 == dif2)
					return 0;
				else
					return 1;
			}
	}
}

// O(n^4) + O(k^n) = O(k^n)
int functie_backtracking(int graf[100][100], muchie E[100], int n, int m, int numar[100][100], int k){ 
	int i;
	if (k == n){
		if (functie_verificare(graf, E, n, m, numar) == 1) // O(n^4)
			return 1;
		else
			return 0;
		i = 0;
		while(i < n) {
			numar[k] = i;
			
			if (functie_backtracking(g, E, n, m, numar, k+1) == 1){ //O(k^n)
				return 1;
				numar[i] = 0;
				i++
			}
			else
				return 0;
		}	
}

//O(n)*O(n) + O(n^2) = O(n^n) --> COMPLEXITATE ALGORITM: O(n^n)
int main()
{
	int graf[100][100], n, m, numar[100];
	muchie E[100]; 
	scanf("%d", &n);
	scanf("%d", &m);

	for (i = 1; i <= n; i++){ //O(n)
		for (j = 1; j <= n; j++) //O(n)
			graf[i][j] = 0;
		numar[i] = 0;
	}

	for (i = 1; i <= m; i++){ //O(n^2)
		scanf("%d", &E[i].u); 
		scanf("%d", &E[i].v);
	}
	
	for (i = 1; i <= m; i++){
		graf[E[i].u][E[i].v] = 1;
		graf[E[i].v][E[i].u] = 1;
	}

	bt(g, E, n, m, numar, 1); //O(1)

	return 0;
}