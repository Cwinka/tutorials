from graph import Graph, Vertex
from queue import PriorityQueue
from math import sqrt
import random
def dfs(graph, current_vertex, target_value, visited = None):
  if visited is None:
    visited = []
  visited.append(current_vertex)
  if current_vertex is target_value:
    return visited

  for neighbor in graph[current_vertex].edges:
    if neighbor not in visited:
      path = dfs(graph, neighbor, target_value, visited)
      if path:
          return path
      else:
          return None

def hevristic(graph, current_vertex, end_vertex):
    return (abs(graph[end_vertex].position[0]-graph[current_vertex].position[0]) +
            abs(graph[end_vertex].position[1]-graph[current_vertex].position[1]))

def best_first(graph, start_vertex, target_value):
    path = [start_vertex]
    vertex_and_path = [0, start_vertex, path]
    bfs_queue = PriorityQueue()
    bfs_queue.put(vertex_and_path)
    visited = set()
    while bfs_queue:
        h, current_vertex, path = bfs_queue.get_nowait()
        visited.add(current_vertex)
        for neighbor in graph[current_vertex].edges:
            if neighbor not in visited:
                if neighbor == target_value:
                    return path + [neighbor]
                else:
                    h = hevristic(graph, neighbor, target_value)
                    bfs_queue.put([h, neighbor, path + [neighbor]])


gr = Graph()
def matrix(size, flag=False):
    ll = range(1,size**2+1)
    x, y = 1, 1
    for i in ll:
        gr.add_vertex(Vertex(i,(x,y)))
        x += 1
        if x > size:
            x = 1
            y += 1

    for i in gr.graph_dict:
        if i+1 in ll:
            if i%size==0:
                pass
            else:
                gr.add_edge(gr.graph_dict[i], gr.graph_dict[i+1])
        if i-1 in ll:
            if (i-1)%size==0:
                pass
            else:
                gr.add_edge(gr.graph_dict[i], gr.graph_dict[i-1])

        if i+size in ll:
            gr.add_edge(gr.graph_dict[i], gr.graph_dict[i+size])
        if i-size in ll:
            gr.add_edge(gr.graph_dict[i], gr.graph_dict[i-size])

        # if flag is True:
            # if (i + size +1) in ll:
            #     gr.add_edge(gr.graph_dict[i], gr.graph_dict[i+size+1])
            # if (i - size -1) in ll:
            #     gr.add_edge(gr.graph_dict[i], gr.graph_dict[i-size-1])
            # if (i - size +1) in ll:
            #     gr.add_edge(gr.graph_dict[i], gr.graph_dict[i-size+1])
            # if (i + size -1) in ll:
            #     gr.add_edge(gr.graph_dict[i], gr.graph_dict[i+size-1])








def print_graph(graph):
    for vertex in graph.graph_dict:
        print("")
        print(str(vertex) + " connected to")
        vertex_neighbors = graph.graph_dict[vertex].edges
        if len(vertex_neighbors) == 0:
            print("No edges!")
        for adjacent_vertex in vertex_neighbors:
            try:
                path = graph.graph_dict[vertex].edges[adjacent_vertex]
                print(f"=> {adjacent_vertex} path:{path}")
            except KeyError:
                print(f"=> {adjacent_vertex}")





matrix(5)
# print_graph(gr)
# gr.del_vertex(18)
gr.del_vertex(14)
print(best_first(gr, 1, 25))
