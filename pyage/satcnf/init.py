import random
from pyage.core.emas import EmasAgent
from pyage.core.operator import Operator
from pyage.satcnf.genotype import SATGenotype
from pyage.core.inject import Inject

class EmasInitializer(object):

    def __init__(self,booleans, energy, size):
        self.booleans = booleans
        self.energy = energy
        self.size = size

    @Inject("naming_service")
    def __call__(self):
        agents = {}
        for i in range(self.size):
            agent = EmasAgent(SATGenotype(self.booleans), self.energy, self.naming_service.get_next_agent())
            agents[agent.get_address()] = agent
        return agents 

    

def root_agents_factory(count, type):
    def factory():
        agents = {}
        for i in range(count):
            agent = type('R' + str(i))
            agents[agent.get_address()] = agent
        return agents

    return factory

class SATGenotypeInitializer(object):

    def __init__(self, booleans_nr, seed):
        self.booleans_nr = booleans_nr
        random.seed(seed)

    def __call__(self):
        np.random.seed(0)
        np.random.choice(a=[False, True], size=self.booleans_nr)