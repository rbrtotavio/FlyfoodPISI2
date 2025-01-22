import itertools

def load_matrix(file_path):
    """Lê os pontos de interesse e o ponto inicial diretamente de um arquivo."""
    points = {}
    start = None

    with open(file_path, 'r') as file:
        rows, _ = map(int, file.readline().split())  
        for i, line in enumerate(file):
            for j, cell in enumerate(line.split()):
                if cell == 'R':
                    start = (i, j)
                elif cell != '0':
                    points[cell] = (i, j)

    return points, start

def dist_manhattan(p1, p2):
    """Calcula a distância Manhattan entre dois pontos."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def calc_route_dist(route, points, start):
    """Calcula a distância total de uma rota usando a distância Manhattan."""
    dist = sum(
        dist_manhattan(points[route[i - 1]], points[point])
        for i, point in enumerate(route)
        if i > 0
    )
    dist += dist_manhattan(start, points[route[0]])
    dist += dist_manhattan(points[route[-1]], start)

    return dist

def find_best_route(points, start):
    """Encontra a rota ótima usando força bruta com pequenas otimizações."""
    deliveries = list(points.keys())
    dist_min = float('inf')
    best_route = None

    for perm in itertools.permutations(deliveries):
        dist = 0
        current_position = start
        for point in perm:
            dist += dist_manhattan(current_position, points[point])
            current_position = points[point]
            if dist >= dist_min:
                break
        dist += dist_manhattan(current_position, start)

        if dist < dist_min:
            dist_min = dist
            best_route = perm

    return best_route, dist_min

if __name__ == "__main__":
    file_path = "src/inputs/matrix.txt"
    points, start = load_matrix(file_path)

    best_route, dist_min = find_best_route(points, start)

    print("Melhor rota:", " ".join(best_route))
    print("Distância mínima:", dist_min)