class SATGenotype(object):
    def __init__(self, booleans):
        super(SATGenotype, self).__init__()
        self.booleans = booleans # list of ordered bool values which will be used as variables in clauzules
        self.fitness = None # at first will say how many clauzules are correct maybe changed later