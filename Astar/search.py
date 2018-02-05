import matplotlib.pyplot as plt
import networkx as nx

def load_nodes(G, visited):
    for v in visited:
        G.add_node(v)

def dist(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def load_edge_pair(visited):
    pairs = []
    for v in visited:
        neighbor_up = (v[0]-1, v[1])
        neighbor_down = (v[0]+1, v[1])
        neighbor_right = (v[0], v[1]+1)
        neighbor_left = (v[0], v[1]-1)
        if neighbor_up in visited:
            p = [v, neighbor_up]
            if [neighbor_up, v] not in pairs:
                pairs.append(p)
        if neighbor_down in visited:
            p = [v, neighbor_down]
            if [neighbor_down, v] not in pairs:
                pairs.append(p)
        if neighbor_right in visited:
            p = [v, neighbor_right]
            if [neighbor_right, v] not in pairs:
                pairs.append(p)
        if neighbor_left in visited:
            p = [v, neighbor_left]
            if [neighbor_left, v] not in pairs:
                pairs.append(p)
    return pairs

def load_edges(G, edges):
    for e in edges:
        G.add_edge(e[0], e[1])


def get_direction(cur_x, cur_y, next_x, next_y):
    if cur_x - next_x == 1:
        return "up"
    elif cur_x - next_x == -1:
        return "down"
    elif cur_y - next_y == 1:
        return "left"
    elif cur_y - next_y == -1:
        return "right"

def get_path(visited, start, goal):

    G = nx.Graph()
    edges = load_edge_pair(visited)
    load_nodes(G, visited)
    load_edges(G, edges)

    start = (start['x'], start['y'])
    goal = (goal['x'], goal['y'])

    # print "visited", visited
    # print start
    # print goal

    # back_trace_path = nx.astar_path(G, start, goal, dist)
    back_trace_path = nx.shortest_path(G, source=start, target=goal)

    G.clear()
    # print "back_path", back_trace_path

    real_path = []
    for i in xrange(len(back_trace_path)):
        p = back_trace_path[i]
        x = p[0]
        y = p[1]

        if i+1 < len(back_trace_path):
            next_p = back_trace_path[i+1]
            next_x = next_p[0]
            next_y = next_p[1]

            direct = get_direction(x, y, next_x, next_y)
            real_path.append((direct, {"x":x, "y":y}))


    # print "real_path", real_path
    return real_path
