#n-numar noduri
#k-acoperirea pe care vrem sa o aflam
#nod 1 -> variabile: 1, 2, 3, ..., k
#nod 2 -> variabile: k+1, k+2, k+3, ..., 2^k
#...
#nod n -> variabile: (n-1)*k + 1, (n-1)*k + 2,(n-1)*k + 3, ..., n*k

#output : (u * k + 1) V (v * k + 1) V (u * k + 2) V (v * k + 2) V … V (u * k + k) V (v * k + k)
#(1 V (k + 1) V (2 * k + 1) V … V (n-1)k + 1) ^ (1V(k + 1)) ^ (1V(2k + 1)) ^ … ^ (((n-2)k + 1) V ((n-1)* + 1))


def creare_mat(graph, muchie):               #O(n)
    for i in range(muchie):
        arc = input().split(" ")
        linie = int(arc[0])
        coloana = int(arc[1])
        mat[linie - 1][coloana - 1] , mat[coloana - 1][linie - 1] = 1, 1
    
def creare_var(n, k):                        #O(k*n)
    aux = []
    for i in range(n * k):
        aux.append(i + 1)
    return aux

#testare apartenenta fiecarei muchii din cadrul grafului la un set ales ca
#si posibila acoperire

def test1(var, k):              # un singur nod care sa apartina unei acoperiri  -> O(n*n*k)
    length = len(var)           #lenght=n*k
    aux = []
    for i in range(k):          #face un pas de k 
        aux1 = []
        for j in range(i, length, k):
            aux1.append(str(var[j]))
        aux1 = " V ".join(aux1)
        aux1 = "( " + aux1 + " )"
        aux.append(aux1)
        for j in range(i, length, k):
            for p in range(j + k, length, k):
                aux1 = "( " + str(j + 1) + " V " + str(p + 1) + " )"
                aux.append(aux1)
    return aux

def test2(graph, k):            # k noduri care sa apartina unei acoperiri  -> O(n*n*k)
    aux = []
    nr_nod = len(graph)
    for i in range(nr_nod):
        for j in range(i + 1, nr_nod):
            aux1 = []
            if mat[i][j] == 1:
                for p in range(0, k):
                    aux1.append(str((i + 1) * k - p))
                    aux1.append(str((j + 1) * k - p))
                aux.append("( " + " V ".join(aux1) + " )")
    return aux

if __name__ == "__main__":                    #O(n)
    k = int(input())
    nr_nod = int(input())
    muchie = int(input())
    mat = [([0] * nr_nod) for i in range(nr_nod)]
    
    creare_mat(mat, muchie)
    
    var = creare_var(nr_nod, k)
    SAT_1 = test1(var, k)
    SAT_1 = "^".join(SAT_1)
    SAT_2 = test2(mat, k)
    SAT_2 = "^".join(SAT_2)
    
    SAT = SAT_1 + "^" +  SAT_2     # concatenarea solutiilor obtinute
    
    print(SAT)


#Complexitate:
    #worst_case ---->> k == n
    #O(n) + O(n^2) + O(n^3) + O(n^3) + O(n) = O(n^3)

















