

from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
import networkx as nx

pts = []

for line in open('generes.csv').readlines():
    xs = line.split(',')
    x = int(xs[1])
    y = int(xs[2])
    pts.append([x, y])

tri = Delaunay(pts)

def w(u, v, pts):
    dx = pts[u][0] - pts[v][0]
    dy = pts[u][1] - pts[v][1] 
    return (dx * dx + dy * dy) ** 0.5 

g = nx.Graph()

for simplex in tri.simplices:
    x, y, z = tuple(simplex)
    g.add_edge(x, y, weight = w(x, y, pts))
    g.add_edge(y, z, weight = w(y, z, pts))
    g.add_edge(z, x, weight = w(z, x, pts))

mst = nx.minimum_spanning_tree(g)

nx.draw(g, pos = pts, node_size= 0.01, edge_color='gray')
nx.draw(mst, pos = pts, node_size= 0.01, edge_color='red')
plt.show() 



