import time
import matplotlib.pyplot as plt
from main import load_matrix, find_best_route
from typing import List

def experiments(file_paths: List[str]):
    """Executa experimentos e plota os resultados."""
    matrix_sizes = []
    execution_times = []

    for file_path in file_paths:
        points, start = load_matrix(file_path)
        num_points = len(points)

        start_time = time.time()
        best_route, dist_min = find_best_route(points, start)
        end_time = time.time()

        execution_time = end_time - start_time

        matrix_name = file_path.split('/')[-1].split('_')[0]
        matrix_sizes.append(matrix_name)
        execution_times.append(execution_time)

        print(f"Arquivo: {file_path}")
        print(f"Pontos: {num_points}")
        print(f"Melhor Rota: {best_route}")
        print(f"Tempo: {execution_time:.2f}s | Distância: {dist_min}\n")
        
    plt.figure(figsize=(10, 6))
    
    bars = plt.bar(matrix_sizes, execution_times, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
    
   
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}s',
                ha='center', va='bottom')

    
    plt.title('Comparação do Tempo de Execução entre Matrizes', fontsize=14, pad=20)
    plt.xlabel('Dimensões da Matriz', fontsize=12)
    plt.ylabel('Tempo de Execução (segundos)', fontsize=12)
    plt.xticks(fontsize=11)
    plt.yticks(fontsize=11)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.savefig('execution_time_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    file_paths = [
        "src/inputs/4x5_matrix.txt",
        "src/inputs/7x5_matrix.txt",
        "src/inputs/10x10_matrix.txt"
    ]
    experiments(file_paths)