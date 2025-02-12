# FlyFood

## Descrição do Projeto

Este projeto resolve o problema de otimização de rotas para drones de entrega no contexto do sistema FlyFood. O objetivo é determinar o menor trajeto possível para realizar entregas em pontos designados de uma matriz, minimizando a distância total percorrida. O algoritmo utiliza a distância Manhattan para calcular o custo do trajeto e explora todas as permutações possíveis das entregas para garantir a solução ótima.

## Funcionalidades

- Leitura de uma matriz a partir de um arquivo de entrada.
- Identificação dos pontos de entrega e do ponto de origem.
- Cálculo da distância total de cada rota possível usando a distância Manhattan.
- Determinação da rota de menor custo.

## Formato da Entrada

O arquivo de entrada deve ter o seguinte formato:

```
4 5
0 0 0 0 D
0 A 0 0 0
0 0 0 0 C
R 0 B 0 0
```

- A primeira linha contém as dimensões da matriz (linhas e colunas).
- Os seguintes valores representam a matriz, onde:
  - `R` indica o ponto de origem/retorno do drone.
  - Letras (`A`, `B`, `C`, etc.) indicam os pontos de entrega.
  - `0` indica células vazias.

## Como Executar

1. **Pré-requisitos**:

   - Python 3.8 ou superior.

2. **Preparar o ambiente**:

   - Certifique-se de que o arquivo de entrada está no mesmo diretório do script Python e siga o formato descrito acima.

3. **Executar o programa**:

   - No terminal, execute:
     ```
     python src/main.py
     ```

4. **Saída esperada**:

   - A sequência de pontos a ser percorrida para minimizar a distância.
   - A distância total mínima calculada.

Exemplo:

```
Melhor rota: A D C B
Distância mínima: 12
```

## Melhorias Futuras

- Implementar algoritmos mais eficientes para casos maiores, como
  - Algoritmo de Dijkstra
  - Algoritmos aproximados para o problema do caixeiro-viajante (TSP).
  - Algoritmo Genético
- Adicionar suporte para múltiplos drones.
- Implementar uma interface gráfica para visualização das rotas.

## Outros
- [Apresentação em slides](https://www.canva.com/design/DAGc6vIOn8c/FcwysvUVlCbPgKFvCMGcTA/edit)

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests no repositório.
