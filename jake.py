#!/usr/bin/env python3


representation = {
    '$': 1,
    'F': 2,
    '+': 0,
    '-': 0,
    '|': 0,
    '_': 1,
    ' ': 1,
    '': 1,
    '  ':1
}

def check_adjacencies(maze, tile):
    """
        Let tile be a tuple of (row, column):
            Need to check row+-1, col
                          row, col+-1
    """
    adjacencies = []
    if representation[maze[tile[0]+1][tile[1]]]:
        #down
        adjacencies.append((tile[0]+1,tile[1], 'down'))
    if representation[maze[tile[0]-1][tile[1]]]:
        #up
        adjacencies.append((tile[0]-1,tile[1], 'up'))
    if representation[maze[tile[0]][tile[1]+1]]:
        #right
        adjacencies.append((tile[0],tile[1]+1, 'right'))
    if representation[maze[tile[0]][tile[1]-1]]:
        #left
        adjacencies.append((tile[0],tile[1]-1, 'left'))

    return adjacencies

if __name__ == "__main__":
    maze = eval(input())
    starting_index = (None, None)
    end_index = (None, None)

    for i in range(0,len(maze)):
        try:
            j = maze[i].index('$')
            starting_index = (i,j)

        except ValueError:
            continue

    for i in range(0,len(maze)):
        try:
            j = maze[i].index('F')
            end_index = (i,j)

        except ValueError:
            continue


    visited_vertices = [[0 for i in range(len(maze[0]))] for j in range(len(maze))]
    predecessors = [[None for i in range(len(maze[0]))] for j in range(len(maze))]

    visited_vertices[starting_index[0]][starting_index[1]] = 1
    vertex_queue = [starting_index]


    found = False

    #Perform Breadth First search
    while vertex_queue:
        tile = vertex_queue.pop()
        for adjacency in check_adjacencies(maze, tile):
            if(visited_vertices[adjacency[0]][adjacency[1]] == 0):
                visited_vertices[adjacency[0]][adjacency[1]] = 1
                predecessors[adjacency[0]][adjacency[1]] = (tile[0],tile[1], adjacency[2])
                vertex_queue.append(adjacency)
                if(adjacency[0] == end_index[0] and adjacency[1] == end_index[1]):
                    found = True
                    break
        if found:
            break

    path = []
    node = end_index
    while node:
        node = predecessors[node[0]][node[1]]
        if node:
            path.append(node[2])

    path = path[::-1]
    out = ""
    for string in path:
        out += string + ","
    print(out[:-1])
#[['+', '-', '+', '-', '+', '-', '+'],['|', ' ', ' ', ' ', ' ', ' ', '|'],['+', ' ', '+', '-', '+', ' ', '+'],['|', '  ', ' ', 'F', '|', ' ', '|'],['+', '-', '+', '-', '+', ' ', '+'],['|', '$', ' ', ' ', ' ', ' ', '|'],['+', '-', '+', '-', '+', '-', '+']]
