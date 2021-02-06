import sys
import math
import time
import graphUI
from node_color import white, yellow, black, red, blue, purple, orange, green
"""
Feel free print graph, edges to console to get more understand input.
Do not change input parameters
Create new function/file if necessary
"""
# Hàm tô màu các đỉnh khi chương trình kết thúc
def fillNode(graph, vertex, start, goal):
    graph[vertex][3] = yellow
    graph[start][3] = orange
    graph[goal][3] = purple
    graphUI.updateUI()

# Hàm tạo mảng mark_path = -1
def initVertexCrossed(graph, path):
    for i in range(len(graph)):
        path.append(-1)
#Hàm tô màu đường đi
def colorPath(mark_path, path, edges, edge_id, start, goal):
    for i in range(len(mark_path)):
        for j in range(len(mark_path)):
            if j == goal:
                path.append(goal)
                goal = mark_path[j]
                break
        if goal == start:
            path.append(start)
            break
    for i in range(len(path) - 1):
        edges[edge_id(path[i], path[i + 1])][1] = green
    graphUI.updateUI()
#Hàm lấy chi phí của giữa 2 đỉnh theo khoảng cách trên trục tọa độ
def getWeight(graph, a, b):
    (x1, y1) = graph[a][0]
    (x2, y2) = graph[b][0]
    dist = math.sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))
    return dist
    pass
# Sắp xếp bộ đỉnh, đường đi từ gốc tới đỉnh tăng dần
def sortTuple(tup):
    for i in range(len(tup)):
        for j in range(len(tup)):
            if tup[i][1] < tup[j][1]:
                temp = tup[i]
                tup[i] = tup[j]
                tup[j] = temp
# Hàm heuristic chi phí tới đỉnh gốc của mỗi đỉnh theo đường "chim bay"
def initWeighAF(graph, weight, goal):
    for i in range(len(graph)):
        weight.append(i)
    for i in range(len(graph)):
        if i != goal:
            weight[i] = getWeight(graph, i, goal)



def BFS(graph, edges, edge_id, start, goal):
    """
    BFS search
    """
    # TODO: your code
    k = 0
    mark_path = [] #mảng lấy vết đường đi
    initVertexCrossed(graph, mark_path) # hàm khởi tạo mả_path = -1
    queue = [] # stack2: lưu đỉnh chờ duyệt
    queueNode = [] #stack1: lưu những đỉnh đã duyệt qua
    queue.append(start)
    while(len(queue) !=0):
        vertex = queue[0]
        queue.remove(queue[0]) # Xóa đỉnh đầu sau mỗi lần duyệt
        queueNode.append(vertex)
        graph[vertex][3] = yellow
        node_1 = graph[vertex]
        for adjacency_node in node_1[1]:
            if adjacency_node not in queueNode: #queueNode kiểm tra đỉnh đã có trong danh sách chưa?
                queue.append(adjacency_node) #Thêm vào nếu chưa có trong danh sách
                graph[adjacency_node][3] = red # Tô màu đỉnh duyệt đến
                mark_path[adjacency_node] = vertex #Đánh dấu dường đi của các đỉnh
                edges[edge_id(vertex, adjacency_node)][1] = white #Tô màu cạnh đã duyệt qua
            queueNode.append(adjacency_node)
            graphUI.updateUI()
            time.sleep(.1)
            if goal in queue:
                k = 1
                break
        graphUI.updateUI()
        time.sleep(1)
        graph[vertex][3] = blue
        if k == 1:
            break
    fillNode(graph, vertex, start, goal) # Hàm tô màu đỉnh sau khi kết thúc duyệt
    path = []
    colorPath(mark_path, path, edges, edge_id, start, goal) #Tô mày đường đi
    print("Implement BFS algorithm.")
    pass

def DFS(graph, edges, edge_id, start, goal):
    """
    DFS search
    """
    # TODO: your code
    pos = -1

    k = 0
    mark_path = []
    initVertexCrossed(graph, mark_path)
    stack = []
    queueNode = []
    stack.append(start)
    while (stack):
        vertex = stack.pop() #Lấy đỉnh cuối ra để duyệt đồng thời xóa khỏi stack
        queueNode.append(vertex)
        graph[vertex][3] = yellow
        node_1 = graph[vertex]
        time.sleep(.3)
        for adjacency_node in node_1[1]:
            if adjacency_node not in queueNode:
                stack.append(adjacency_node)
                graph[adjacency_node][3] = red
                mark_path[adjacency_node] = vertex
                edges[edge_id(vertex, adjacency_node)][1] = white
            queueNode.append(adjacency_node)
            graphUI.updateUI()
            if goal in stack:
                k = 1
                break
        time.sleep(1)
        graph[vertex][3] = blue
        if k == 1:
            break
    fillNode(graph, vertex, start, goal)
    path = []
    colorPath(mark_path, path, edges, edge_id, start, goal)
    print("Implement DFS algorithm.")
    pass

def UCS(graph, edges, edge_id, start, goal):
    """
    Uniform Cost Search search
    """
    # TODO: your code
    k = 0
    mark_path = []
    initVertexCrossed(graph, mark_path)
    queue = []
    queueNode = []
    a = (start, 0)
    queue.append(a)
    while (len(queue) != 0): #Kiểm tra stack rỗng thì ngưng
        vertex = queue[0]
        queue.remove(queue[0])
        queueNode.append(vertex[0])
        graph[vertex[0]][3] = yellow
        node_1 = graph[vertex[0]]
        for adjacency_node in node_1[1]:
            if adjacency_node not in queueNode:
                a = int(getWeight(graph, vertex[0], adjacency_node))#Chi phí từ đỉnh gốc tới đỉnh kề đang xét
                queue.append((adjacency_node, a + vertex[1]))#Bộ đỉnh, chi phí đường đi giữa 2 đỉnh
                graph[adjacency_node][3] = red
                mark_path[adjacency_node] = vertex[0]
                edges[edge_id(vertex[0], adjacency_node)][1] = white
            sortTuple(queue)
            queueNode.append(adjacency_node)
            time.sleep(.1)
            graphUI.updateUI()
            if goal == adjacency_node:
                k = 1
                break
        graphUI.updateUI()
        time.sleep(1)
        graph[vertex[0]][3] = blue
        if k == 1:
            break
    fillNode(graph, vertex[0], start, goal)
    path = []
    colorPath(mark_path, path, edges, edge_id, start, goal)
    print("Implement Uniform Cost Search algorithm.")
    pass

def AStar(graph, edges, edge_id, start, goal):
    """
    A star search
    """
    # TODO: your code

    weight = []
    wei1 = 0
    initWeighAF(graph, weight, goal)
    k = 0
    mark_path = []
    initVertexCrossed(graph, mark_path)
    queue = []
    queueNode = []
    a = (start, 0)
    queue.append(a)
    while (len(queue) != 0):
        vertex = queue[0]
        queue.remove(queue[0])
        queueNode.append(vertex[0])
        graph[vertex[0]][3] = yellow
        node_1 = graph[vertex[0]]
        for adjacency_node in node_1[1]:
            if adjacency_node not in queueNode:
                a = int(getWeight(graph, vertex[0], adjacency_node))#Chi phí từ đỉnh gốc tới đỉnh kề đang xét
                b = int(weight[adjacency_node]) # Heuristic chi phí từ đỉnh kề đang xét tới đích
                # Bộ đỉnh, chi phí đường đi giữa 2 đỉnh và chi phí từ đỉnh đó tới đích
                queue.append((adjacency_node, a + b + vertex[1]))
                graph[adjacency_node][3] = red
                mark_path[adjacency_node] = vertex[0]
                edges[edge_id(vertex[0], adjacency_node)][1] = white
            sortTuple(queue)
            queueNode.append(adjacency_node)
            graphUI.updateUI()
            time.sleep(.1)
            if goal == adjacency_node:
                k = 1
                break
        graphUI.updateUI()
        time.sleep(1)
        graph[vertex[0]][3] = blue
        if k == 1:
            break
    fillNode(graph, vertex[0], start, goal)
    path = []
    colorPath(mark_path, path, edges, edge_id, start, goal)
    print("Implement A* algorithm.")
    pass


def GBF(graph, edges, edge_id, start, goal):
    """
    A star search
    """
    # TODO: your code

    weight = []
    wei1 = 0
    initWeighAF(graph, weight, goal)
    k = 0
    mark_path = []
    initVertexCrossed(graph, mark_path)
    queue = []
    queueNode = []
    a = (start, 0)
    queue.append(a)
    while (len(queue) != 0):
        vertex = queue[0]
        queue.remove(queue[0])
        queueNode.append(vertex[0])
        graph[vertex[0]][3] = yellow
        node_1 = graph[vertex[0]]
        for adjacency_node in node_1[1]:
            if adjacency_node not in queueNode:
                b = int(weight[adjacency_node]) # Heuristic chi phí từ đỉnh kề đang xét tới đích
                # Bộ đỉnh, chi phí đường đi từ đỉnh đó tới đích
                queue.append((adjacency_node, b))
                graph[adjacency_node][3] = red
                mark_path[adjacency_node] = vertex[0]
                edges[edge_id(vertex[0], adjacency_node)][1] = white
            sortTuple(queue)
            queueNode.append(adjacency_node)
            graphUI.updateUI()
            time.sleep(.1)
            if goal == adjacency_node:
                k = 1
                break
        graphUI.updateUI()
        time.sleep(1)
        graph[vertex[0]][3] = blue
        if k == 1:
            break
    fillNode(graph, vertex[0], start, goal)
    path = []
    colorPath(mark_path, path, edges, edge_id, start, goal)
    print("Implement Greedy Best-First Search algorithm.")
    pass

def example_func(graph, edges, edge_id, start, goal):
    """This function is just show some basic feature that you can use your project.
    @param graph: list - contain information of graph (same value as global_graph)
                    list of object:
                     [0] : (x,y) coordinate in UI
                     [1] : adjacent node indexes
                     [2] : node edge color
                     [3] : node fill color
                Ex: graph = [
                                [
                                    (139, 140),             # position of node when draw on UI
                                    [1, 2],                 # list of adjacent node
                                    (100, 100, 100),        # grey - node edged color
                                    (0, 0, 0)               # black - node fill color
                                ],
                                [(312, 224), [0, 4, 2, 3], (100, 100, 100), (0, 0, 0)],
                                ...
                            ]
                It means this graph has Node 0 links to Node 1 and Node 2.
                Node 1 links to Node 0,2,3 and 4.
    @param edges: dict - dictionary of edge_id: [(n1,n2), color]. Ex: edges[edge_id(0,1)] = [(0,1), (0,0,0)] : set color
                    of edge from Node 0 to Node 1 is black.
    @param edge_id: id of each edge between two nodes. Ex: edge_id(0, 1) : id edge of two Node 0 and Node 1
    @param start: int - start vertices/node
    @param goal: int - vertices/node to search
    @return:
    """
    # Ex1: Set all edge from Node 1 to Adjacency node of Node 1 is green edges.
    node_1 = graph[1]
    for adjacency_node in node_1[1]:
        edges[edge_id(1, adjacency_node)][1] = green
    graphUI.updateUI()
    #Ex2: Set color of Node 2 is Red
    graph[1][3] = red
    graphUI.updateUI()
    # # Ex3: Set all edge between node in a array.
    # path = [4, 7, 9]  # -> set edge from 4-7, 7-9 is blue
    # for i in range(len(path) - 1):
    #     edges[edge_id(path[i], path[i + 1])][1] = blue
    # graphUI.updateUI()
