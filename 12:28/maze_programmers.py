def print_road_map(road_map):
    for i in range(len(road_map)):
        print(road_map[i])
    return 0

def set_data_on_road_map(road_map, road):
    head = road[0]
    tail = road[1]
    long = road[2]
    road_map[head][tail] = long

def solution(n, start, end, roads, traps):
    road_map = [[0 for row in range(n+1)] for col in range(n+1)]
    for road in roads:
        set_data_on_road_map(road_map, road)
    print_road_map(road_map)
    answer = 0
    return answer

solution(3 ,1, 3, [[1, 2, 2],[3, 2, 3]], [2])