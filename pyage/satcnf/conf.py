# coding=utf-8
import logging
import os
import math

import pandas as pd
import numpy as np

from pyage.core import address
from pyage.core.agent.agent import generate_agents

from pyage.core.agent.agent import generate_agents, Agent
from pyage.core.emas import EmasService
from pyage.core.locator import GridLocator
from pyage.core.migration import ParentMigration
from pyage.core.stats.gnuplot import StepStatistics
from pyage.core.stop_condition import StepLimitStopCondition

from pyage.satcnf.crossover import SATCrossover
from pyage.satcnf.eval import SATEvaluation 
from pyage.satcnf.init import EmasInitializer, root_agents_factory, SATGenotypeInitializer, SATGenotypeInitializer2
from pyage.satcnf.mutation import Mutation
from pyage.satcnf.naming_service import NamingService
from pyage.satcnf.load_values import load_values
from pyage.satcnf.selection import TournamentSelectionV2

from pyage.solutions.evolution.selection import TournamentSelection



logger = logging.getLogger(__name__)



# cnf_data=pd.read_csv("50var-80claus-satisable.cnf",skiprows=11,header=None,sep=" ",usecols=[0,1,2]).values

cnf_data,number_of_booleans,number_of_clauses=load_values("zebra_v155_c1135.cnf")

# number_of_booleans=cnf_data.max() # 50 since clauses have values from 1 to 50, for each variable
# number_of_clauses=len(cnf_data) # 80

agents_count = 2
logger.debug("EMAS, %s agents", agents_count)

agents = generate_agents("agent", agents_count, Agent)

stop_condition = lambda: StepLimitStopCondition(100)

size = 250
seed = 0
operators = lambda: [SATEvaluation(cnf_data), TournamentSelectionV2(size=10, tournament_size=10),
                     SATCrossover(size=100, max_fitness=number_of_clauses,worse_factor=0.1), Mutation(probability=0.1, evol_probability=0.1)]
initializer = lambda: SATGenotypeInitializer2( size=size, booleans_nr=number_of_booleans, seed=seed)

address_provider = address.SequenceAddressProvider

migration = ParentMigration
locator = GridLocator

stats = lambda: StepStatistics('fitness_%s_pyage.txt' % __name__)

naming_service = lambda: NamingService(starting_number=2)
