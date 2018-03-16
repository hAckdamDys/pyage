class SATGenotype(object):
    def __init__(self, booleans):
        super(SATGenotype, self).__init__()
        self.booleans = list(booleans) # list of ordered bool values which will be used as variables in clauzules
        self.fitness = None # at first will say how many clauzules are correct maybe changed later
        
    def __str__(self):
        return "{0}\nfitness: {1}".format("\n".join(map(str,self.booleans)), self.fitness)
        