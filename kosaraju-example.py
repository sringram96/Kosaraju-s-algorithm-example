import random
import math
#kosarajus algorithm computes the metagraph of G, this is a very useful
#algorithm that runs in linear time (calls modified DFS twice) and can be used to collect
#incredible amounts of data from a graph

#function generates radnom graph
def gengraph( n, p ):
    matrix = [[0 for i in range(n)] for j in range(n)];
    for i in range(n):
        for j in range(n):
            q = random.random()
            if(q<p):
                matrix[i][j] = 1
                matrix[j][i] = 1
    return(matrix)
#recursive visted algorithm visits every node in the graph
#using DFS, Once the algorithm has visited every child node, it puts the parent node into a list called L
def Visit(u, visitt, G, L):
    if(visitt[u] == False):
        visitt[u] = True
        for i in range(len(G)):
            if(G[u][i] == 1 and visitt[i] == False):
                Visit(i, visitt, G , L)
        L.append(u)
#Assignment prints all nodes belonging to an SCC     
def Assignment(u, v, assigned, G):
    assigned[u] = True
    #print the child node with every souce node, this displays each scc on
    #an independent line
    print(u, end = ' ')
    for i in range(len(G)):
        if(G[u][i] == 1 and assigned[i] == False):
            Assignment(i, u, assigned, G)
                
if __name__ == "__main__":
    G = gengraph(5, 0.5)
    V = [i for i in range(len(G))]
    visited = [False for i in range(len(G))]
    L = []
    for i in range(len(G)):
        Visit(i, visited, G, L)
    #reverse the graph
    RG = [[2 for i in range(len(G))] for j in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if(G[i][j] == 1):
                RG[i][j] = 0
            else:
                RG[i][j] = 1    
    assigned = [False for i in range(len(RG))]
    print("the vertices that make up the SCC's in the graph are")
    for i in L:
        if(assigned[i] == False):
            Assignment(i, i, assigned, RG)
            print()
    