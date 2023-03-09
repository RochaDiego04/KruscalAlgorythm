edges = [
    (1, 2, 5),  # Nodo 1 conectado a nodo 2 con peso de 5
    (1, 3, 1),
    (2, 3, 2),
    (2, 4, 6),
    (3, 4, 4)
]


# Deberemos mantener un conjunto de conjuntos, cada conjunto es una componente conexa en el grafo. Componente conexa
# es una partición del grafo que es conexa, es decir que todos los vertices se puedan unir en un solo camino

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        # n es el num de nodos del grafo
        # parent y rank son listas que representan la estructura de datos disjuntos.
        # parent[i] seria el padre del elemento i, rank es la altura del arbol enraizado en i

    def find(self, x):  # Devuelve representante del conjunto que contiene el elemento dado, usamos "comprensión de
        # caminos"
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):  # Une los 2 conjuntos que contienen los elementos dados, usamos la "union por rango"
        px, py = self.find(x), self.find(y)
        if px != py:  # Los nodos que se vayan a unir deben ser distintos
            if self.rank[px] < self.rank[py]:
                px, py = py, px
            self.parent[py] = px
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1


def kruskal(n, edges):  # n numero de nodos del grafo, edges es una lista de aristas
    dsu = DisjointSet(n)
    edges = sorted(edges, key=lambda e: e[2])  # Ordenamos segun el tercer elemento, es decir el peso
    tree = []
    for u, v, w in edges:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            tree.append((u, v, w))  # Si la arista no forma un ciclo, la agregamos al arbol resultante
    return tree


def print_tree(tree):
    for u, v, w in tree:
        print(f"{u} -- {v}, peso {w}")


tree = kruskal(5, edges)
print_tree(tree)