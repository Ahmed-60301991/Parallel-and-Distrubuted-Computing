# ####SEQUENTIAL CODE
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
#     calculate_fitness_values = np.array([-calculate_fitness(route, distance_matrix) for route in population])

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
# calculate_fitness_values = np.array([-calculate_fitness(route, distance_matrix) for route in population])
# end_time = time.time()  # Stop timing
# print(f"Execution Time: {end_time - start_time:.2f} seconds")

# # Output the best solution
# best_idx = np.argmin(calculate_fitness_values)
# best_solution = population[best_idx]
# print("Best Solution:", best_solution)
# print("Total Distance:", -calculate_fitness(best_solution, distance_matrix))


"""
Genetic Algorithm for Solving the Traveling Salesman Problem (Parallelized Version)
----------------------------------------------------------------
"""

import numpy as np
import pandas as pd
import multiprocessing
from genetic_algorithms_functions import (
    calculate_fitness, select_in_tournament, order_crossover, mutate, 
    generate_unique_population, adaptive_mutation_rate, local_search
)

# Load the distance matrix from CSV
distance_matrix = pd.read_csv('city_distances.csv').to_numpy()

# Genetic Algorithm Parameters
elitism_size = 2  # Number of elite individuals retained each generation
num_nodes = distance_matrix.shape[0]  # Number of cities
population_size = 10000  # Total number of routes in the population
num_tournaments = 4  # Number of tournaments for selection
mutation_rate = 0.1  # Probability of mutation
num_generations = 200  # Maximum number of generations
stagnation_limit = 5  # Number of generations without improvement before regenerating population

# Initialize population
np.random.seed(42)  # Ensures reproducibility
population = generate_unique_population(population_size, num_nodes)
best_fitness = float('inf')  # Initialize best fitness
stagnation_counter = 0  # Tracks stagnation count

import time
start_time = time.time()  # Start execution timer

# Set up multiprocessing pool for parallel execution
pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

# Main Genetic Algorithm loop
for generation in range(num_generations):
    """
    This loop runs the genetic algorithm for the specified number of generations.
    It includes fitness evaluation, selection, crossover, mutation, local search,
    and population regeneration in case of stagnation.
    """

    # Parallelized Fitness Calculation
    fitness_values = np.array([-calculate_fitness(route, distance_matrix) for route in population])
    current_best_fitness = np.min(fitness_values)
    
    # Track Best Solution and Handle Stagnation
    if current_best_fitness < best_fitness:
        best_fitness = current_best_fitness
        stagnation_counter = 0  # Reset stagnation if improvement occurs
    else:
        stagnation_counter += 1  # Increase stagnation counter if no improvement

    # Regenerate population if stagnation limit is reached
    if stagnation_counter >= stagnation_limit:
        print(f"Regenerating population at generation {generation} due to stagnation")
        best_individual = population[np.argmin(fitness_values)]
        population = generate_unique_population(population_size - 1, num_nodes)
        population.append(best_individual)
        stagnation_counter = 0
        continue

    # Adjust mutation rate dynamically
    mutation_rate = adaptive_mutation_rate(generation, num_generations)

    # Implement Elitism (Retain top individuals)
    elite_indices = np.argsort(fitness_values)[:elitism_size]
    elite = [population[i] for i in elite_indices]

    # Selection and Crossover (Parallelized Crossover)
    selected = select_in_tournament(population, fitness_values)
    offspring = pool.starmap(order_crossover, [(selected[i][1:], selected[i + 1][1:]) for i in range(0, len(selected), 2)])
    offspring = [[0] + child for child in offspring]  # Ensure starting city is 0

    # Mutation (Parallelized)
    mutated_offspring = pool.starmap(mutate, [(route, mutation_rate) for route in offspring])

    # Local Search (Parallelized)
    best_idx = np.argmin(fitness_values)
    population[best_idx] = pool.apply(local_search, (population[best_idx], distance_matrix))

    # Replacement with Elitism (Preserve best individuals)
    for i in range(elitism_size):
        population[np.argmax(fitness_values)] = elite[i]

    # Print progress
    print(f"Generation {generation}: Best fitness = {current_best_fitness}")

# Execution time tracking
end_time = time.time()
print(f"Execution Time: {end_time - start_time:.2f} seconds")

# Final evaluation and best solution output
fitness_values = np.array([-calculate_fitness(route, distance_matrix) for route in population])
best_idx = np.argmin(fitness_values)
best_solution = population[best_idx]
print("Best Solution:", best_solution)
print("Total Distance:", -calculate_fitness(best_solution, distance_matrix))

# Close multiprocessing pool
pool.close()
pool.join()
