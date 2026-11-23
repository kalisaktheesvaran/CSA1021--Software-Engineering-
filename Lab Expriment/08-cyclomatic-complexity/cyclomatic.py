"""Cyclomatic complexity of a flow graph.  V(G) = E - N + 2P  (P = connected components = 1)
Also cross-checked with V(G) = (number of decision nodes) + 1."""
# Flow graph of: read n; if n<0 print error; else sum=0,i=1; while i<=n: if i even sum+=i; i++; print sum
def complexity(nodes, edges, p=1):
    return len(edges) - len(nodes) + 2*p
if __name__ == "__main__":
    # Corrected graph: node 5 = while test, 6 = even-check, 7 = sum+=i, 8 = i++
    nodes = [1,2,3,4,5,6,7,8,9,10]
    edges = [(1,2),(2,3),(2,4),(4,5),(5,6),(5,9),(6,7),(6,8),(7,8),(8,5),(3,10),(9,10)]
    E, N = len(edges), len(nodes)
    print(f"Nodes N = {N}, Edges E = {E}")
    print(f"V(G) = E - N + 2 = {complexity(nodes, edges)}")
    out = {}
    for a,_ in edges: out[a] = out.get(a,0)+1
    decisions = [n for n,c in out.items() if c>1]
    print(f"Decision nodes = {decisions} -> V(G) = {len(decisions)} + 1 = {len(decisions)+1}")
    print("Independent paths = V(G) =", complexity(nodes, edges))
