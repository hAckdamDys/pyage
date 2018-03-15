class SATEvaluation(Operator):
    def __init__(self, cnf=None): # cnf is a list of clauses f.e. [[4,1,-2],[-1,-5],[1,2],[-1]] , `-` means negative variable can't be 0
        super(SATEvaluation, self).__init__(SATGenotype)
        self.cnf=cnf
        
    def process(self, population):
        for genotype in population:
            genotype.fitness = - self.__SatCount(genotype.booleans) # we will count satisified count of clauses

    def __SatCount(self, booleans):
        count_good=0
        for clause i self.cnf:
            # now we have clause like: [4,-1,3], since clause can't have 0 we count from 1 upwards
            # [4,-1,3] means one of 4,3 needs to be true OR 1 needs to be false
            any_good=False
            for clause_num in clause:
                if  booleans[abs(clause_num)-1] == (clause_num > 0):
                    any_good=True
                    break
                count_good+=1
        return - count_good # we get negative value cause we want maximum number of clauses to fit