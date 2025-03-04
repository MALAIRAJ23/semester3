def prims(v, e):
    sel = [False] * v
    sel[0] = True
    mst = []
    total_cost = 0
    print("\nPrim's Algorithm:")
    while len(mst) < v - 1:
        min_e = (None, None, float('inf'))
        for u, w, wt in e:
            u -= 1
            w -= 1
            if sel[u] and not sel[w] and wt < min_e[2]:
                min_e = (u, w, wt)
            elif sel[w] and not sel[u] and wt < min_e[2]:
                min_e = (w, u, wt)
        mst.append(min_e)
        sel[min_e[1]] = True
        total_cost += min_e[2]
        print(min_e[0] + 1, "--", min_e[1] + 1, "Weight", min_e[2])
    print("Total cost:", total_cost)
    return mst, total_cost

def kruskals(v, e):
    p = list(range(v))
    def find(n):
        if p[n] == n:
            return n
        p[n] = find(p[n])
        return p[n]
    def union(u, w):
        r1 = find(u)
        r2 = find(w)
        if r1 != r2:
            p[r1] = r2
    e = [(u - 1, w - 1, wt) for u, w, wt in e]
    e.sort(key=lambda x: x[2]) 
    mst = []
    total_cost = 0
    print("\nKruskal's Algorithm:")    
    for u, w, wt in e:
        if find(u) != find(w):
            mst.append((u, w, wt))
            union(u, w)
            total_cost += wt
            print(u + 1, "--", w + 1, "Weight", wt)
    print("Total cost:", total_cost)
    return mst, total_cost

def main():
    print("Enter the number of vertices and edges:")
    v = int(input("Vertices: "))
    ec = int(input("Edges: "))
    e = []
    print("Enter edges (u, w, wt):")
    for _ in range(ec):
        u, w, wt = map(int, input().split())
        e.append((u, w, wt))
    while True:
        print("\nMenu:")
        print("1. Run Prim's Algorithm")
        print("2. Run Kruskal's Algorithm")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            prims(v, e)
        elif choice == 2:
            kruskals(v, e)
        elif choice == 3:
            print("Exiting!")
            break
        else:
            print("Enter a valid choice")
main()