import unittest

import sys
sys.path.append("..")
from src.genetic_algorithm import rastrigin, initial_population, fitness_function, start_tournament, update_for_next_generation
from src.genetic_algorithm import get_best_individual_position, get_worst_individual_position, population_has_converged
from config import constants

class TestGeneticAlgorithm(unittest.TestCase):
    
    def test_rastrigin_returns_0_if_0(self):
        expected = 0
        result = rastrigin([0])
        self.assertEqual(expected, result)

    def test_initial_population_returns_correct_number_individuals(self):
        expected = constants.POPULATION
        result = len(initial_population())
        self.assertEqual(expected, result)

    def test_fitness_function_0_better_than_1(self):
        self.assertGreater(fitness_function([0]), fitness_function([1]))
    
    def test_fitness_function_0_1_better_than_5_1(self):
        self.assertGreater(fitness_function([0, 1]), fitness_function([5, 1]))

    def test_get_best_individual_position_0(self):
        self.assertEqual(0, get_best_individual_position([0, 1, 5]))

    def test_get_best_individual_position_2(self):
        self.assertEqual(2, get_worst_individual_position([0, 1, 5]))

    def test_population_has_converged_true(self):
        self.assertTrue(population_has_converged([[0, 0], [0, 0]]))

    def test_update_for_next_generation_1_for_0(self):
        self.assertEqual([[0, 0], [0, 0]], update_for_next_generation([[0, 0], [1, 1]], [0, 0]))

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    unittest.main()

if __name__ == '__main__':
    unittest.main()