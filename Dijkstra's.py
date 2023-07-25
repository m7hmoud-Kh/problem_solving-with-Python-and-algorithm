graph = {
    'start': {'a':5,'b':2},
    'a':{'d':4,'c':2},
    'b':{'a':8,'c':7},
    'd':{'c':6,'f':3},
    'c':{'f':1},
    'f':{}
}
infinity = float("inf")
costs = {
    'a':5,
    'b':2,
    'c': infinity,
    'd': infinity,
    'f': infinity
}

parents = {
    'a':'start',
    'b': 'start',
    'c': None,
    'd': None,
    'f': None
}

procced = []

def find_lowest_cost_node(costs):
    lowest_node = None
    lowest_node_cost = infinity

    for node in costs:
        cost = costs[node]

        if cost < lowest_node_cost and node not in procced:
            lowest_node = node
            lowest_node_cost = cost
    return lowest_node

node = find_lowest_cost_node(costs)

while node is not None:

    cost = costs[node]
    neighboor = graph[node]

    for n in neighboor.keys():
        new_cost = cost + neighboor[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    procced.append(node)
    node = find_lowest_cost_node(costs)

print(costs)
print(parents)





