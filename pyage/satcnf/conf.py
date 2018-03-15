# coding=utf-8
import logging
import os
import math

from pyage.core import address

from pyage.core.agent.aggregate import AggregateAgent
from pyage.core.emas import EmasService
from pyage.core.locator import GridLocator
from pyage.core.migration import ParentMigration
from pyage.core.stats.gnuplot import StepStatistics
from pyage.core.stop_condition import StepLimitStopCondition

from pyage.satcnf.crossover import Crossover
from pyage.satcnf.eval import kApprovalEvaluator 
from pyage.satcnf._init import EmasInitializer, root_agents_factory, VotesInitializer
from pyage.satcnf.mutation import Mutation

logger = logging.getLogger(__name__)

satvalues,cnfformat = sth sthi ...alizer(number_of_cand,number_of_votes, chosen_candidate,0)()
logger.info("Initial votes:\n%s", "\n".join(map(str,satvals)))

satvals_nr = len(votes)


agents_count = 2
logger.debug("EMAS, %s agents", agents_count)
agents = root_agents_factory(agents_count, AggregateAgent)

stop_condition = lambda: StepLimitStopCondition(20000)

agg_size = 40
aggregated_agents = EmasInitializer(votes=votes, size=agg_size, energy=40 )

emas = EmasService

minimal_energy = lambda: 10
reproduction_minimum = lambda: 100
migration_minimum = lambda: 120
newborn_energy = lambda: 100
transferred_energy = lambda: 40

budget = 0
evaluation = lambda: kApprovalEvaluator(k_approval_coeff,[simple_cost_func]*votes_nr,budget, init_c_places, chosen_candidate)
crossover = lambda: Crossover(size=30)
mutation = lambda: Mutation(probability=0.1, evol_probability=0.3)

def simple_cost_func(x): return abs(x)*10


address_provider = address.SequenceAddressProvider

migration = ParentMigration
locator = GridLocator

stats = lambda: StepStatistics('fitness_%s_pyage.txt' % __name__)

naming_service = lambda: NamingService(starting_number=2)
