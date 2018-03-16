import random
from pyage.core.operator import Operator

class TournamentSelectionV2(Operator):
    def __init__(self, type=None, size=20, tournament_size=20, top_k=3): # we will take top_k values instead of 1 max each time
        super(TournamentSelectionV2, self).__init__()
        self.size = size
        self.tournament_size = tournament_size
        self.top_k = top_k

    def process(self, population):
        p = list(population)
        population[:] = []
        for i in range(self.size%self.top_k):
            sample = random.sample(p, self.tournament_size)
            winner = max(sample, key=lambda genotype: genotype.fitness)
            population.append(winner)
            # p.remove(winner) - maybe add later
        for i in range(self.size//self.top_k):
            sample = random.sample(p, self.tournament_size)
            for winner in self.select_max_k_fitness(sample):
                population.append(winner)
                # p.remove(winner) - maybe add later
            
    def select_max_k_fitness(self, values):
        for i in range(self.top_k):
            maxIndex = i
            maxValue = values[i]
            for j in range(i+1,self.tournament_size):
                if values[j].fitness > maxValue.fitness:
                    maxIndex = j
                    maxValue = values[j]
                    values[i],values[maxIndex]=values[maxIndex],values[i]
        return values[:self.top_k][:]