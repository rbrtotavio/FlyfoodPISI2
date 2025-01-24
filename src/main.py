import itertools
from typing import Dict, Tuple, Optional, List

def load_matrix(file_path: str) -> Tuple[Dict[str, Tuple[int, int]], Optional[Tuple[int, int]]]:
    """Lê os pontos de interesse e o ponto inicial diretamente de um arquivo.
    
    Args:
        file_path (str): Caminho para o arquivo contendo a matriz.
        
    Returns:
        Tuple[Dict[str, Tuple[int, int]], Optional[Tuple[int, int]]]:
        Um dicionario de pontos de interesse com suas coordenadas e a posição inicial, caso exista.
    """
    points: Dict[str, Tuple[int, int]] = {}
    start: Optional[Tuple[int, int]] = None

    with open(file_path, 'r') as file:
        rows, cols = map(int, file.readline().split())

        i = 0
        while i < rows:
            line = file.readline().strip()
            if not line:
                break
            
            cells = line.split()
            j = 0
            while j < cols:
                cell = cells[j]
                if cell == 'R':
                    start = (i, j)
                elif cell != '0':
                    points[cell] = (i, j)
                j += 1
            i += 1

    return points, start

def dist_manhattan(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    """Calcula a distância Manhattan entre dois pontos.
    
    Args:
        p1 (Tuple[int, int]): Coordenadas do primeiro ponto.
        p2 (Tuple[int, int]): Coordenadas do segundo ponto.
        
    Returns:
        int: A distância Manhattan entre os dois pontos.
    """
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def find_best_route(points: Dict[str, Tuple[int, int]], start: Optional[Tuple[int, int]]) -> Tuple[Tuple[str], float | int]:
    """Encontra a rota ótima usando força bruta com pequenas otimizações.
    
    Args:
        points: Dict[str, Tuple[int, int]]: Dicionário de pontos dos pontos de interesse e suas coordenadas.
        start: Optional[Tuple[int, int]]: Posição inicial
    
    Returns:
        Tuple[Tuple[str], float | int]: Uma tupla contendo a ordem da rota e um numeral representando o custo da rota.
    """
    deliveries: List[str] = list(points.keys())
    dist_min: float | int = float('inf')
    best_route: Tuple[str] = None

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