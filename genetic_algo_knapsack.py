import random

# Parameters for the Genetic Algorithm
population_size = 10  # Number of individuals in each generation
mutation_rate = 0.1  # Probability of mutation for each gene
generations = 100  # Number of generations to run

# Example problem data: items with weights and values
# Each item is represented as (weight, value)
items = [(10, 60), (20, 100), (30, 120)]
max_weight = 50  # Maximum weight capacity of the knapsack

# Initialize population
def initialize_population():
    # Each individual is a list of 0s and 1s representing item inclusion in the knapsack
    return [[random.choice([0, 1]) for _ in items] for _ in range(population_size)]

# Fitness function to evaluate the value of a solution
def fitness(individual):
    total_weight = total_value = 0
    for i, included in enumerate(individual):
        if included:
            total_weight += items[i][0]
            total_value += items[i][1]
    # If total weight exceeds max capacity, return 0; otherwise, return total value
    return total_value if total_weight <= max_weight else 0

# Selection function to choose the best individuals as parents
def select(population):
    # Sort population by fitness (highest first) and select the top half
    population = sorted(population, key=fitness, reverse=True)
    return population[:population_size // 2]

# Crossover function to combine genes of two parents
def crossover(parent1, parent2):
    # Randomly choose a crossover point
    point = random.randint(1, len(items) - 1)
    # Create offspring by combining parts of parents at crossover point
    return parent1[:point] + parent2[point:]

# Mutation function to introduce random changes
def mutate(individual):
    # Flip each gene with a probability equal to the mutation rate
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]  # Flip 0 to 1 or 1 to 0
    return individual

# Main Genetic Algorithm function
def genetic_algorithm():
    # Step 1: Initialize the population
    population = initialize_population()
    # Step 2: Run the algorithm for the specified number of generations
    for _ in range(generations):
        # Select the best individuals to be parents
        selected_parents = select(population)
        # Create offspring through crossover and mutation
        offspring = []
        for i in range(0, len(selected_parents), 2):
            if i + 1 < len(selected_parents):
                child1 = crossover(selected_parents[i], selected_parents[i + 1])
                child2 = crossover(selected_parents[i + 1], selected_parents[i])
                offspring.extend([mutate(child1), mutate(child2)])
        # New population is formed by combining parents and offspring
        population = selected_parents + offspring

    # After all generations, find the best solution in the final population
    best_solution = max(population, key=fitness)
    return best_solution, fitness(best_solution)

# Run the genetic algorithm and display the best solution
solution, solution_value = genetic_algorithm()
print("Best solution:", solution)
print("Best solution value:", solution_value)
