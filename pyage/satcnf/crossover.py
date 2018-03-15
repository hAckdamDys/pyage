import random
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
    def __init__(self, size):
        super(Crossover, self).__init__(SATGenotype, size)

    def cross(self, p1, p2):
        logger.debug("Crossing:\n{0}\nAND\n{1}".format(p1, p2))
        division = random.randint(1, len(p1.booleans)-2)
        new_booleans = p1.booleans[:division] + p2.booleans[division:]
        return SATGenotype(new_booleans)
