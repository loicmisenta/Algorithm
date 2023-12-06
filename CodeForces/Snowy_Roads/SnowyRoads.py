from collections import defaultdict
from heapq import *

def main(edges, f, t, n, m):
    if f == t or (n == 1 and m == 0):
        print("{} {}".format(0, 0))
        return 0
    min_snow = dijkstra_snow(edges, f, t)[0]
    print(min_snow)

    edges_with_min_snow = []
    for i in range(len(edges)):
        if(edges[i][3] <= min_snow):
            edges_with_min_snow.append(edges[i])
    
    cost = dijkstra(edges_with_min_snow, f, t)[0]
    if(cost >= float("inf")):
        print("Impossible")
    else:
        print("{} {}".format(min_snow, cost))
    return cost


def dijkstra_snow(edges, f, t):
    g = defaultdict(list)
    for l,r,c,snow in edges:
        g[l].append((snow,r))
        g[r].append((snow,l))
    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = max(cost, c)
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf"), None 



#relancer sans les edges plus grande que le resultat trouver


def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c,s in edges:
        g[l].append((c,r))
        g[r].append((c,l))

    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf"), None

if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]
    edges_with_snow = [
        ["A","C",1,3],
        ["A","B",10,1],
        ["B","C",10,2]
    ]


def inlt():
    return(list(map(int,input().split())))


firstLine = inlt()

n = firstLine[0] # Number of intersection
m = firstLine[1] # Number of intact road
s = firstLine[2] # start
t = firstLine[3] # end

edges = [] # List of [post number, dest, dog food, gasoline]

for i in range(m):
    edges_i = inlt()
    edges.append(edges_i)

main(edges, s, t, n, m)