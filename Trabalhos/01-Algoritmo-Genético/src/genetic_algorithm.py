# -*- encoding: utf8 -*-
# 1. Geração da população inicial, de tamanho N, de forma aleatória, entre -5.12 e 5.12. Sugestão N=20
# 2. Seleção por torneio 2 a 2. Lembrando que os indivíduos selecionados podem ser repetidos.
# 3. Realizar a mutação, sendo que, a taxa de mutação seja de 30 % (por exemplo, 30 a cada 100 indivíduos devem sofrer mutação).
# - Da população selecionada no item 2, você deve escolher 30 % deles e realizar uma perturbação de + ou - 5 % do valor do indivíduo. Por exemplo, selecione um indivíduo, ele deve contar x_1 e x_2:
# 1. Selecione qual variável/dimensão você deseja alterar
# 2. Selecione qual operação você irá realizar + 5 % ou - 5%
# 4. Entre os pais e filhos, escolha os novos N indivíduos, que irão para a próxima geração
# 5. Exiba a cada geração o melhor indivíduo(x e f(x))
# 6. Repita 2 a 5 até atingir o número máximo de gerações. Sugestão: 100 gerações.
# Depois do algoritmo pronto, execute-o 30 vezes. Para cada execução salve o melhor indivíduo ao final das gerações. Portanto, serão 30 indivíduos diferentes.

import copy
import math
import numpy as np
import random

import sys
sys.path.append("..")
from config import constants

def rastrigin(X):
    A = constants.RASTRIGIN_A
    return A * len(X) + sum([(x**2 - A * np.cos(2 * math.pi * x)) for x in X])

def initial_population():
    return np.random.uniform(constants.X_MIN, constants.X_MAX + 0.01, (constants.POPULATION, constants.DIMENSIONS))

def fitness_function(x):
    return abs(abs(np.min(x))-constants.X_MAX)

def select_individuals(population):
    best_individual = copy.deepcopy(population[get_best_individual_position(population)])
    selected_individuals = start_tournament(population)
    return selected_individuals, best_individual

def crossover(parent_1, parent_2):
    # Não necessário para esta entrega
    pass

def mutate(population):
    for individual in population:
        if random.random() <= constants.MUTATION_RATE:
            pos = random.randint(0, len(individual)-1)
            noise = constants.NOISE_MAX if random.randint(0, 1) == 1 else constants.NOISE_MIN
            individual[pos] += individual[pos] * noise
    return population

def update_for_next_generation(population, best_individual):
    population[get_worst_individual_position(population)] = copy.deepcopy(best_individual)
    return population


def population_has_converged(population):
    for individual in population:
        if individual != population[0]:
            return False
    return True

def start_tournament(population):
    selected_individuals = []
    for _ in range(len(population)):
        individual_1 = copy.deepcopy(population[random.randint(0, len(population)-1)])
        individual_2 = copy.deepcopy(population[random.randint(0, len(population)-1)])
        if fitness_function(individual_1) > fitness_function(individual_2):
            selected_individuals.append(individual_1)
        else:
            selected_individuals.append(individual_2)
    return selected_individuals

def get_best_individual_position(population):
    best = fitness_function(population[0])
    best_ind = 0
    for i in range(len(population)):
        if fitness_function(population[i]) > best:
            best = fitness_function(population[i])
            best_ind = i
    return best_ind

def get_worst_individual_position(population):
    worst = fitness_function(population[0])
    worst_ind = 0
    for i in range(len(population)):
        if fitness_function(population[i]) < worst:
            worst = fitness_function(population[i])
            worst_ind = i
    return worst_ind

def main():
    population = initial_population()
    print('População Inicial: ', *population, sep='\n')
    for generation in range(1, 101):
        population, best_individual = select_individuals(population)
        print('\nIndivíduos Selecionados: ', *population, sep='\n')
        population = mutate(population)
        print('\nIndivíduos Após Mutação: ', *population, sep='\n')
        population = update_for_next_generation(population, best_individual)
        print('\nIndivíduos Após Atualização: ', *population, sep='\n')
        print('\nGeração Atual: ', generation)
        print('Melhor Indivíduo: ', best_individual)

if __name__ == "__main__":
    main()