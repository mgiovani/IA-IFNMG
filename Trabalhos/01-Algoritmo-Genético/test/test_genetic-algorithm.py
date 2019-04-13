import unittest

from src.genetic_algorithm import rastrigin, initial_population, fitness_function
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

if __name__ == '__main__':
    unittest.main()