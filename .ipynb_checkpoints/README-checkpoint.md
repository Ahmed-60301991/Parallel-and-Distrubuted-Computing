### SEQUENTIAL CODE OUTPUT
- Generation 189: Best calculate_fitness = 1192.0
- Generation 190: Best calculate_fitness = 1192.0
- Generation 191: Best calculate_fitness = 1192.0
- Generation 192: Best calculate_fitness = 1192.0
- Regenerating population at generation 193 due to stagnation
- Generation 194: Best calculate_fitness = 1187.0
- Generation 195: Best calculate_fitness = 1187.0
- Generation 196: Best calculate_fitness = 1187.0
- Generation 197: Best calculate_fitness = 1187.0
- Generation 198: Best calculate_fitness = 1187.0
- Regenerating population at generation 199 due to stagnation
Execution Time: 19.92 seconds
Best Solution:  [0, 25, 20, 30, 29, 31, 19, 28, 11, 9, 24, 27, 3, 14, 10, 12, 18, 23, 7, 22, 5, 4, 13, 15, 2, 8, 17, 1, 6, 26, 21, 16]
Total Distance: 1187.0


### ENHANCED CODE OUTPUT
Generation 190: Best fitness = 465.0
Regenerating population at generation 191 due to stagnation
Generation 192: Best fitness = 465.0
Generation 193: Best fitness = 465.0
Generation 194: Best fitness = 465.0
Generation 195: Best fitness = 465.0
Regenerating population at generation 196 due to stagnation
Generation 197: Best fitness = 465.0
Generation 198: Best fitness = 465.0
Generation 199: Best fitness = 465.0
Execution Time: 100.05 seconds
Best Solution: [0, 14, 2, 8, 13, 30, 18, 15, 19, 11, 9, 25, 12, 10, 23, 31, 27, 16, 3, 20, 24, 28, 26, 17, 6, 29, 1, 7, 22, 4, 5, 21]
Total Distance: 465.0

### PARALLALISED AND ENHANCED CODE OUTPUT
Generation 190: Best fitness = 1477.0
Generation 191: Best fitness = 1477.0
Generation 192: Best fitness = 1477.0
Regenerating population at generation 193 due to stagnation
Generation 194: Best fitness = 1187.0
Generation 195: Best fitness = 1400.0
Generation 196: Best fitness = 1400.0
Generation 197: Best fitness = 1400.0
Generation 198: Best fitness = 1400.0
Regenerating population at generation 199 due to stagnation
Execution Time: 21.74 seconds
Best Solution: [0, 20, 15, 8, 29, 12, 27, 1, 16, 3, 14, 28, 6, 9, 21, 26, 2, 17, 22, 7, 10, 24, 25, 18, 30, 5, 11, 19, 31, 23, 13, 4]
Total Distance: 1265.0


1. Explanation of the Program
The genetic algorithm (GA) in the script solves the Traveling Salesman Problem (TSP) by finding the shortest route that visits all cities once and returns to the starting city. Key components include:
Fitness Calculation: Computes the total distance of a route, penalizing infeasible routes.
Population Generation: Creates an initial population of unique routes.
Selection: Tournament selection picks the best individuals for reproduction.
Crossover: Combines two parent routes to produce offspring.
Mutation: Introduces variability by swapping cities in the route.
Stagnation Handling: Regenerates the population if no improvement occurs over several generations.

2. Parallelization and Distribution
Parts of the algorithm that can be parallelized:
Fitness Calculation: Evaluating fitness for each individual can be done in parallel to speed up the process.
Selection: Tournament selection can be parallelized by running each tournament independently.
Crossover and Mutation: Both operations can be performed in parallel for all offspring, reducing computation time.

3. Improvements Implemented
Adaptive Mutation Rate: Dynamically adjusts the mutation rate throughout the generations to balance exploration and exploitation.
Local Search (2-opt): Refines the best route after each generation by reversing parts of the route to find better solutions.
Elitism: Ensures the best solutions from each generation are carried forward, preserving good solutions.
Stagnation Handling: Regenerates the population if no improvement occurs over multiple generations to prevent getting stuck in local optima.

4. How to implemet more cars
To add more cars to the problem, I would modify the population representation to include multiple routes, each corresponding to a different car. Each individual in the population would consist of a set of routes, with each route representing the path for a specific car, ensuring that each car starts and ends at the depot (node 0). I would then update the crossover and mutation functions to handle multiple routes within each individual, ensuring that the cars' routes are appropriately assigned during these operations. Finally, I would adjust the fitness function to evaluate the total distance traveled by all cars combined, summing the distances for each individual car’s route. 