# coding=utf-8
import logging
import os
import math

import pandas as pd
import numpy as np

from pyage.core import address

from pyage.core.agent.aggregate import AggregateAgent
from pyage.core.emas import EmasService
from pyage.core.locator import GridLocator
from pyage.core.migration import ParentMigration
from pyage.core.stats.gnuplot import StepStatistics
from pyage.core.stop_condition import StepLimitStopCondition

from pyage.satcnf.crossover import SATCrossover
from pyage.satcnf.eval import SATEvaluation 
from pyage.satcnf.init import EmasInitializer, root_agents_factory, SATGenotypeInitializer
from pyage.satcnf.mutation import Mutation
from pyage.satcnf.naming_service import NamingService

logger = logging.getLogger(__name__)



cnf_data=pd.read_csv("50var-80claus-satisable.cnf",skiprows=11,header=None,sep=" ",usecols=[0,1,2]).values

number_of_booleans=cnf_data.max() # 50 since clauses have values from 1 to 50, for each variable
number_of_clauses=len(cnf_data) # 80

seed=0
booleans=SATGenotypeInitializer(number_of_booleans,0)()


logger.info("Initial booleans:\n%s", "\n".join(map(str,booleans)))


agents_count = 2
logger.debug("EMAS, %s agents", agents_count)
agents = root_agents_factory(agents_count, AggregateAgent)



stop_condition = lambda: StepLimitStopCondition(20000)

agg_size = 40
aggregated_agents = EmasInitializer(booleans=booleans, size=agg_size, energy=40 )

emas = EmasService

minimal_energy = lambda: 10
reproduction_minimum = lambda: 100
migration_minimum = lambda: 120
newborn_energy = lambda: 100
transferred_energy = lambda: 40

evaluation = lambda: SATEvaluation(cnf_data)
crossover = lambda: SATCrossover(size=30,max_fitness=number_of_clauses)
mutation = lambda: Mutation(probability=0.1, evol_probability=0.3)

def simple_cost_func(x): return abs(x)*10


address_provider = address.SequenceAddressProvider

migration = ParentMigration
locator = GridLocator

stats = lambda: StepStatistics('fitness_%s_pyage.txt' % __name__)

naming_service = lambda: NamingService(starting_number=2)
