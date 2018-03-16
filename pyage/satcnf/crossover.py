import random
import numpy as np
from pyage.core.operator import Operator
from pyage.satcnf.genotype import SATGenotype

import logging

logger = logging.getLogger(__name__)

class AbstractCrossover(Operator):
    def __init__(self, type, size):
        super(AbstractCrossover, self).__init__(type)
        self.__size = size

    def process(self, population):
        parents = list(population)
        for i in range(len(population), self.__size):
            p1, p2 = random.sample(parents, 2)
            genotype = self.cross(p1, p2)
            population.append(genotype)

class SATCrossover(AbstractCrossover):
    def __init__(self, size, max_fitness, worse_factor=0.4):
        super(SATCrossover, self).__init__(SATGenotype, size)
        self.max_fitness=max_fitness
        self.worse_factor=worse_factor # probability of taking worse fitnessed value

    def cross(self, p1, p2):
        logger.debug("Crossing:\n{0}\nAND\n{1}".format(p1, p2))
        # print("crossover!!")
        # 1. chosse better fitness
        if p2.fitness > p1.fitness:
            p1,p2 = p2,p1 # swap
        # p1 has better fitness
        # 2. make array of True,False which will determine if we take value from p1 or p2
        choose_array = np.random.rand(len(p1.booleans))<self.worse_factor
        # 3. choose values from p1 or p2 depending on choose_array
        new_booleans = np.choose(choose_array,[p1.booleans,p2.booleans])
        return SATGenotype(new_booleans)
