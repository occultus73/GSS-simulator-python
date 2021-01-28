import numpy as np

from demographic_information import get_segregated_populations
from graph_methods import graph_simulation_results
from iq_information import get_iq_segregated_populations

demographics = ["Whole", "White", "Black", "Male", "Female", "White_Male", "White_Female", "Black_Male", "Black_Female"]
iq_demographics = ["Above_Average_IQ", "Below_Average_IQ", "Q4_IQ", "Q3_IQ", "Q2_IQ", "Q1_IQ"]


class InformationProcessor:
    def __init__(self, trait, max_trait, min_trait, directory, actual_results, ideal_results, sterile_results):
        self.trait = trait
        self.max_trait = max_trait
        self.min_trait = min_trait
        self.dir = directory
        self.actual_results = actual_results
        self.ideal_results = ideal_results
        self.sterile_results = sterile_results

    def process_results(self):
        # Graph averages for whole population, and population broken down by demographic and/or IQ-demographic.
        demographic_pops = get_segregated_populations(self.actual_results, self.ideal_results, self.sterile_results)
        for demographic in demographics:
            self.graph_demographic(demographic, demographic_pops)

    def graph_demographic(self, dem, dem_pop):
        # Graph average for specific demographic
        graph_simulation_results(self.dir, f"Average {self.trait}, {dem}", f"Score({self.min_trait}-{self.max_trait})",
                                 [(year, np.mean([a.trait for a in year_pop]))
                                  for year, year_pop in dem_pop[f"actual_{dem}_Population"] if len(year_pop) > 100],
                                 [(year, np.mean([a.trait for a in year_pop]))
                                  for year, year_pop in dem_pop[f"ideal_{dem}_Population"] if len(year_pop) > 100],
                                 [(year, np.mean([a.trait for a in year_pop]))
                                  for year, year_pop in dem_pop[f"sterile_{dem}_Population"] if len(year_pop) > 100])

        iq_demographic_pops = get_iq_segregated_populations(dem_pop[f"actual_{dem}_Population"],
                                                            dem_pop[f"ideal_{dem}_Population"],
                                                            dem_pop[f"sterile_{dem}_Population"])
        for iq_demographic in iq_demographics:
            self.graph_iq_demographic(dem, iq_demographic, iq_demographic_pops)

    def graph_iq_demographic(self, dem, iq_dem, iq_dem_pop):
        # Graph average for specific iq_demographic
        graph_simulation_results(self.dir + "/IQ_sub-demographics",
                                 f"Average {self.trait}, {dem} {iq_dem}", f"Score({self.min_trait}-{self.max_trait})",
                                 [(year, np.mean([a.trait for a in year_pop]))
                                  for year, year_pop in iq_dem_pop[f"actual_{iq_dem}"] if len(year_pop) > 100],
                                 [(year, np.mean([a.trait for a in year_pop]))
                                  for year, year_pop in iq_dem_pop[f"ideal_{iq_dem}"] if len(year_pop) > 100],
                                 [(year, np.mean([a.trait for a in year_pop]))
                                  for year, year_pop in iq_dem_pop[f"sterile_{iq_dem}"] if len(year_pop) > 100])
