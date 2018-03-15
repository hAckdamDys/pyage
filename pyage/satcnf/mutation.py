import logging
import random
from pyage.core.operator import Operator
from pyage.satcnf.genotype import SATGenotype

logger = logging.getLogger(__name__)

class AbstractMutation(Operator):
    def __init__(self, type, probability):
        super(AbstractMutation, self).__init__()
        self.probability = probability

    def process(self, population):
        for genotype in population:
            if random.random() < self.probability:
                self.mutate(genotype)

class Mutation(AbstractMutation):
    def __init__(self, probability, evol_probability):
        super(Mutation, self).__init__(SATGenotype, evol_probability)
        self.probability = probability

    def mutate(self, genotype):
        logger.debug("Mutating genotype: {0}".format(genotype))
        for i in range(len(genotype.booleans)):
            rand = random.random()
            if rand < self.probability:
                genotype.booleans[i]=not genotype.booleans[i]



