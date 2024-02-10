import os
import cv2
import numpy as np
import random

def initialize_population(population_size):
    population = []
    folder_path = "output"
    for filename in os.listdir(folder_path):
        image_path = os.path.join(folder_path, filename)
        image = cv2.imread(image_path)
        chromosome = np.asarray(image)
        population.append(chromosome)
    return population


def evaluate_fitness(chromosome):
  

    fitness_score = 0
    return fitness_score


def crossover(parent1, parent2, crossover_rate):
    if random.random() < crossover_rate:
        crossover_point = random.randint(0, len(parent1))
        child = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]), axis=0)
    else:
        child = parent1
    return child


def mutate(chromosome, mutation_rate):
    mutated_chromosome = chromosome.copy()
    for i in range(len(mutated_chromosome)):
        if random.random() < mutation_rate:
            
            mutated_chromosome[i] = random.randint(0, 255)
    return mutated_chromosome


def selection(population, num_parents):
    fitness_scores = [evaluate_fitness(chromosome) for chromosome in population]
    parents = []
    for _ in range(num_parents):
        max_fitness_index = np.argmax(fitness_scores)
        parents.append(population[max_fitness_index])
        fitness_scores[max_fitness_index] = -1  
    return parents


def genetic_algorithm(population_size, num_parents, offspring_size, mutation_rate, crossover_rate, num_generations):
    population = initialize_population(population_size)
    for generation in range(num_generations):
        parents = selection(population, num_parents)
        offspring = []
        for _ in range(offspring_size):
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)
            child = crossover(parent1, parent2, crossover_rate)
            child = mutate(child, mutation_rate)
            offspring.append(child)
        population = parents + offspring
    return population


population_size = 50
num_parents = 10
offspring_size = 10
mutation_rate = 0.1
crossover_rate = 0.8
num_generations = 100

final_population = genetic_algorithm(population_size, num_parents, offspring_size, mutation_rate, crossover_rate, num_generations)


output_folder = "output"
for i, chromosome in enumerate(final_population):
    image_path = os.path.join(output_folder, f"output_{i}.jpg")
    cv2.imwrite(image_path, chromosome)