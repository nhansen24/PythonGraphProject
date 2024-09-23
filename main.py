import csv
from math import sqrt, inf
# from random import randint, randrange
from heapq import heappush, heappop
# from Graph import Graph, ManhattanGraph

# Consider implementing graph, A*, Dijkstras, etc... for practice with vertices and edge weights
# Initial thoughts, it would be interesting to create an euclidian graph for navigating Seattle?
# STATUS working partially, only connects two closest neighbors during build_graph() which creates a
# disconnected graph between areas like West Seattle and Downtown. Revise to connect to closest neighbor in
# each cardinal direction within a range or by selectively connecting certain vertices...


def heuristic(a, b, points):
    x1, y1 = points[a]
    x2, y2 = points[b]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2) * 69


def a_star(graph, start, target, points):
    count = 0
    path_distances = {}
    # Initialize each vertex weight /  distance as inf
    for vertex in graph:
        path_distances[vertex] = [inf, [start]]
    # Sets start vertex weight to 0
    path_distances[start][0] = 0
    vertices_to_visit = [(0, start)]
    # Loops while path to target not found
    while vertices_to_visit and path_distances[target][0] == inf:
        current_distance, current_vertex = heappop(vertices_to_visit)
        # Iterate through neighboring vertexes and determine the shortest path to target
        for neighbor, edge_weight in graph[current_vertex]:
            new_distance = current_distance + edge_weight + heuristic(neighbor, target, points)
            new_path = path_distances[current_vertex][1] + [neighbor]
            # If a shorter path is found from the current_vertex to target reassign new_distance new_path
            if new_distance < path_distances[neighbor][0]:
                path_distances[neighbor][0] = new_distance
                path_distances[neighbor][1] = new_path
                heappush(vertices_to_visit, (new_distance, neighbor))
                count += 1
    # OR clause prevents listing start or target as the attractions between
    if path_distances[target][0] == inf or len(path_distances[target][1]) < 3:
        print(f'No Attractions found between {start} and {target}')
        return []

    print(f'\n============================================\n\nHere are Attractions between {start} and {target}:')
    route = []
    for path1 in path_distances[target][1]:
        route.append(path1)
    for i in range(1, len(route) - 2):
        print(f'{route[i]}', end='    ')

    return path_distances[target][1]


def build_graph():
    points = {}
    with open('seattle.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            name = str(row[0])
            x = float(row[1])
            y = float(row[2])
            points[name] = (x, y)

    seattle_graph = {}

    for id1, (x1, y1) in points.items():
        seattle_graph[id1] = []
        distances = []
        for id2, (x2, y2) in points.items():
            if id1 != id2:
                distance = sqrt((x2 - x1)**2 + (y2 - y1)**2) * 69
                distances.append((id2, distance))
        distances.sort(key=lambda i: i[1])
        # Every vertex is a key = [(neighbor, distance), (neighbor2, distance2)]
        seattle_graph[id1] = distances[:2]          # THIS NEEDS TO BE MODIFIED TO BETTER CONNECT THE GRAPH
    # Test that prints every node and the two closest neighbors & their distance. TEST SORT
    '''
    for node, edges in seattle_graph.items():
        print(f'\n{node}: ')
        for edge in edges:
            print(f'    {edge[0]}: {edge[1]:.2f} miles')
    '''
    return seattle_graph, points


# Initialize the graph from the CSV
seattle_graph1, points1 = build_graph()


# Prints available start and target locations. Seperated by ' // '
def get_locations():
    sorted_locations = sorted(seattle_graph1.keys(), key=lambda i: i[0])
    for name in sorted_locations:
        print(f'{name}', end=' // ')


# Starts the program off with an intro and query the user for start and target locations
def welcome():
    print('\n\nWelcome to Seattle')
    input('\nPress enter to continue')
    print('\nHere is a list of popular locations:\n')
    # Prints possible inputs for locations
    get_locations()
    start_location = input('\n\nWhat is your starting location? ')
    target_location = input('\nWhere would you like to go? ')
    # Submits the user inputs as arguments into a_star() for finding en-route attractions
    # Passes in points1 (x,y) returned by build_graph() for use in a_star() heuristic function.
    path = a_star(seattle_graph1, start_location, target_location, points1)
    return start_location, target_location


# Calls the start function.
start_location1, target_location1 = welcome()

# Loop for checking additional routes
again = input('\nWould you like to visit another location? (y/n) ')
while again == 'y':
    start_location2, target_location2 = welcome()
    again = input('\nWould you like to visit another location? (y/n) ')
