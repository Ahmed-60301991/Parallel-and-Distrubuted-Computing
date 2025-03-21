# import numpy as np
# import pandas as pd
# from genetic_algorithms_functions import calculate_fitness, \
#     select_in_tournament, order_crossover, mutate, \
#     generate_unique_population


# # Load the distance matrix
# distance_matrix = pd.read_csv('city_distances.csv').to_numpy()

# # Parameters
# num_nodes = distance_matrix.shape[0]
# population_size = 10000
# num_tournaments = 4  # Number of tournaments to run
# mutation_rate = 0.1
# num_generations = 200
# infeasible_penalty = 1e6  # Penalty for infeasible routes
# stagnation_limit = 5  # Number of generations without improvement before regeneration


# # Generate initial population: each individual is a route starting at node 0
# np.random.seed(42)  # For reproducibility
# population = generate_unique_population(population_size, num_nodes)

# # Initialize variables for tracking stagnation
# best_calculate_fitness = int(1e6)
# stagnation_counter = 0
# import time

# start_time = time.time()  # Start timing

# # Main GA loop
# for generation in range(num_generations):
#     # Evaluate calculate_fitness
#     calculate_fitness_values = np.array([calculate_fitness(route, distance_matrix) for route in population])

#     # Check for stagnation
#     current_best_calculate_fitness = np.min(calculate_fitness_values)
#     if current_best_calculate_fitness < best_calculate_fitness:
#         best_calculate_fitness = current_best_calculate_fitness
#         stagnation_counter = 0
#     else:
#         stagnation_counter += 1

#     # Regenerate population if stagnation limit is reached, keeping the best individual
#     if stagnation_counter >= stagnation_limit:
#         print(f"Regenerating population at generation {generation} due to stagnation")
#         best_individual = population[np.argmin(calculate_fitness_values)]
#         population = generate_unique_population(population_size - 1, num_nodes)
#         population.append(best_individual)
#         stagnation_counter = 0
#         continue  # Skip the rest of the loop for this generation

#     # Selection, crossover, and mutation
#     selected = select_in_tournament(population,
#                                     calculate_fitness_values)
#     offspring = []
#     for i in range(0, len(selected), 2):
#         parent1, parent2 = selected[i], selected[i + 1]
#         route1 = order_crossover(parent1[1:], parent2[1:])
#         offspring.append([0] + route1)
#     mutated_offspring = [mutate(route, mutation_rate) for route in offspring]

#     # Replacement: Replace the individuals that lost in the tournaments with the new offspring
#     for i, idx in enumerate(np.argsort(calculate_fitness_values)[::-1][:len(mutated_offspring)]):
#         population[idx] = mutated_offspring[i]

#     # Ensure population uniqueness
#     unique_population = set(tuple(ind) for ind in population)
#     while len(unique_population) < population_size:
#         individual = [0] + list(np.random.permutation(np.arange(1, num_nodes)))
#         unique_population.add(tuple(individual))
#     population = [list(individual) for individual in unique_population]

#     # Print best calculate_fitness
#     print(f"Generation {generation}: Best calculate_fitness = {current_best_calculate_fitness}")

# # Update calculate_fitness_values for the final population
# calculate_fitness_values = np.array([calculate_fitness(route, distance_matrix) for route in population])
# end_time = time.time()  # Stop timing
# print(f"Execution Time: {end_time - start_time:.2f} seconds")

# # Output the best solution
# best_idx = np.argmin(calculate_fitness_values)
# best_solution = population[best_idx]
# print("Best Solution:", best_solution)
# print("Total Distance:", calculate_fitness(best_solution, distance_matrix))

import numpy as np
import pandas as pd
from genetic_algorithms_functions import calculate_fitness, select_in_tournament, order_crossover, mutate, generate_unique_population, adaptive_mutation_rate, local_search

# Load the distance matrix
distance_matrix = pd.read_csv('city_distances.csv').to_numpy()

# Parameters
elitism_size = 2
num_nodes = distance_matrix.shape[0]
population_size = 10000
num_tournaments = 4  # Number of tournaments to run
mutation_rate = 0.1
num_generations = 200
infeasible_penalty = 1e6  # Penalty for infeasible routes
stagnation_limit = 5  # Number of generations without improvement before regeneration

# Generate initial population
np.random.seed(42)
population = generate_unique_population(population_size, num_nodes)
best_fitness = float('inf')
stagnation_counter = 0

import time
start_time = time.time()

# Main GA loop
for generation in range(num_generations):
    fitness_values = np.array([calculate_fitness(route, distance_matrix) for route in population])
    current_best_fitness = np.min(fitness_values)
    
    # Track Best Solution
    if current_best_fitness < best_fitness:
        best_fitness = current_best_fitness
        stagnation_counter = 0
    else:
        stagnation_counter += 1

    if stagnation_counter >= stagnation_limit:
        print(f"Regenerating population at generation {generation} due to stagnation")
        best_individual = population[np.argmin(fitness_values)]
        population = generate_unique_population(population_size - 1, num_nodes)
        population.append(best_individual)
        stagnation_counter = 0
        continue

    # Adaptive mutation rate
    mutation_rate = adaptive_mutation_rate(generation, num_generations)

    # Elitism
    elite_indices = np.argsort(fitness_values)[:elitism_size]
    elite = [population[i] for i in elite_indices]

    # Selection and Crossover
    selected = select_in_tournament(population, fitness_values)
    offspring = []
    for i in range(0, len(selected), 2):
        parent1, parent2 = selected[i], selected[i + 1]
        child = order_crossover(parent1[1:], parent2[1:])
        offspring.append([0] + child)

    # Mutation
    mutated_offspring = [mutate(route, mutation_rate) for route in offspring]

    # Local Search on Best Individual
    best_idx = np.argmin(fitness_values)
    population[best_idx] = local_search(population[best_idx], distance_matrix)

    # Replacement with Elitism
    for i in range(elitism_size):
        population[np.argmax(fitness_values)] = elite[i]

    # Print progress
    print(f"Generation {generation}: Best fitness = {current_best_fitness}")

end_time = time.time()
print(f"Execution Time: {end_time - start_time:.2f} seconds")

# Output best solution
fitness_values = np.array([calculate_fitness(route, distance_matrix) for route in population])
best_idx = np.argmin(fitness_values)
best_solution = population[best_idx]
print("Best Solution:", best_solution)
print("Total Distance:", calculate_fitness(best_solution, distance_matrix))
